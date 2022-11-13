# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print("New message: ",message)
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTAzNjI0OTkwNzYzNzUyMjQ1Mg.G0H1u9.d4XQiSqm7myx1OCidC706XXHU9sQ_d46Qqp4G4')
