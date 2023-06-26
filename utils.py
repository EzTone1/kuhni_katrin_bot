import datetime
import text
import kb, files, re, asyncio, config, db, time

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


async def send_messages_func(msg):
    task1 = asyncio.create_task(waiting_message(msg=msg, text="text.phone_number_fire_1", timeout=5,
                                                reply_markup="fire_button_1",
                                                number_of_message=1))
    tasks.append(task1)
    task2 = asyncio.create_task(waiting_message(msg=msg, text="text.phone_number_fire_2", timeout=10,
                                                reply_markup="fire_button_1",
                                                number_of_message=2))
    tasks.append(task2)
    task3 = asyncio.create_task(waiting_message(msg=msg, text="text.phone_number_fire_3", timeout=15,
                                                reply_markup="calendar",
                                                number_of_message=3))
    tasks.append(task3)
    task4 = asyncio.create_task(waiting_message(msg=msg, text="text.phone_number_fire_4", timeout=20,
                                                reply_markup="fire_button_1",
                                                number_of_message=4))
    tasks.append(task4)
    task5 = asyncio.create_task(waiting_message(msg=msg, text="text.phone_number_fire_5", timeout=25,
                                                reply_markup="fire_button_2",
                                                number_of_message=5))
    tasks.append(task5)
    task6 = asyncio.create_task(waiting_message(msg=msg, text="text.phone_number_fire_6", timeout=30,
                                                reply_markup="fire_button_2",
                                                number_of_message=6, image="data/firing/checklist.png"))
    tasks.append(task6)

    try:
        await asyncio.wait_for(asyncio.gather(*tasks), timeout=None)  # Ждем завершения всех задач
    except asyncio.TimeoutError:
        await cancel_tasks(tasks)
        print("Остановлено выполнение задач из-за таймаута")



async def waiting_message(text, timeout, reply_markup, number_of_message, chat_id=None, msg=None, image=None):
    try:
        if chat_id:
            user_id = chat_id
        else:
            user_id = msg.from_user.id
        start_time = time.time()
        message = text
        db.save_timer_message(user_id, start_time, message, timeout, number_of_message, reply_markup, image)
        await asyncio.sleep(timeout)
        db.delete_timer_message(user_id, number_of_message)
        await config.bot.send_message(chat_id=user_id, text=text)

    except Exception as e:
        print(e)

async def cancel_tasks(tasks):
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)