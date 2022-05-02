import os
from dotenv import load_dotenv
import discord
import audioread
from asyncio import sleep

# .env
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
MEMBER = os.getenv('MEMBER_ID')
PATH = os.getenv('FILE_PATH')

bot = discord.Bot()

@bot.event
async def on_voice_state_update(member, before, after):
    vc_before = before.channel
    vc_after = after.channel
    
    if not vc_before and int(member.id) == int(MEMBER):
        vc = await vc_after.connect()
        vc.play(discord.FFmpegPCMAudio(PATH))
        with audioread.audio_open(PATH) as f:
            #Start Playing
            await sleep(f.duration + 5) # Allow a bit of time for song to load :D
        await vc.disconnect()

bot.run(TOKEN)