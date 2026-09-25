# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    ETH_RPC_URL: str = os.getenv("ETH_RPC_URL", "https://eth.llamarpc.com")


settings = Settings()

if not settings.BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in .env")