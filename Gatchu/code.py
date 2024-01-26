import discord as ds
import asyncio

intent = ds.Intents.default()
intent.message_content = True
client = ds.Client(intents=intent)
memes = ["3alawi","haaa"]

@client.event 
async def on_ready():
    print("Bot is online. {0.user}".format(client))


@client.event 
async def on_message(msg):
    if msg.author==client.user:
        return
    else:
        for word in msg.content.split(" "):
            if word.strip() in memes:
                VoiceChannelID = open("VoiceChannelID",'r')
                channel = client.get_channel(int(VoiceChannelID.read().strip()))
                connection = await channel.connect()
                connection.play(ds.FFmpegPCMAudio("./memes/"+word+".mp3"))

                while connection.is_playing():
                    await asyncio.sleep(1)

                await connection.disconnect()

token = open("token",'r')
client.run(token.read().strip())
