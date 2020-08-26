import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("등록"):
        await message.channel.send("등록되었습니다")
        
        

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
