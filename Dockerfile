FROM python:3.10-slim

# Install ffmpeg and git
RUN apt-get update && \
    apt-get install -y ffmpeg git build-essential libffi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy application files
COPY bin /app/bin
COPY bois /app/bois
COPY requirements.txt /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Clone and install discord.py with voice support
RUN git clone https://github.com/Rapptz/discord.py && \
    cd discord.py && \
    pip install --no-cache-dir -U ".[voice]"

CMD ["python", "bois/main.py"]