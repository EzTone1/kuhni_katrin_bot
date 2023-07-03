import datetime
import text
import kb, files, re, asyncio, config, db, time
from aiogram.types import Message, CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import sheduled_message

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

async def create_fire_messages_scheduler(msg: Message):
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(sheduled_message.send_first_fire_message, trigger='date', run_date=datetime.datetime.now() + datetime.timedelta(seconds=10), kwargs={"msg": msg})
    scheduler.start()
    return scheduler