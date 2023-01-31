import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink
from aiogram.dispatcher.filters import Text
from config import token
from parser_vacancies import check_vacancies_update_from_yandex
from parser_vacancies import check_vacancies_update_from_vk


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = [
        "Все вакансии",
        "Свежие вакансии Яндекса",
        "Свежие вакансии ВК"
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Посмотри вакансии:", reply_markup=keyboard)


@dp.message_handler(Text(equals="Все вакансии"))
async def get_all_vacancies(message: types.Message):
    with open("vacancies_dict.json", encoding="utf-8") as file:
        vacancies_dict = json.load(file)

    for k, v in vacancies_dict.items():
        vacancies = f'{hlink(v["vacancy_title"], v["vacancy_url"])}'

        await message.answer(vacancies)


@dp.message_handler(Text(equals="Свежие вакансии Яндекса"))
async def get_fresh_vacancies_yandex(message: types.Message):
    fresh_vacancies = check_vacancies_update_from_yandex()

    if len(fresh_vacancies) >= 1:
        for k, v in fresh_vacancies.items():
            vacancies = f'{hlink(v["vacancy_title"], v["vacancy_url"])}'

            await message.answer(vacancies)
    else:
        await message.answer("Нет свежих вакансий")


@dp.message_handler(Text(equals="Свежие вакансии ВК"))
async def get_fresh_vacancies_vk(message: types.Message):
    fresh_vacancies = check_vacancies_update_from_vk()

    if len(fresh_vacancies) >= 1:
        for k, v in fresh_vacancies.items():
            vacancies = f'{hlink(v["vacancy_title"], v["vacancy_url"])}'

            await message.answer(vacancies)
    else:
        await message.answer("Нет свежих вакансий")

if __name__ == "__main__":
    executor.start_polling(dp)
