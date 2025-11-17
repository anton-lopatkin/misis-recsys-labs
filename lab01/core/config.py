import os
from dotenv import load_dotenv

load_dotenv()

def get_hf_token() -> str:
    """
    Получает токен Hugging Face из переменных окружения.

    Raises:
        RuntimeError: если токен не найден.
    Returns:
        str: токен Hugging Face.
    """
    token: str = os.getenv('HF_TOKEN')
    if not token:
        raise RuntimeError('HF_TOKEN is not set. Create a .env file (see .env.example)')
    return token
