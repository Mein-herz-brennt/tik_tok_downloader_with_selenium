from aiogram import Bot, Dispatcher, executor, types
from tiktok_parser import *
import os
from random import randint
TOKEN = "1905664044:AAHng-M7s1yompWdVfpZYPV6qzVxhRFMV3o"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await message.answer(
        "Привет ,я бот,  создан что-бы упростить твою \n жизнь и помочь тебе скачать \n📲 видео с tic-tok без водных "
        "знаков\n "
        "Пожалуйста отправь мне ссылочку на видео")


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer("Для того что-бы скачать 📲 видео\n"
                         "с Tik-Tok без водного знака,\n"
                         "просто отправь  мне ссылку на это видео!")


@dp.message_handler(content_types=['text'])
async def link_message(message: types.Message):
    _id = message.from_user.id
    name = message.from_user.full_name
    print(name)
    user = message.from_user.username
    link = message.text
    if link.startswith("https://www.tiktok.com/"):
        try:
            directory = f"downloads{user}"
            os.mkdir(f"downloads{user}")
        except Exception as ex:
            num = randint(1, 99)
            print(ex)
            directory = f"downloads{user}{_id}{num}"
            os.mkdir(f"downloads{user}{_id}{num}")
        # print(directory)
        path = os.getcwd()
        await message.answer("Идёт загрузка пожалуста подождите...")
        tikitoki(link, directory)
        files = os.listdir(rf"{path}\{directory}")
        # print(file[0])
        filename = types.InputFile(rf"{path}\{directory}\{files[0]}",
                                   files[0])
        await message.answer_video(filename)
        await message.answer("Видео успешно загружено!😉")
        # time.sleep(1)
        os.remove(rf"{path}\{directory}\{files[0]}")
        os.removedirs(directory)
        await message.answer("С нетерпением жду следующую ссылочку!😊")
    else:
        await message.answer("Извините но я не знаю что это значит!😢")
        await message.answer("Пришлите пожалуйста ссылочку на видео")


executor.start_polling(dp)
