from aiogram.types import Message, CallbackQuery
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import files
import kb
import text


async def send_1_fire_message(chat_id: int, bot: Bot):
    await bot.send_photo(chat_id=chat_id, photo=files.step1)
    await bot.send_message(chat_id, text.fire_message_1, parse_mode="Markdown", reply_markup=kb.firing_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))

async def send_2_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_2, parse_mode="Markdown", reply_markup=kb.firing_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))

async def send_3_fire_message(chat_id: int, bot: Bot):
    await bot.send_photo(chat_id=chat_id, photo=files.step3)
    await bot.send_message(chat_id, text.fire_message_3, parse_mode="Markdown", reply_markup=kb.firing_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))

async def send_4_fire_message(chat_id: int, bot: Bot):
    await bot.send_media_group(chat_id=chat_id, media=files.media_group)
    # await bot.send_photo(chat_id=chat_id, photo=files.step4_1)
    # await bot.send_photo(chat_id=chat_id, photo=files.step4_2)
    # await bot.send_photo(chat_id=chat_id, photo=files.step4_3)
    # await bot.send_photo(chat_id=chat_id, photo=files.step4_4)
    # await bot.send_photo(chat_id=chat_id, photo=files.step4_5)
    # await bot.send_photo(chat_id=chat_id, photo=files.step4_6)
    # await bot.send_photo(chat_id=chat_id, photo=files.step4_7)
    # await bot.send_photo(chat_id=chat_id, photo=files.step4_8)
    await bot.send_message(chat_id, text.fire_message_4, parse_mode="Markdown", reply_markup=kb.firing2_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))

async def send_5_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_5, parse_mode="Markdown", reply_markup=kb.firing3_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))
    await bot.send_message(chat_id, text.fire_message_5_link)
async def send_6_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_6, parse_mode="Markdown", reply_markup=kb.firing3_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))
