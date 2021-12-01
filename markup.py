from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, reply_keyboard


# --- Main menu ---
show_duty = KeyboardButton('🤱показати чергового')
add_roommate = KeyboardButton('💑додати жильця')
delete_roommate = KeyboardButton('☠️видалити жильця')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(show_duty, add_roommate, delete_roommate)
