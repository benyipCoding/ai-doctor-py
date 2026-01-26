import base64


class AnalyzeService:
    def base64_to_bytes(b64: str) -> bytes:
        # 如果有 data:image/...;base64, 前缀，先去掉
        if "," in b64:
            b64 = b64.split(",", 1)[1]
        return base64.b64decode(b64)

    async def analyze(self, payload):
        image_bytes = self.base64_to_bytes(payload.data)
        print("image bytes:", len(image_bytes))
        return "analysis started"
