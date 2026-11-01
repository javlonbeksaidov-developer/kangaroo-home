from telebot import types


class Keyboard:
    @staticmethod
    def main():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton(text="LOGIN")
        btn2 = types.KeyboardButton(text="REGISTER")

        markup.add(btn1, btn2)
        return markup
