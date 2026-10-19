from decouple import config
from telebot import TeleBot

BOT_TOKEN = config("BOT_TOKEN")

bot = TeleBot(token=BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome(msg):
    bot.send_message(msg.chat.id, text=f"Welcome {msg.from_user.first_name} !")


@bot.message_handler(commands=["help"])
def help(msg):
    bot.send_message(msg.chat.id, text="Ko'chmas mulk")


if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
