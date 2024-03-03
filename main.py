from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import  WebAppInfo


TOKEN = open('TOKEN.txt', 'r').read()
bot = Bot(TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def stsrt(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton('Open web page', web_app=WebAppInfo(url='https://www.google.by/')))
    await message.answer("Hello, my friend!", reply_markup=markup)


executor.start_polling(dp)