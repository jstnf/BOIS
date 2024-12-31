FROM python:3.10-slim

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean

WORKDIR /app
COPY bin /app/bin
COPY bois /app/bois
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "bois/main.py"]