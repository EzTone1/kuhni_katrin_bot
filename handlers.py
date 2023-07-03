import contextvars

import config
import kb
import text
import utils
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils import greeting
from states import StepOfBot
from aiogram import F, Router
import datetime
from contextvars import ContextVar
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import sheduled_message
import asyncio
import files
scheduler = ""
router = Router()
answers_of_client = {}
job1_context = ContextVar('job1_context')



@router.message(Command("start"))
async def greetings_and_style_of_kitchen(msg: Message, state: FSMContext, apscheduler: AsyncIOScheduler):
    await utils.remove_messages_from_redis(msg, apscheduler)
    await state.set_state(StepOfBot.style_of_kitchen_state)
    await msg.answer_photo(files.style_chosen)
    await msg.answer(text.greetings_and_style_of_kitchen.format(greetings=greeting(), name=msg.from_user.full_name), reply_markup=kb.style_of_kitchen_keyboard, parse_mode="Markdown")


@router.message(StepOfBot.style_of_kitchen_state)
async def length_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.length_of_kitchen_state)
    await state.update_data(style_of_kitchen=msg.text)
    #utils.add_value_to_dict(answers_of_client, "style_of_kitchen", msg.text)
    if utils.pictures_of_style(msg.text):
        await msg.answer_photo(utils.pictures_of_style(msg.text))
    await msg.answer(utils.text_of_message(msg.text), parse_mode="Markdown")
    await msg.answer(text.length_of_kitchen, parse_mode="Markdown", reply_markup=kb.length_of_kitchen_keyboard)


@router.message(StepOfBot.length_of_kitchen_state)
async def form_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.form_of_kitchen_state)
    #utils.add_value_to_dict(answers_of_client, "length_of_kitchen", msg.text)
    await state.update_data(length_of_kitchen=msg.text)
    await msg.answer_photo(files.form_chosen)
    await msg.answer(text.form_of_kitchen, parse_mode="Markdown", reply_markup=kb.form_of_kitchen_keyboard)


@router.message(StepOfBot.form_of_kitchen_state)
async def tabletop_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.tabletop_of_kitchen_state)
    #utils.add_value_to_dict(answers_of_client, "form_of_kitchen", msg.text)
    await state.update_data(form_of_kitchen=msg.text)
    await msg.answer_photo(files.tabletop_chosen)
    await msg.answer(text.tabletop_kitchen.format(form_of_kitchen=msg.text), parse_mode="Markdown", reply_markup=kb.type_of_tabletop_keyboard)


@router.message(StepOfBot.tabletop_of_kitchen_state, F.text == kb.plastic_tabletop)
@router.message(StepOfBot.tabletop_of_kitchen_state, F.text == kb.rock_tabletop)
async def price_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.price_of_kitchen_state)
    #utils.add_value_to_dict(answers_of_client, "tabletop_material", msg.text)
    await state.update_data(tabletop_material=msg.text)
    await msg.answer(utils.text_of_message(msg.text), parse_mode="Markdown", reply_markup=kb.delete_keyboard)
    await msg.answer(text.price_of_kitchen, parse_mode="Markdown")


@router.message(StepOfBot.price_of_kitchen_state)
async def city_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.city_of_kitchen_state)
    #utils.add_value_to_dict(answers_of_client, "budget_kitchen", msg.text)
    await state.update_data(budget_kitchen=msg.text)
    await msg.answer(text.city_of_kitchen, parse_mode="Markdown", reply_markup=kb.city_kitchen_keyboard)


@router.message(StepOfBot.city_of_kitchen_state)
async def phone_number_giving(msg: Message, state: FSMContext, apscheduler: AsyncIOScheduler):
    await state.set_state(StepOfBot.number_not_given)
    #utils.add_value_to_dict(answers_of_client, "city_of_kitchen", msg.text)
    await state.update_data(city_of_kitchen=msg.text)
    await msg.answer(text.number_of_phone_kitchen.format(city_name=msg.text), parse_mode="Markdown", reply_markup=kb.phone_keyboard)
    apscheduler.add_job(sheduled_message.send_1_fire_message, trigger='date',
                        run_date=datetime.datetime.now() + datetime.timedelta(minutes=5),
                        kwargs={'chat_id': msg.from_user.id}, id=str(msg.from_user.id) + '1')
    apscheduler.add_job(sheduled_message.send_2_fire_message, trigger='date',
                        run_date=datetime.datetime.now() + datetime.timedelta(days=1),
                        kwargs={'chat_id': msg.from_user.id}, id=str(msg.from_user.id) + '2')
    apscheduler.add_job(sheduled_message.send_3_fire_message, trigger='date',
                        run_date=datetime.datetime.now() + datetime.timedelta(days=3),
                        kwargs={'chat_id': msg.from_user.id}, id=str(msg.from_user.id) + '3')
    apscheduler.add_job(sheduled_message.send_4_fire_message, trigger='date',
                        run_date=datetime.datetime.now() + datetime.timedelta(days=7),
                        kwargs={'chat_id': msg.from_user.id}, id=str(msg.from_user.id) + '4')
    apscheduler.add_job(sheduled_message.send_5_fire_message, trigger='date',
                        run_date=datetime.datetime.now() + datetime.timedelta(days=14),
                        kwargs={'chat_id': msg.from_user.id}, id=str(msg.from_user.id) + '5')
    apscheduler.add_job(sheduled_message.send_6_fire_message, trigger='date',
                        run_date=datetime.datetime.now() + datetime.timedelta(days=21),
                        kwargs={'chat_id': msg.from_user.id}, id=str(msg.from_user.id) + '6')


