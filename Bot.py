import telebot


bot = telebot.TeleBot("TOKEN", parse_mode=None)


def send_answer(answer, count):
    data = open('user_id.txt', 'r', encoding='utf-8')
    users_id = data.readlines()
    a = users_id[count]
    bot.send_message(a, f'{answer}')
    data.close()
    
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    def Help(message):
        user_id = str(message.from_user.id) +'\n'
        data = open('user_id.txt', 'a', encoding='utf-8')
        data.writelines(user_id)
        data.close()
        messageText = str(message.text) +'\n'
        data = open('message_text.txt', 'a', encoding='utf-8')
        data.writelines(messageText)
        data.close()
        bot.send_message(message.chat.id, 'Благодарю за обращение! Наш специалист уже работает над Вашим вопросом. Ожидайте...')

    r = bot.send_message(message.chat.id, 'Приветствую, ' + message.from_user.first_name + '!. Чем я могу Вам помочь? Напишите вопрос')
    bot.register_next_step_handler(r, Help)

bot.infinity_polling()





