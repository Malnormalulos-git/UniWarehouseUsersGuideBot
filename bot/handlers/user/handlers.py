from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.markdown import hbold

from bot.handlers.user.keyboards import get_main_kb, language_buttons, get_product_buttons, get_warehouse_buttons, get_report_buttons
from bot.resources.locales.locales import texts

from bot.db.pseudo_db import user_storage

user_router = Router()


@user_router.message(Command('start'))
async def cmd_start(msg: types.Message, lang: str) -> None:
    """Processes the `start` command"""
    await msg.answer(texts[lang]['welcome'].format(hbold(msg.from_user.first_name)), reply_markup=language_buttons)


@user_router.callback_query(F.data.startswith("lang_"))
async def change_language(callback: types.CallbackQuery) -> None:
    """Sets new language"""
    new_lang = callback.data.split("_")[1]
    await user_storage.set_user_language(callback.from_user.id, new_lang)
    await callback.message.answer(texts[new_lang]['language_changed'], reply_markup=get_main_kb(new_lang))
    await callback.answer()


@user_router.message(F.text.in_({texts[lang]['button_products'] for lang in texts}))
async def products_info(msg: types.Message, lang: str) -> None:
    """Provides information about the products section"""
    await msg.answer(texts[lang]['products'], reply_markup=get_product_buttons(lang))


@user_router.message(F.text.in_({texts[lang]['button_warehouses'] for lang in texts}))
async def warehouses_info(msg: types.Message, lang: str) -> None:
    """Provides information about the warehouse section"""
    await msg.answer(texts[lang]['warehouses'], reply_markup=get_warehouse_buttons(lang))


@user_router.message(F.text.in_({texts[lang]['button_reports'] for lang in texts}))
async def reports_info(msg: types.Message, lang: str) -> None:
    """Provides information about the reports section"""
    await msg.answer(texts[lang]['reports'], reply_markup=get_report_buttons(lang))


@user_router.message(F.text.in_({texts[lang]['button_reports'] for lang in texts}))
async def reports_info(msg: types.Message, lang: str) -> None:
    """Provides information about the reports section"""
    await msg.answer(texts[lang]['reports'])


@user_router.message(F.text.in_({texts[lang]['button_help'] for lang in texts}))
async def help_info(msg: types.Message, lang: str) -> None:
    """Provides general information about the bot"""
    await msg.answer(texts[lang]['help'])


@user_router.message(F.text == '🌐 Change language')
async def change_language_option(msg: types.Message, lang: str) -> None:
    """Provides available bot languages and gives opportunity to set new language"""
    await msg.answer(texts[lang]['language_changed'], reply_markup=language_buttons)


@user_router.message()
async def handle_other_messages(msg: types.Message, lang: str) -> None:
    """Processes other messages"""
    await msg.answer(texts[lang]['unknown'])
