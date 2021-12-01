import asyncio
from aiogram import Dispatcher, Bot, executor, types
from datetime import datetime
import config
import markup as nav
import funcs


TOKEN = config.BOT_TOKEN

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    with open("work.txt", "w", encoding="utf-8") as file_write:
        file_write.write("True")
    await bot.send_message(message.chat.id, text="Бот запущено.", reply_markup=nav.mainMenu)
    await my_func()


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    text = ['/start - розпочинає роботу бота, для кожного учасника працює окремо',
            '/help - довідка',
            '/show - показує чергового та жителів кімнати',
            '/add - добавляє нового жителя за введеним іменем',
            '/delete - видаляє жителя за введеним іменем',
            '/stop - зупиняє роботу бота (для всіх)']
    await bot.send_message(message.chat.id, text='\n'.join(text))


@dp.message_handler()
async def bot_message(message: types.Message):
    with open("work.txt", "r", encoding="utf-8") as file_read:
        if file_read.readline() == "True":
            if message.text == '🤱показати чергового' or message.text == "/show":
                await bot.send_message(message.chat.id, text=funcs.show_duty())

            elif message.text == '💑додати жильця':
                await bot.send_message(message.chat.id, text="/add {ім'я жителя}")

            elif message.text.split()[0] == "/add":
                await bot.send_message(message.chat.id, text=funcs.add_roommate("".join(message.text.rstrip().split()[1:])))

            elif message.text == '☠️видалити жильця':
                await bot.send_message(message.chat.id, text="/del {ім'я жителя}")

            elif message.text.split()[0] == "/del":
                await bot.send_message(message.chat.id, text=funcs.delete_roommate("".join(message.text.rstrip().split()[1:])))

            elif message.text.split()[0] == "/stop":
                with open("work.txt", "w", encoding="utf-8") as file_write:
                    file_write.write("False")
                await bot.send_message(message.chat.id, text="Бота призупинено")



loop = asyncio.get_event_loop()
delay = 60.0

async def my_func(): # міняємо чергового
    with open("work.txt", "r", encoding="utf-8") as file_read:
        if file_read.readline() == "True":
            mess = funcs.distribution(datetime.now())
            if len(mess):
                await bot.send_message("-604531942", text=mess)
    when_to_call = loop.time() + delay
    loop.call_at(when_to_call, my_callback)

def my_callback():
    asyncio.ensure_future(my_func())




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
