from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os

load_dotenv()

token_api = os.getenv("TOKEN_API")

if token_api is None:
    raise ValueError("TOKEN_API environment variable is not set")

bot = Bot(
    token=token_api,
    default=DefaultBotProperties(parse_mode='HTML')
)