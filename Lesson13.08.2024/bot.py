from secret import token
import telebot
bot = telebot.TeleBot(token)
# декорированные ожидания сообщений появятся тут
bot.polling(none_stop=True)
@bot.message_handler(commands=['start'])
def start(message):
  user_id = message.from_user.id

with open('user_ids.txt', 'a') as file:
        file.write(f'{user_id}\n')
    
bot.reply_to(message, "Привет! Ваш ID сохранен.")

# Запускаем бота
bot.polling()