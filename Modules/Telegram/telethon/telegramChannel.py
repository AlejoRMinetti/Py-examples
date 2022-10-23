import configparser
import json
import asyncio
from datetime import date, datetime

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)


# some functions to parse json date
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)


# main class to access to channel
class TelegramChannel():
    def __init__(self, urlChannel=None) -> None:
        self.urlChannel = urlChannel

    def connect(self):
        # Reading Configs
        config = configparser.ConfigParser()
        config.read("config.ini")

        # Setting configuration values
        api_id = config['Telegram']['api_id']
        api_hash = config['Telegram']['api_hash']
        api_hash = str(api_hash)

        self.phone = config['Telegram']['phone']
        self.username = config['Telegram']['username']

        # Create the client and connect
        print('connecting to telegram as:',self.username)
        if config['Telegram'].get('proxyUrl'):
            print('connecting using proxy...',config['Telegram']['proxyMethod'],
                                         config['Telegram']['proxyUrl'],
                                         config['Telegram']['proxyPort'])
            self.client = TelegramClient(self.username, api_id, api_hash,
                                         proxy=(config['Telegram']['proxyMethod'],
                                         config['Telegram']['proxyUrl'],
                                         int(config['Telegram']['proxyPort'])))
        else:
            self.client = TelegramClient(self.username, api_id, api_hash)

    async def getLastMessage(self,add_offset=0):
        await self.client.start()
        # print("Client Created")
        # Ensure you're authorized
        if await self.client.is_user_authorized() == False:
            await self.client.send_code_request(self.phone)
            try:
                await self.client.sign_in(self.phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                await self.client.sign_in(password=input('Password: '))

        self.me = await self.client.get_me()

        if self.urlChannel == None:
            self.urlChannel = input('enter entity(telegram URL or entity id):')

        if self.urlChannel.isdigit():
            entity = PeerChannel(int(self.urlChannel))
        else:
            entity = self.urlChannel

        self.my_channel = await self.client.get_entity(entity)

        self.offset_id = 0
        all_messages = []
        self.total_messages = 0

        history = await self.client(GetHistoryRequest(
            peer=self.my_channel,
            offset_id=self.offset_id,
            offset_date=None,
            add_offset=add_offset,
            limit=1,
            max_id=0,
            min_id=0,
            hash=0
        ))
        return history.messages


    async def getMessagesToJSON(self, total_count_limit=200):
        # total_count_limit = 0 (no limit, get all messages)

        await self.client.start()
        print("Client Created")
        # Ensure you're authorized
        if await self.client.is_user_authorized() == False:
            await self.client.send_code_request(self.phone)
            try:
                await self.client.sign_in(self.phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                await self.client.sign_in(password=input('Password: '))

        self.me = await self.client.get_me()

        if self.urlChannel == None:
            self.urlChannel = input('enter entity(telegram URL or entity id):')

        if self.urlChannel.isdigit():
            entity = PeerChannel(int(self.urlChannel))
        else:
            entity = self.urlChannel

        self.my_channel = await self.client.get_entity(entity)

        self.total_count_limit = total_count_limit
        self.offset_id = 0
        if total_count_limit < 100:
            limit = total_count_limit
        else:
            limit = 100
        all_messages = []
        self.total_messages = 0

        while True:
            print("Current Offset ID is:", self.offset_id, "; Total Messages:", self.total_messages)
            history = await self.client(GetHistoryRequest(
                peer=self.my_channel,
                offset_id=self.offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))
            if not history.messages:
                print("No more messages, Current Offset ID is:", self.offset_id, "; Total Messages:", self.total_messages)
                break
            messages = history.messages
            for message in messages:
                all_messages.append(message.to_dict())
            self.offset_id = messages[len(messages) - 1].id
            self.total_messages = len(all_messages)
            if self.total_count_limit != 0 and self.total_messages >= self.total_count_limit:
                print("Limite reached, Current Offset ID is:", self.offset_id, "; Total Messages:", self.total_messages)
                break

        with open('channel_messages.json', 'w') as outfile:
            json.dump(all_messages, outfile, cls=DateTimeEncoder)
    
    

if __name__ == "__main__":
    goldChannel = TelegramChannel("https://t.me/gold_forexinvest")
    goldChannel.connect()
    with goldChannel.client:
            goldChannel.client.loop.run_until_complete(goldChannel.getMessages(5))

    
