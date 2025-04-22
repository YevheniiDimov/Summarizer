from typing import Union
from fastapi import FastAPI
from models import SummarizeRequest, SummarizeResponse
from summarizer import summarize_text
from logs import log_request


# Initialize FastAPI server
app = FastAPI()

# Routes
@app.get("/")
def read_root():
    log_request(request_data={"text": "/"}, response_data={"summary": "Description"})
    return {
        "Message": "Hello, this is a microservice that allows you to summarize a text!",
        "Routes": "GET / - This message\nPOST {\"text\": \"*\", \"model\": \"*\" (optional), \"limit\": * (500 is default, optional), \"temperature\": * (0.7 is default, optional)} to /summarize - summarizes a text for you"
    }
    

@app.post("/summarize")
async def summarize(request: SummarizeRequest) -> SummarizeResponse:
    response = summarize_text(request)
    log_request(request_data={"text": request.model_dump()}, response_data=response.model_dump())

    return summarize_text(request)