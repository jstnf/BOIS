import os
from dotenv import load_dotenv
import discord
import audioread
from asyncio import sleep

# .env
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
MEMBER = os.getenv('MEMBER_ID')
SOUND_FILE_PATH = os.getenv('SOUND_FILE_PATH')

class BoisBot(discord.Client):
    async def on_voice_state_update(self, member, before, after):
        vc_before = before.channel
        vc_after = after.channel

        if not vc_before and int(member.id) == int(MEMBER):
            vc = await vc_after.connect()
            vc.play(discord.FFmpegPCMAudio(SOUND_FILE_PATH))
            with audioread.audio_open(SOUND_FILE_PATH) as f:
                # Start Playing
                await sleep(f.duration + 5)  # Allow a bit of time for song to load :D
            await vc.disconnect()

intents = discord.Intents.default()
intents.voice_states = True

client = BoisBot(intents = intents)
client.run(TOKEN)
