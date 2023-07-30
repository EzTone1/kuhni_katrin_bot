from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

import text

classic_style = "📎 Классика"
hitech_style = "📎 Хай-тек"
loft_style = "📎 Лофт"
minimalistic_style = "📎 Минимализм"
scandinavian_style = "📎 Скандинавский стиль"
neoclassic_style = "📎 Нео-классика"
style_of_kitchen = [
    [KeyboardButton(text=classic_style),
    KeyboardButton(text=hitech_style)],
    [KeyboardButton(text=loft_style),
    KeyboardButton(text=minimalistic_style)],
    [KeyboardButton(text=scandinavian_style),
    KeyboardButton(text=neoclassic_style)]
]
style_of_kitchen_keyboard = ReplyKeyboardMarkup(
    keyboard=style_of_kitchen,
    resize_keyboard=True,
    input_field_placeholder="Выберите подходящий стиль, или напишите его сюда",
    one_time_keyboard=True
)


length_three_meters = "3️⃣ метра (от 90 000 руб.)"
length_four_meters = "4️⃣ метра (от 120 000 руб.)"
length_five_meters = "5️⃣ метров (от 150 000 руб.)"
length_six_meters = "6️⃣ метров (от 180 000 руб.)"
length_seven_plus_meters = "7️⃣+ метров (от 210 000 руб.)"
dont_know_meters = "➡ Точно не могу сказать"
length_of_kitchen = [
    [KeyboardButton(text=length_three_meters)],
    [KeyboardButton(text=length_four_meters),
    KeyboardButton(text=length_five_meters)],
    [KeyboardButton(text=length_six_meters),
    KeyboardButton(text=length_seven_plus_meters)],
    [KeyboardButton(text=dont_know_meters)]
]
length_of_kitchen_keyboard = ReplyKeyboardMarkup(
    keyboard=length_of_kitchen, resize_keyboard=True,
    input_field_placeholder="Выберите длину Вашей кухни или напишите сюда",
    one_time_keyboard=True
)


straight_form = "⭕ Прямая"
angular_form = "⭕ Угловая"
u_shaped_form = "⭕ П-образная"
with_the_island = "⭕ С островом"
form_of_kitchen = [
    [KeyboardButton(text=straight_form),
    KeyboardButton(text=angular_form)],
    [KeyboardButton(text=u_shaped_form),
    KeyboardButton(text=with_the_island)]
]
form_of_kitchen_keyboard = ReplyKeyboardMarkup(
    keyboard=form_of_kitchen,
    resize_keyboard=True,
    input_field_placeholder="Выберите форму из списка",
    one_time_keyboard=True
)

plastic_tabletop = "🟠 Пластиковая"
rock_tabletop = "🟠 Каменная"
type_of_tabletop = [
    [KeyboardButton(text=plastic_tabletop)],
    [KeyboardButton(text=rock_tabletop)]
]
type_of_tabletop_keyboard = ReplyKeyboardMarkup(
    keyboard=type_of_tabletop,
    resize_keyboard=True,
    input_field_placeholder="Выберите столешницу из списка",
    one_time_keyboard=True
)

first_city = "📍 Армавир"
second_city = "📍 Ставрополь"
third_city = "📍 Черкесск"
forth_city = "📍 Невинномысск"
fivth_city = "📍 Майкоп"
sixth_city = "📍 Кропоткин"
seventh_city = "📍 Другое"
city_kitchen = [
    [KeyboardButton(text=first_city),
    KeyboardButton(text=second_city)],
    [KeyboardButton(text=third_city),
    KeyboardButton(text=forth_city)],
    [KeyboardButton(text=fivth_city),
    KeyboardButton(text=sixth_city)],
    [KeyboardButton(text=seventh_city)]
]
city_kitchen_keyboard = ReplyKeyboardMarkup(
    keyboard=city_kitchen,
    resize_keyboard=True,
    input_field_placeholder="Выберите, из какого Вы города",
    one_time_keyboard=True
)

phone_key = [KeyboardButton(text="Отправить номер телефона", request_contact=True)]
phone_keyboard = ReplyKeyboardMarkup(keyboard=[phone_key],
                                     resize_keyboard=True,
                                     input_field_placeholder="Введите номер телефона или нажмите кнопку")

delete_keyboard = ReplyKeyboardRemove()
#tg_channel_button = [
#    [InlineKeyboardButton(text="Перейти в телеграмканал 'Кухни Катрин'", url="https://t.me/kuhni_katrin")],
#]
tg_channel_1 = "3D-проект"
tg_channel_button =[
    [KeyboardButton(text=tg_channel_1, web_app=WebAppInfo(url='https://thankskuhni.tilda.ws/'))],
]
tg_channel_keyboard = ReplyKeyboardMarkup(keyboard=tg_channel_button,
                                          resize_keyboard=True,
                                          input_field_placeholder="Выберите вариант ниже")
tg_channel_2 = "На канал"
tg_channel_inline_button = [
    [InlineKeyboardButton(text=tg_channel_2, url="https://t.me/kuhni_katrin")],
]
tg_channel_inline_kb = InlineKeyboardMarkup(inline_keyboard = tg_channel_inline_button)

firing_reply = ReplyKeyboardBuilder()
firing_reply.button(text=text.firing_button_phone)
firing_reply.button(text=text.firing_button_whatsapp)
firing_reply.adjust(2)


firing2_reply = ReplyKeyboardBuilder()
firing2_reply.button(text=text.firing_button_on_phone)
firing2_reply.button(text=text.firing_button_on_whatsapp)
firing2_reply.adjust(2)


firing3_reply = ReplyKeyboardBuilder()
firing3_reply.button(text=text.firing_button_meeting)
firing3_reply.button(text=text.firing_button_consult)
firing3_reply.adjust(2)

