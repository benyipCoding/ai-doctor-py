import base64
from app.clients.gemini import get_gemini_client
from app.schemas.analyze import AnalyzePayload
from app.prompt.analyze_image import generate_prompt
from google.genai import types
import json
from sqlalchemy.ext.asyncio import AsyncSession


class AnalyzeService:
    def base64_to_bytes(self, b64: str) -> bytes:
        # 如果有 data:image/...;base64, 前缀，先去掉
        if "," in b64:
            b64 = b64.split(",", 1)[1]
        return base64.b64decode(b64)

    async def analyze(self, payload: AnalyzePayload, db: AsyncSession):
        image_bytes = self.base64_to_bytes(payload.data)
        client = get_gemini_client()
        # 构造提示词
        prompt_text = generate_prompt(payload.explanationStyle)
        # 调用 Gemini API 进行图像分析
        response = client.models.generate_content(
            model=payload.llmKey,
            contents=[
                # 文本 prompt
                types.Part.from_text(text=prompt_text),
                # 以 bytes 形式传入图像
                types.Part.from_bytes(data=image_bytes, mime_type=payload.mimeType),
            ],
            config=types.GenerateContentConfig(response_mime_type="application/json"),
        )
        # TODO: 解析 response，提取所需信息，记录使用的 token 数量
        total_token_count = json.loads(response.json())["usage_metadata"][
            "total_token_count"
        ]
        # temp['usage_metadata']['total_token_count']
        print(f"Total token count: {total_token_count}")
        # 将分析结果返回给调用方
        result = json.loads(response.text)
        result["total_token_count"] = total_token_count
        return result
