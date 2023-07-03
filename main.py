import config
import asyncio
import logging
from handlers import router
from aiogram import Bot, Dispatcher
from middlewares.timer_message_middleware import SchedulerMiddleware
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler_di import ContextSchedulerDecorator
from apscheduler.jobstores.redis import RedisJobStore

async def main():
    storage = RedisStorage.from_url("redis://localhost:6379/0")


    dp = Dispatcher(storage=storage)

    dp.include_router(router)
    jobstores = {
        'default': RedisJobStore(jobs_key='dispatched_trips_jobs',
                                 run_times_key='dispatched_trips_running',
                                 host='localhost',
                                 db=2,
                                 port=6379)
    }
    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone="Europe/Moscow", jobstores=jobstores))
    scheduler.ctx.add_instance(config.bot, declared_class=Bot)
    scheduler.start()
    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    await config.bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(config.bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())