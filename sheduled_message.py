from aiogram.types import Message, CallbackQuery
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import kb
import text


async def send_1_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_1, parse_mode="Markdown", reply_markup=kb.firing_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))

async def send_2_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_2, parse_mode="Markdown", reply_markup=kb.firing_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))

async def send_3_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_3, parse_mode="Markdown", reply_markup=kb.firing_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))

async def send_4_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_4, parse_mode="Markdown", reply_markup=kb.firing2_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))

async def send_5_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_5, parse_mode="Markdown", reply_markup=kb.firing3_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))
    await bot.send_message(chat_id, text.fire_message_5_link)
async def send_6_fire_message(chat_id: int, bot: Bot):
    await bot.send_message(chat_id, text.fire_message_6, parse_mode="Markdown", reply_markup=kb.firing3_reply.as_markup(resize_keyboard=True, one_time_keyboard=True))
