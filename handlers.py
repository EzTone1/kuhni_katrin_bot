import config, db, kb, text, utils
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils import greeting
from states import StepOfBot
from aiogram import F, Router
import asyncio
router = Router()
answers_of_client = {}



@router.message(Command("start"))
async def greetings_and_style_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.style_of_kitchen_state)
    await msg.answer(text.greetings_and_style_of_kitchen.format(greetings=greeting(), name=msg.from_user.full_name), reply_markup=kb.style_of_kitchen_keyboard, parse_mode="Markdown")


@router.message(StepOfBot.style_of_kitchen_state)
async def length_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.length_of_kitchen_state)
    utils.add_value_to_dict(answers_of_client, "style_of_kitchen", msg.text)
    if utils.pictures_of_style(msg.text):
        await msg.answer_photo(utils.pictures_of_style(msg.text))
    await msg.answer(utils.text_of_message(msg.text), parse_mode="Markdown")
    await msg.answer(text.length_of_kitchen, parse_mode="Markdown", reply_markup=kb.length_of_kitchen_keyboard)


@router.message(StepOfBot.length_of_kitchen_state)
async def form_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.form_of_kitchen_state)
    utils.add_value_to_dict(answers_of_client, "length_of_kitchen", msg.text)
    await msg.answer(text.form_of_kitchen, parse_mode="Markdown", reply_markup=kb.form_of_kitchen_keyboard)


@router.message(StepOfBot.form_of_kitchen_state)
async def tabletop_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.tabletop_of_kitchen_state)
    utils.add_value_to_dict(answers_of_client, "form_of_kitchen", msg.text)
    await msg.answer(text.tabletop_kitchen.format(form_of_kitchen=msg.text), parse_mode="Markdown", reply_markup=kb.type_of_tabletop_keyboard)


@router.message(StepOfBot.tabletop_of_kitchen_state, F.text == kb.plastic_tabletop)
@router.message(StepOfBot.tabletop_of_kitchen_state, F.text == kb.rock_tabletop)
async def price_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.price_of_kitchen_state)
    utils.add_value_to_dict(answers_of_client, "tabletop_material", msg.text)
    await msg.answer(utils.text_of_message(msg.text), parse_mode="Markdown", reply_markup=kb.delete_keyboard)
    await msg.answer(text.price_of_kitchen, parse_mode="Markdown")


@router.message(StepOfBot.price_of_kitchen_state)
async def city_of_kitchen(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.city_of_kitchen_state)
    utils.add_value_to_dict(answers_of_client, "budget_kitchen", msg.text)
    await msg.answer(text.city_of_kitchen, parse_mode="Markdown", reply_markup=kb.city_kitchen_keyboard)


@router.message(StepOfBot.city_of_kitchen_state)
async def phone_number_giving(msg: Message, state: FSMContext):
    await state.set_state(StepOfBot.number_not_given)
    utils.add_value_to_dict(answers_of_client, "city_of_kitchen", msg.text)
    await msg.answer(text.number_of_phone_kitchen.format(city_name=msg.text), parse_mode="Markdown", reply_markup=kb.phone_keyboard)
    await utils.send_messages_func(msg)


@router.message(StepOfBot.number_not_given)
async def number_of_phone_text(msg: Message, state: FSMContext):
    if msg.contact:
        await state.set_state(StepOfBot.number_given)
        utils.add_value_to_dict(answers_of_client, "number_of_phone_kitchen", msg.contact.phone_number)
        await msg.answer(allow_sending_without_reply=True, text=text.finish_kitchen.format(**answers_of_client), reply_markup=kb.delete_keyboard, parse_mode="Markdown")
        await msg.answer(text.saving_kitchen, parse_mode="Markdown")
        await asyncio.sleep(5)
        asyncio.create_task(succesful_saving(msg, state))
    elif utils.validate_phone_number(msg.text):
        await state.set_state(StepOfBot.number_given)
        utils.add_value_to_dict(answers_of_client, "number_of_phone_kitchen", msg.text)
        await msg.answer(allow_sending_without_reply=True, text=text.finish_kitchen.format(**answers_of_client), reply_markup=kb.delete_keyboard, parse_mode="Markdown")
        await msg.answer(text.saving_kitchen, parse_mode="Markdown")
        await asyncio.sleep(5)
        asyncio.create_task(succesful_saving(msg, state))
    else:
        await msg.answer(text=text.wrong_number)

async def succesful_saving(msg: Message, state: FSMContext):
    await msg.answer(allow_sending_without_reply=True, text=text.thanksgiving_kitchen, parse_mode="Markdown", reply_markup=kb.tg_channel_keyboard)
