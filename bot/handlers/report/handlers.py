from aiogram import Router, types, F

from bot.utils.send_guide_with_animation import send_guide_with_animation

report_router = Router()


@report_router.callback_query(F.data == 'how_to_generate_current_stock')
async def handle_current_stock_report(callback: types.CallbackQuery, lang: str) -> None:
    """Handles current stock report guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_generate_current_stock')


@report_router.callback_query(F.data == 'how_to_generate_movement')
async def handle_movement_report(callback: types.CallbackQuery, lang: str) -> None:
    """Handles movement report guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_generate_movement')


@report_router.callback_query(F.data == 'how_to_generate_low_stock')
async def handle_low_stock_report(callback: types.CallbackQuery, lang: str) -> None:
    """Handles low stock report guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_generate_low_stock')


@report_router.callback_query(F.data == 'how_to_generate_analytics')
async def handle_analytics_report(callback: types.CallbackQuery, lang: str) -> None:
    """Handles analytics report guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_generate_analytics')
