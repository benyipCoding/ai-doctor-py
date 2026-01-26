import base64
from app.clients.gemini import get_gemini_client
from app.schemas.analyze import AnalyzePayload
from app.prompt.analyze_image import generate_prompt
from google.genai import types
import json


class AnalyzeService:
    def base64_to_bytes(b64: str) -> bytes:
        # 如果有 data:image/...;base64, 前缀，先去掉
        if "," in b64:
            b64 = b64.split(",", 1)[1]
        return base64.b64decode(b64)

    def analyze(self, payload: AnalyzePayload):
        image_bytes = self.base64_to_bytes(payload.data)
        client = get_gemini_client()
        # 构造提示词
        prompt_text = generate_prompt(payload.explanation_style)
        # 调用 Gemini API 进行图像分析
        response = client.models.generate_content(
            model=payload.llm_key,
            contents=[
                # 文本 prompt
                types.Part.from_text(text=prompt_text),
                # 以 bytes 形式传入图像
                types.Part.from_bytes(data=image_bytes, mime_type=payload.mime_type),
            ],
            # config=types.GenerateContentConfig(response_mime_type="application/json"),
        )
        result = json.loads(response.text)
        return result
