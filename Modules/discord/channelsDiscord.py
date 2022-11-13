import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents = intents)
guild = discord.Guild
messages =  []


print("Bot started")
@client.event
async def on_message(message):
    
    channelIDsToListen = [ 1034160983612076124, 592446624882491402 ] # put the channels that you want to listen to here

    if message.channel.id in channelIDsToListen:

        if message.content != "" :
 
            messages.append(message.content)

        print("New message: " + message.content)
    
client.run('MTAzNjI0OTkwNzYzNzUyMjQ1Mg.G0H1u9.d4XQiSqm7myx1OCidC706XXHU9sQ_d46Qqp4G4')