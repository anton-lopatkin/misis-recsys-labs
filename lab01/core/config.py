import os
from dotenv import load_dotenv

load_dotenv()

def get_hf_token() -> str:
    token: str = os.getenv('HF_TOKEN')
    if not token:
        raise RuntimeError('HF_TOKEN is not set. Create a .env file (see .env.example)')
    return token