@router.message(StepOfBot.number_not_given, F.text==text.firing_button_phone)
@router.message(StepOfBot.number_not_given, F.text==text.firing_button_whatsapp)
@router.message(StepOfBot.number_not_given, F.text==text.firing_button_on_phone)
@router.message(StepOfBot.number_not_given, F.text==text.firing_button_on_whatsapp)
@router.message(StepOfBot.number_not_given, F.text==text.firing_button_consult)
@router.message(StepOfBot.number_not_given, F.text==text.firing_button_meeting)
async def city_of_kitchen(msg: Message, state: FSMContext):
    await msg.answer(text.giving_number_on_firing.format(city_name=msg.text), parse_mode="Markdown",
                     reply_markup=kb.phone_keyboard)


@router.message(StepOfBot.number_not_given)
async def number_of_phone_text(msg: Message, state: FSMContext, apscheduler: AsyncIOScheduler):
    if msg.contact:
        await utils.remove_messages_from_redis(msg, apscheduler)
        await state.set_state(StepOfBot.number_given)
        await state.update_data(number_of_phone_kitchen=msg.contact.phone_number)
        context_data = await state.get_data()
        utils.add_value_to_dict(answers_of_client, 'style_of_kitchen', context_data.get('style_of_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'length_of_kitchen', context_data.get('length_of_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'form_of_kitchen', context_data.get('form_of_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'tabletop_material', context_data.get('tabletop_material'))
        utils.add_value_to_dict(answers_of_client, 'budget_kitchen', context_data.get('budget_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'city_of_kitchen', context_data.get('city_of_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'number_of_phone_kitchen', context_data.get('number_of_phone_kitchen'))
        await msg.answer(allow_sending_without_reply=True, text=text.finish_kitchen.format(**answers_of_client),
                         reply_markup=kb.delete_keyboard, parse_mode="Markdown")
        await msg.answer(text.saving_kitchen, parse_mode="Markdown")
        await asyncio.sleep(5)
        await msg.answer(allow_sending_without_reply=True, text=text.thanksgiving_kitchen, parse_mode="Markdown",
                         reply_markup=kb.tg_channel_keyboard)
        await config.bot.send_message(config.group_id, text=text.finish_kitchen_in_group.format(**answers_of_client), parse_mode="Markdown")
        await state.clear()
    elif utils.validate_phone_number(msg.text):
        await utils.remove_messages_from_redis(msg, apscheduler)
        await state.set_state(StepOfBot.number_given)
        await state.update_data(number_of_phone_kitchen=msg.text)
        context_data = await state.get_data()
        utils.add_value_to_dict(answers_of_client, 'style_of_kitchen', context_data.get('style_of_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'length_of_kitchen', context_data.get('length_of_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'form_of_kitchen', context_data.get('form_of_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'tabletop_material', context_data.get('tabletop_material'))
        utils.add_value_to_dict(answers_of_client, 'budget_kitchen', context_data.get('budget_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'city_of_kitchen', context_data.get('city_of_kitchen'))
        utils.add_value_to_dict(answers_of_client, 'number_of_phone_kitchen', context_data.get('number_of_phone_kitchen'))

        await msg.answer(allow_sending_without_reply=True, text=text.finish_kitchen.format(**answers_of_client),
                         reply_markup=kb.delete_keyboard, parse_mode="Markdown")
        await msg.answer(text.saving_kitchen, parse_mode="Markdown")
        await asyncio.sleep(5)
        await msg.answer(allow_sending_without_reply=True, text=text.thanksgiving_kitchen, parse_mode="Markdown",
                         reply_markup=kb.tg_channel_keyboard)
        await config.bot.send_message(config.group_id, text=text.finish_kitchen_in_group.format(**answers_of_client), parse_mode="Markdown")
        await state.clear()

    else:
        await msg.answer(text=text.wrong_number)

