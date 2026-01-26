from pydantic import BaseModel


class AnalyzePayload(BaseModel):
    mime_type: str
    data: str
    explanation_style: str
    llm_key: str
