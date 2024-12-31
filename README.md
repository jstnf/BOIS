# BOIS [![](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
> Inspired by Ludwig's popcorn castle "BOIS!" video intro.

BOIS is a Discord bot that plays a sound when you join a voice channel.

The bot was implemented before Discord allowed Nitro users to play a sound from a server soundboard when joining.

## How to use
### Creating a Discord app (bot)
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give it a name.
3. Go to the "Bot" tab and click "Add Bot".
4. Copy the token and save it for later.
5. Go to the "OAuth2" tab and select the "bot" scope.
6. Select the `View Channels`, `Connect`, and `Speak` permissions. Copy the generated URL and paste it into your browser.
7. Select the server you want to add the bot to and click "Authorize".

### Pre-Setup
1. Clone the repository

   ```bash
   git clone https://github.com/jstnf/BOIS/
   ```
2. Using `example.env` as a template, create a `.env` file in the root directory of the project and fill in the fields.

   ```bash
   cp example.env .env
   ```
   ### Environment Variables
   | Field             | Description                        |
   |-------------------|------------------------------------|
   | `BOT_TOKEN`       | The token of your Discord bot      |
   | `MEMBER_ID`       | The ID of the user joining VC      |
   | `SOUND_FILE_PATH` | The OS file path to the sound file |

### Easy Setup (Docker + Makefile) 
If you have Docker and `make` installed, you can use the following commands to run the bot.

| Command       | Description                                                                               |
|---------------|-------------------------------------------------------------------------------------------|
| `make docker` | Builds the Docker image. The image is tagged as `bois`.                                   |
| `make run`    | Runs the Docker container. The command will look for a `.env` file in the repo directory. |

### Manual Setup
You can also use the following instructions to set up your own Python environment and run the BOIS bot.
1. Install FFmpeg

   [FFmpeg](https://ffmpeg.org/) is a well-known, open-source audio processor. BOIS uses
   [discord.py](https://discordpy.readthedocs.io/en/latest/api.html?highlight=audio#ffmpegpcmaudio) which requires
   FFmpeg in order to play audio.
2. Create a Python virtual environment and install `requirements.txt`

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the bot!

   ```bash
   python bois/main.py
   ```
