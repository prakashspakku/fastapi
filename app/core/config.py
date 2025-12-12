import os
from typing import Optional

class Settings:
    def __init__(self):
        self.app_name: str = os.getenv("APP_NAME", "fastapi-ci-expert")
        self.env: str = os.getenv("APP_ENV", "dev")
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        self.enable_metrics: bool = os.getenv("ENABLE_METRICS", "true").lower() == "true"
        self.version_override: Optional[str] = os.getenv("APP_VERSION", None)

settings = Settings()
