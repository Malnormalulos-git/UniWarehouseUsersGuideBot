import asyncio

from aiogram import Dispatcher

from bot.bot import bot
from bot.handlers.product.handlers import product_router
from bot.handlers.user.handlers import user_router
from bot.handlers.warehouse.handlers import warehouse_router
from bot.handlers.report.handlers import report_router
from bot.middlewares.language_middleware import LanguageMiddleware


def register_routers(dp: Dispatcher) -> None:
    """Registers routers"""
    dp.include_router(user_router)
    dp.include_router(product_router)
    dp.include_router(warehouse_router)
    dp.include_router(report_router)


async def main() -> None:
    """Entry Point - event loop and start polling."""
    dp = Dispatcher()
    dp.message.middleware(LanguageMiddleware())
    dp.callback_query.middleware(LanguageMiddleware())

    register_routers(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
