from aiogram import Router, types, F

from bot.utils.send_guide_with_animation import send_guide_with_animation

product_router = Router()


@product_router.callback_query(F.data == 'how_to_add_new_product')
async def handle_add_product(callback: types.CallbackQuery, lang: str) -> None:
    """Handles add product guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_add_new_product')


@product_router.callback_query(F.data == 'how_to_view_the_product')
async def handle_view_product(callback: types.CallbackQuery, lang: str) -> None:
    """Handles view product guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_view_the_product')


@product_router.callback_query(F.data == 'how_to_edit_product')
async def handle_edit_product(callback: types.CallbackQuery, lang: str) -> None:
    """Handles edit product guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_edit_product')


@product_router.callback_query(F.data == 'how_to_delete_product')
async def handle_delete_product(callback: types.CallbackQuery, lang: str) -> None:
    """Handles delete product guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_delete_product')


@product_router.callback_query(F.data == 'how_to_view_the_remaining_stock')
async def handle_view_stock(callback: types.CallbackQuery, lang: str) -> None:
    """Handles view stock guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_view_the_remaining_stock')


@product_router.callback_query(F.data == 'how_to_set_minimum_balances_for_automatic_ordering')
async def handle_set_min_stock(callback: types.CallbackQuery, lang: str) -> None:
    """Handles minimum stock setup guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_set_minimum_balances_for_automatic_ordering')
