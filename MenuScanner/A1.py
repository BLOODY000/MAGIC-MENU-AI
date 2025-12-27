import telebot
from telebot import types
import requests

TOKEN = "8398741876:AAE1eocjsuZNaNz3XcNZggA81vBwaXZKnqo"
WEATHER_API_KEY = "12a34567890bcdef1234567890abcdef"

bot = telebot.TeleBot(TOKEN)


def get_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Погода в Москве", "Погода в СПБ")
    markup.add("Прогноз на 5 дней", "Расскажи шутку")
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот запущен!", reply_markup=get_main_keyboard())


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Команды: /start, /help, /photo\nИли просто напиши город.")


@bot.message_handler(commands=['photo'])
def send_photo(message):
    bot.send_photo(message.chat.id, "https://picsum.photos/500/300")


def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
        res = requests.get(url)
        data = res.json()
        if data.get("cod") != 200:
            return "❌ Город не найден."
        return f"🌡 {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C"
    except:
        return "⚠️ Ошибка связи."


def get_forecast(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
        res = requests.get(url)
        data = res.json()
        if data.get("cod") != "200":
            return "❌ Не удалось получить прогноз."

        text = f"📅 Прогноз для {city}:\n"
        for i in range(0, 40, 8):
            day = data['list'][i]
            date = day['dt_txt'].split()[0]
            temp = day['main']['temp']
            text += f"{date}: {temp}°C\n"
        return text
    except:
        return "⚠️ Ошибка сервиса."


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Расскажи шутку":
        bot.send_message(message.chat.id, "Почему программисты не любят море? Там слишком много Windows и мало окон.")
    elif message.text == "Прогноз на 5 дней":
        bot.send_message(message.chat.id, "Напишите название города и слово 'прогноз' (например: Алматы прогноз)")
    elif "прогноз" in message.text.lower():
        city = message.text.lower().replace("прогноз", "").strip()
        bot.send_message(message.chat.id, get_forecast(city))
    elif "Погода в" in message.text:
        city = message.text.replace("Погода в ", "")
        bot.send_message(message.chat.id, get_weather(city))
    else:
        bot.send_message(message.chat.id, get_weather(message.text))


if __name__ == "__main__":
    bot.infinity_polling()