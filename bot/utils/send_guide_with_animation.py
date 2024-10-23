from aiogram import types

from bot.config import GIFS_DIRECTORY
from bot.utils.find_file_by_name import find_file_by_name
from bot.resources.locales.locales import texts


async def send_guide_with_animation(callback: types.CallbackQuery, lang: str, action: str) -> None:
    """Sends an instruction to the user as a GIF animation with a caption if gif_file exists, just text if it doesn't"""
    gif_file = find_file_by_name(GIFS_DIRECTORY, f"{action}.mp4")
    if gif_file is not None:
        await callback.message.answer_animation(animation=gif_file, caption=texts[lang][action])
    else:
        await callback.message.answer(texts[lang][action])
    await callback.answer()
