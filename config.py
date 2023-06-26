from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from handlers import router

BOT_TOKEN = '6280887333:AAHDT2tALWOn03ERKgN6tQweF1upblViL98'
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)
tasks = []