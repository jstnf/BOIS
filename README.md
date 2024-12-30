# BOIS [![](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
> Inspired by Ludwig's popcorn castle "BOIS!" video intro.

BOIS is a Discord bot that plays a sound when you join a voice channel.

The bot was implemented before Discord allowed Nitro users to play a sound from a server soundboard when joining. 

## How to use
Use the following instructions to set up and run your own BOIS bot.
1. Clone the repository

   ```bash
   git clone https://github.com/jstnf/BOIS/
   ```
2. Install FFmpeg

   [FFmpeg](https://ffmpeg.org/) is a well-known, open-source audio processor. BOIS uses
   [discord.py](https://discordpy.readthedocs.io/en/latest/api.html?highlight=audio#ffmpegpcmaudio) which requires
   FFmpeg in order to play audio.
3. Create a Python virtual environment and install `requirements.txt`

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Create a Discord bot and invite it to your server.

   The Discord bot requires the following permissions:
   - Bot
     - View Channels
     - Connect
     - Speak
5. Using `example.env` as a template, create a `.env` file in the root directory of the project and fill in the fields.

   ```bash
   cp example.env .env
   ```
   ### Environment Variables
   | Field             | Description                        |
   |-------------------|------------------------------------|
   | `BOT_TOKEN`       | The token of your Discord bot      |
   | `MEMBER_ID`       | The ID of the user joining VC      |
   | `SOUND_FILE_PATH` | The OS file path to the sound file |
6. Run the bot!

   ```bash
   python bot.py
   ```
