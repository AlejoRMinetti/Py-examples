from telethon import TelegramClient, events
import configparser

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
# api_hash = str(api_hash)
phone = config['Telegram']['phone']
username = config['Telegram']['username']

def on(self: 'TelegramClient', event: events.NewMessage):
        """
        Decorator used to `add_event_handler` more conveniently.
        Arguments
            event (`_EventBuilder` | `type`):
                The event builder class or instance to be used,
                for instance ``events.NewMessage``.
        Example
            .. code-block:: python
                from telethon import TelegramClient, events
                client = TelegramClient(...)
                # Here we use client.on
                @client.on(events.NewMessage)
                async def handler(event):
                    ...
        """
        def decorator(f):
            self.add_event_handler(f, event)
            return f

        return decorator 

with TelegramClient(username, api_id, api_hash) as client:
    # Here we use client.on
    @client.on(events.NewMessage)
    async def handler(event):
        print(event.raw_text)

    client.start()
    client.run_until_disconnected()