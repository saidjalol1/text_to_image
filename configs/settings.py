import os
from decouple import config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.makedirs(os.path.join(BASE_DIR, "media"), exist_ok=True)

# API confs
API_URL = config("API_URL")
REQUEST_HEADERS = {config("HEADER"): f"{config('TOKEN_TYPE')} {config('HUGGING_FACE_TOKEN')}"}


# Bot conf
TOKEN =  config("BOT_TOKEN")