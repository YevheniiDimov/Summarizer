from huggingface_hub import InferenceClient
from models import SummarizeRequest, SummarizeResponse
from dotenv import load_dotenv
import os


# Load API Token from the .env file
load_dotenv()
API_TOKEN = os.getenv('huggingface-token')

client = InferenceClient(
    provider="novita",
    api_key=API_TOKEN,
)

def summarize_text(request: SummarizeRequest) -> SummarizeResponse:
    completion = client.chat.completions.create(
        model=request.model,
        messages=[
            {
                "role": "user",
                "content": "Summarize the following text: " + request.text
            }
        ],
    )

    return SummarizeResponse(http_response=completion.choices[0].finish_reason, text=completion.choices[0].message)