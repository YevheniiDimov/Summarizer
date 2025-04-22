from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    text: str
    model: str = "deepseek-ai/DeepSeek-V3-0324"

class SummarizeResponse(BaseModel):
    http_response: str
    text: str