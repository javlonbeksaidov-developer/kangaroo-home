from telebot import types


class Keyboard:
    @staticmethod
    def login():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("🔐 LOGIN")

        btn2 = types.KeyboardButton("🏠 Uy qidirish")
        btn3 = types.KeyboardButton("🗺 Xaritadan ko'rish")

        btn4 = types.KeyboardButton("ℹ️ Biz haqimizda")

        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)

        return markup

    @staticmethod
    def main(is_admin=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("🏠 Uy qidirish")
        btn2 = types.KeyboardButton("🗺 Xaritadan ko'rish")

        btn3 = types.KeyboardButton("📋 Mening murojaatlarim")
        btn4 = types.KeyboardButton("📅 Agent bilan uchrashuv")

        btn5 = types.KeyboardButton("ℹ️ Biz haqimizda")
        btn6 = types.KeyboardButton("📞 Menejer bilan aloqa")

        btn7 = types.KeyboardButton("👤 Mening profilim")

        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
        markup.add(btn7)

        if is_admin:
            btn10 = types.KeyboardButton("⚙️ Admin panel")
            markup.add(btn10)

        return markup
