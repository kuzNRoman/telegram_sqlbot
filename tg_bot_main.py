from config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import Text
import json

import re
import sys

bot = Bot(token=token)
dp = Dispatcher(bot)

# keyboard_main
imp_info_button = types.KeyboardButton("🤓 Полезная информация")
cheatsheet_button = types.KeyboardButton("📗 Шпаргалка")
cases_button = types.KeyboardButton("📙 Кейсы")
keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.add(cheatsheet_button)
keyboard_main.add(cases_button)
keyboard_main.add(imp_info_button)

# keyboard_info_imp
courses_button = types.KeyboardButton("🖥 Видео-уроки и курсы")
trainers_button = types.KeyboardButton("💻 Тренажеры SQL")
back_button = types.KeyboardButton("Назад")
keyboard_info_imp = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_info_imp.add(courses_button)
keyboard_info_imp.add(trainers_button)
keyboard_info_imp.add(back_button)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(
        "Добрый день!\nДанный бот призван бесплатно распространять полезную информацию и уроки для начинающих и продвинутых пользователей SQL.\n\nВы можете скачать <b>PDF файл с полным описанием функционала баз данных SQL</b> - детально разобраны функции и их применение в MSSQL, MySQL и Postgres (учитывая особенности каждой базы), нажав на <b>кнопку 📗 Шпаргалка</b>.\n\nТакже вы можете скачать <b>PDF файл с собранными вопросами и заданиями с разных собеседований по SQL</b>, нажав <b>кнопку 📙 Кейсы</b>\n\nЛибо вы можете воспользоваться кнопкой Разделы и поискать информацию там.",
        parse_mode="HTML",
        reply_markup=keyboard_main,
    )


@dp.message_handler(Text(equals="📗 Шпаргалка"))
async def tarifs(message: types.Message):
    report_file = open(f"Cheatsheet_SQL.pdf", "rb")
    await bot.send_document(
        message.from_user.id,
        report_file,
        caption="\nВ присланном файле👆 содержится описание большей части функций SQL с разбором специфики их применения в MSSQL, MySQL, Postgres.\n\n Надеюсь, этот файл поможет Вам в изучении языка SQL или будет служить отличной 'шпаргалкой' для уже практикующих пользователей😉",
        parse_mode="HTML",
        reply_markup=keyboard_main,
    )


@dp.message_handler(Text(equals="📙 Кейсы"))
async def tarifs(message: types.Message):
    report_file = open(f"Cases_sql.pdf", "rb")
    await bot.send_document(
        message.from_user.id,
        report_file,
        caption="\nВ присланном файле👆 содержатся вопросы с ответами на все найденные мной в интернете собесодвания по SQL на позиции, связанные с аналитикой данных.\n\nПриятного пользования👍",
        parse_mode="HTML",
        reply_markup=keyboard_main,
    )


@dp.message_handler(Text(equals="🤓 Полезная информация"))
async def tarifs(message: types.Message):
    await message.answer(
        "Данный раздел содержит полезные ссылки на уроки и курсы (платные и бесплатные), ссылки на тренажеры по sql и многое другое!",
        parse_mode="HTML",
        reply_markup=keyboard_info_imp,
    )


@dp.message_handler(Text(equals="🖥 Видео-уроки и курсы"))
async def tarifs(message: types.Message):
    await message.answer(
        "<b>Полезные уроки и курсы:</b>\nШкола менеджмента Яндекс\nhttps://www.youtube.com/watch?v=LGwy0QmMvOE\nКурс Stepik - Научное мышление\nhttps://stepik.org/course/578/promo",
        parse_mode="HTML",
        reply_markup=keyboard_info_imp,
    )


@dp.message_handler(Text(equals="Назад"))
async def tarifs(message: types.Message):
    await message.answer(
        "Вы вернулись в главное меню",
        parse_mode="HTML",
        reply_markup=keyboard_main,
    )


if __name__ == "__main__":
    executor.start_polling(dp)
