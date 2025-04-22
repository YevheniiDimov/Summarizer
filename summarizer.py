from models import SummarizeRequest, SummarizeResponse
from fastapi import HTTPException
from dotenv import load_dotenv
import requests
import json
import os


# Load API Token from the .env file
load_dotenv()
MODEL_API_TOKEN = os.getenv('model-api-token')
MODEL_API_URL = os.getenv('openai-compatible-model-url')


def summarize_text(request: SummarizeRequest) -> SummarizeResponse:
    body = {
        "model": request.model,
        "messages": [
            {
                "role": "system", 
                "content": "Summarize the following text: " + request.text
            }
        ],
        "max_tokens": request.limit,
        "temperature": request.temperature
    }

    if MODEL_API_TOKEN != None:
        body.update({"api-key": MODEL_API_TOKEN})

    response = requests.post(MODEL_API_URL + "/chat/completions", json=body)
    result = json.loads(response.text)

    try:
        return SummarizeResponse(http_response=str(response.status_code), text=result["choices"][0]["message"]["content"])
    except KeyError:
        raise HTTPException(status_code=500, detail="Error: your model does not require an API key, set it to \"None\"")