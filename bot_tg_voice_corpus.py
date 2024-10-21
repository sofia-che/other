import telebot
from telebot import types
import config
import dbworker
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, '<b>Добрый день!</b> Благодарим Вас за участие в нашем исследовании голосовых сообщений как нового жанра устной повседневной речи. Перед тем, как отправить нам свои голосовые сообщения, заполните, пожалуйста, анкету участника. Нажимая на кнопку /confirm, вы автоматически подтверждаете своё согласие на участие в проекте.', parse_mode='html')
    dbworker.set_state(message.chat.id, config.States.S_ENTER_SEX.value)


@bot.message_handler(commands=['confirm'], func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_SEX.value)
def enter_sex(message):
    markup = types.ReplyKeyboardMarkup()
    male = types.KeyboardButton('Мужской')
    female = types.KeyboardButton('Женский')
    other = types.KeyboardButton('Другое/Не хочу отвечать')
    markup.add(male, female, other)
    bot.send_message(message.chat.id, 'Укажите, пожалуйста, ваш пол', reply_markup=markup)
    dbworker.set_state(message.chat.id, config.States.S_ENTER_AGE.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_AGE.value)
def enter_age(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, 'Укажите, пожалуйста, Ваш возраст в виде целого числа')
        return
    if int(message.text) < 18:
        bot.send_message(message.chat.id, 'К сожалению, Вы не можете принять участие в исследовании. Дождитесь наступления совершеннолетия.')
        return
    elif int(message.text) >= 100:
        bot.send_message(message.chat.id, 'С целью получения корректных результатов исследования мы просим участников указывать реальный возраст.')
        return
    else:
        bot.send_message(message.chat.id, 'Укажите Ваш первый (родной) язык')
        dbworker.set_state(message.chat.id, config.States.S_ENTER_LANGUAGE.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_LANGUAGE.value)
def enter_language(message):
    if not message.text.isalpha():
        bot.send_message(message.chat.id, 'Попробуйте ещё раз')
        return
    else:
        bot.send_message(message.chat.id, 'Укажите город, в котором вы росли. Если вы росли не в России, напишите "Другое"')
        dbworker.set_state(message.chat.id, config.States.S_ENTER_CITY.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_CITY.value)
def enter_city(message):
    if not message.text.isalpha():
        bot.send_message(message.chat.id, 'Попробуйте ещё раз')
        return
    else:
        bot.send_message(message.chat.id, 'Спасибо за заполнение анкеты! Перешлите, пожалуйста, свои голосовые сообщения, которые Вы готовы предоставить для нашего исследования.')
        dbworker.set_state(message.chat.id, config.States.S_ENTER_AUDIO.value)


@bot.message_handler(content_types=['audio', 'voice'], func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_AUDIO.value)
def enter_audio(message):
    bot.send_message(message.chat.id, 'Большое спасибо за участие! Вы можете прислать неограниченное количество голосовых сообщений. Если Вы прислали всё, что хотели, нажмите /start')
    return


@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Подтвердите своё участие в исследовании, нажав на кнопку /confirm')
    dbworker.set_state(message.chat.id, config.States.S_ENTER_SEX.value)


bot.polling(none_stop=True)


channel_id = '-1001819222472'


def text_message(update, context):
    user_message = update.message.text
    bot.send_message(chat_id=channel_id, text=user_message)


def voice_message(update, context):
    voice_file = update.message.voice.file_id
    bot.send_voice(chat_id=channel_id, voice=voice_file)


def main():
    updater = Updater(token=config.token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, text_message))
    dp.add_handler(MessageHandler(Filters.voice, voice_message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()