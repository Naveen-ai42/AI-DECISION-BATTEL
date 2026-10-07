import os
from typing import List
from dotenv import load_dotenv

# Load environment variables if .env exists
load_dotenv()


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Decision Arena")
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:5173")
    AI_PROVIDER: str = os.getenv("AI_PROVIDER", "mock")

    @property
    def CORS_ORIGINS(self) -> List[str]:
        origins = [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:5174",
            "http://127.0.0.1:5174",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ]

        if self.FRONTEND_URL and self.FRONTEND_URL not in origins:
            origins.append(self.FRONTEND_URL)

        return origins


settings = Settings()