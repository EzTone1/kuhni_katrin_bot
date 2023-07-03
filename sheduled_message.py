from aiogram.types import Message, CallbackQuery


async def send_first_fire_message(msg: Message):
    await msg.answer("First Message")


async def send_second_fire_message(msg: Message):
    await msg.answer("Second Message")


async def send_third_fire_message(msg: Message):
    await msg.answer("Third Message")


async def send_fourth_fire_message(msg: Message):
    await msg.answer("Fourth Message")


async def send_five_fire_message(msg: Message):
    await msg.answer("Five Message")


async def send_sixth_fire_message(msg: Message):
    await msg.answer("Six Message")