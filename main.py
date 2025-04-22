from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from models import SummarizeRequest, SummarizeResponse
from summarizer import summarize_text


# Initialize FastAPI server
app = FastAPI()

# Routes
@app.get("/")
def read_root():
    return {
        "Message": "Hello, this is a microservice that allows you to summarize a text!",
        "Routes": "GET / - This message\nPOST {\"text\": \"*\", \"model\": \"*\" (deepseek-ai/DeepSeek-V3-0324 is default)} to /summarize - summarizes a text for you"
    }

@app.post("/summarize")
async def summarize(request: SummarizeRequest) -> SummarizeResponse:
    return summarize_text(request)

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}