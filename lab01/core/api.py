import requests
from typing import Any, Dict, TypedDict

ROUTER_BASE: str = "https://router.huggingface.co/hf-inference/models/"

class Response(TypedDict, total=False):
    error: bool
    message: str
    status_code: int
    raw: Any


def query_model(model_id: str, text: str, hf_token: str) -> Response:
    """
    Отправляет текст в модель Hugging Face и возвращает ответ.

    Args:
        model_id (str): Идентификатор модели Hugging Face.
        text (str): Входной текст для анализа.
        hf_token (str): Токен Hugging Face.

    Returns:
        ModelResponse: Результат запроса с полями 'error', 'message', 'status_code', 'raw'.
    """

    url: str = ROUTER_BASE + model_id
    headers: Dict[str, str] = {"Authorization": f"Bearer {hf_token}"}
    payload: Dict[str, str] = {"inputs": text}

    try:
        resp: requests.Response = requests.post(url, headers=headers, json=payload, timeout=20)
    except requests.RequestException as e:
        return {"error": True, "message": f"Request failed: {e}"}

    if resp.status_code != 200:
        return {"error": True, "status_code": resp.status_code, "message": resp.text}

    try:
        data: Any = resp.json()
    except ValueError:
        return {"error": True, "message": "Invalid JSON response"}

    return {"error": False, "raw": data[0]}
