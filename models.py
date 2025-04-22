from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    text: str
    model: str = "Nous Hermes 2 Mistral 7B DPO"

class SummarizeResponse(BaseModel):
    http_response: str
    text: str