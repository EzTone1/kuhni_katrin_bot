from aiogram.fsm.state import StatesGroup, State

class StepOfBot(StatesGroup):
    idle = State()
    style_of_kitchen_state = State()
    length_of_kitchen_state = State()
    form_of_kitchen_state = State()
    tabletop_of_kitchen_state = State()
    price_of_kitchen_state = State()
    city_of_kitchen_state = State()
    number_not_given = State()
    number_given = State()