import config
import asyncio
import logging

async def main():
    await config.bot.delete_webhook(drop_pending_updates=True)
    await config.dp.start_polling(config.bot, allowed_updates=config.dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())