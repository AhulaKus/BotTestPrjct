import httpx
from config import HF_TOKEN

MODEL_URL = "https://router.huggingface.co/v1/chat/completions"

async def get_meme_text(topic:str) -> str:
    prompt = (
        f"Придумай короткий смешной текст для мема на тему: {topic}. "
        f"До 10 слов. Без пояснений, только сам текст мема."
    )
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "Qwen/Qwen3-Coder-480B-A35B-Instruct:cerebras",
    }


    async with httpx.AsyncClient() as client:
        resp = await client.post(MODEL_URL, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        result = resp.json()
        # Достаем текст:
        return result["choices"][0]["message"]["content"].strip()
