from abc import ABC, abstractmethod


class UserStorageInterface(ABC):
    """
    Interface for user storage implementations.
    Defines the contract for storing and retrieving user language preferences.
    """

    @abstractmethod
    async def get_user_language(self, user_id: int) -> str:
        """
        Get the language preference for a specific user.

        Args:
            user_id: The unique identifier of the user

        Returns:
            str: The language code for the user's preferred language
        """
        pass

    @abstractmethod
    async def set_user_language(self, user_id: int, language: str) -> None:
        """
        Set the language preference for a specific user.

        Args:
            user_id: The unique identifier of the user
            language: The language code to set as the user's preference
        """
        pass