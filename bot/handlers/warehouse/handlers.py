from aiogram import Router, types, F

from bot.utils.send_guide_with_animation import send_guide_with_animation

warehouse_router = Router()


@warehouse_router.callback_query(F.data == 'how_to_add_new_warehouse')
async def handle_add_warehouse(callback: types.CallbackQuery, lang: str) -> None:
    """Handles add warehouse guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_add_new_warehouse')


@warehouse_router.callback_query(F.data == 'how_to_view_warehouse')
async def handle_view_warehouse(callback: types.CallbackQuery, lang: str) -> None:
    """Handles view warehouse guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_view_warehouse')


@warehouse_router.callback_query(F.data == 'how_to_edit_warehouse')
async def handle_edit_warehouse(callback: types.CallbackQuery, lang: str) -> None:
    """Handles edit warehouse guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_edit_warehouse')


@warehouse_router.callback_query(F.data == 'how_to_delete_warehouse')
async def handle_delete_warehouse(callback: types.CallbackQuery, lang: str) -> None:
    """Handles delete warehouse guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_delete_warehouse')


@warehouse_router.callback_query(F.data == 'how_to_manage_products_in_warehouse')
async def handle_manage_products(callback: types.CallbackQuery, lang: str) -> None:
    """Handles product management guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_manage_products_in_warehouse')


@warehouse_router.callback_query(F.data == 'how_to_conduct_inventory')
async def handle_inventory(callback: types.CallbackQuery, lang: str) -> None:
    """Handles inventory guide request"""
    await send_guide_with_animation(callback, lang, 'how_to_conduct_inventory')
