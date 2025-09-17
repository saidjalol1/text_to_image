FROM python:3.10-slim


WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


ENV PYTHONUNBUFFERED=1

# Start the bot
CMD ["python", "main.py"]
