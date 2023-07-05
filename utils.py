import datetime
import text
import kb
import files
import re
import asyncio
from aiogram.types import Message, CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import sheduled_message
from contextvars import ContextVar
from aiogram import Bot
tasks = []
def greeting():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        return "Доброе утро"
    elif 12 <= current_time.hour < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"

def text_of_message(text_of_message):
    match text_of_message:
        case kb.classic_style:
            return text.classic_kitchen
        case kb.hitech_style:
            return text.hitech_kitchen
        case kb.loft_style:
            return text.loft_kitchen
        case kb.minimalistic_style:
            return text.minimalistic_kitchen
        case kb.scandinavian_style:
            return text.scandinavian_kitchen
        case kb.neoclassic_style:
            return text.neoclassic_kitchen
        case kb.plastic_tabletop:
            return text.plastic_tabletop
        case kb.rock_tabletop:
            return text.rock_tabletop
        case _:
            return text.other_kichen.format(user_style=text_of_message)

def pictures_of_style(text_of_message):
    match text_of_message:
        case kb.classic_style:
            return files.clasic_kitchen
        case kb.hitech_style:
            return files.hitech_kitchen
        case kb.loft_style:
            return files.loft_kitchen
        case kb.minimalistic_style:
            return files.minimalistic_kitchen
        case kb.scandinavian_style:
            return files.scandinavian_kitchen
        case kb.neoclassic_style:
            return files.neoclassic_kitchen
        case kb.rock_tabletop:
            return text.rock_tabletop
        case kb.plastic_tabletop:
            return text.plastic_tabletop
        case _:
            return None


def add_value_to_dict(answers_of_client, key, value):
    answers_of_client[key] = value


def validate_phone_number(phone_number):
    # Удаляем все символы, кроме цифр
    phone_number = re.sub(r'\D', '', phone_number)
    # Проверяем, что номер состоит из 11 цифр и начинается с 7, 8 или 9
    if re.match(r'^[7-9]\d{10}$', phone_number):
        return True
    else:
        return False

async def remove_messages_from_redis(msg: Message, apscheduler: AsyncIOScheduler):
    if apscheduler.get_job(str(msg.from_user.id) + '1'):
        apscheduler.remove_job(str(msg.from_user.id) + '1')
    if apscheduler.get_job(str(msg.from_user.id) + '2'):
        apscheduler.remove_job(str(msg.from_user.id) + '2')
    if apscheduler.get_job(str(msg.from_user.id) + '3'):
        apscheduler.remove_job(str(msg.from_user.id) + '3')
    if apscheduler.get_job(str(msg.from_user.id) + '4'):
        apscheduler.remove_job(str(msg.from_user.id) + '4')
    if apscheduler.get_job(str(msg.from_user.id) + '5'):
        apscheduler.remove_job(str(msg.from_user.id) + '5')
    if apscheduler.get_job(str(msg.from_user.id) + '6'):
        apscheduler.remove_job(str(msg.from_user.id) + '6')