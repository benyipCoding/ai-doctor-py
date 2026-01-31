# app/schemas/llms.py
from pydantic import BaseModel


class LLMSerializer(BaseModel):
    key: str
    name: str
    tag: str
    desc: str
    model_config = {"from_attributes": True}  # ⭐ Pydantic v2 关键
