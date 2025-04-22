from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    text: str
    model: str = "Nous Hermes 2 Mistral 7B DPO"
    limit: int = 500
    temperature: float = 0.7

class SummarizeResponse(BaseModel):
    http_response: str
    text: str