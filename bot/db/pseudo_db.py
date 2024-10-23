from typing import Dict
from bot.config import DEFAULT_LANGUAGE
from .interfaces import UserStorageInterface


class PseudoUserStorage(UserStorageInterface):
    def __init__(self):
        self.users: Dict[int, str] = {}

    async def get_user_language(self, user_id: int) -> str:
        return self.users.get(user_id, DEFAULT_LANGUAGE)

    async def set_user_language(self, user_id: int, language: str):
        self.users[user_id] = language


user_storage = PseudoUserStorage()