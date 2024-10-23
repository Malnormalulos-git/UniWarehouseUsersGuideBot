from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from bot.resources.locales.locales import texts


def get_main_kb(lang: str):
    """Returns main keyboard"""
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=texts[lang]['button_products']), KeyboardButton(text=texts[lang]['button_warehouses'])],
        [KeyboardButton(text=texts[lang]['button_reports']), KeyboardButton(text=texts[lang]['button_help'])],
        [KeyboardButton(text='🌐 Change language')]
    ], resize_keyboard=True, input_field_placeholder=texts[lang]['main_menu_placeholder'])


"""Language buttons"""
language_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=texts[lang]['language'], callback_data=f'lang_{lang}') for lang in texts]
])


def get_product_buttons(lang: str):
    """Returns product buttons"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=texts[lang]['button_how_to_add_new_product'], callback_data='how_to_add_new_product')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_view_the_product'], callback_data='how_to_view_the_product')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_edit_product'], callback_data='how_to_edit_product')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_delete_product'], callback_data='how_to_delete_product')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_view_the_remaining_stock'], callback_data='how_to_view_the_remaining_stock')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_set_minimum_balances_for_automatic_ordering'], callback_data='how_to_set_minimum_balances_for_automatic_ordering')]
    ])


def get_warehouse_buttons(lang: str):
    """Returns warehouse buttons"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=texts[lang]['button_how_to_add_new_warehouse'], callback_data='how_to_add_new_warehouse')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_view_warehouse'], callback_data='how_to_view_warehouse')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_edit_warehouse'], callback_data='how_to_edit_warehouse')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_delete_warehouse'], callback_data='how_to_delete_warehouse')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_manage_products_in_warehouse'], callback_data='how_to_manage_products_in_warehouse')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_conduct_inventory'], callback_data='how_to_conduct_inventory')]
    ])


def get_report_buttons(lang: str):
    """Returns report buttons"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=texts[lang]['button_how_to_generate_current_stock'], callback_data='how_to_generate_current_stock')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_generate_movement'], callback_data='how_to_generate_movement')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_generate_low_stock'], callback_data='how_to_generate_low_stock')],
        [InlineKeyboardButton(text=texts[lang]['button_how_to_generate_analytics'], callback_data='how_to_generate_analytics')]
    ])