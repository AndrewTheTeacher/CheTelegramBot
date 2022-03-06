import requests
import telebot
from auth_data import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, "Hello! Write down the IP to find information")

    @bot.message_handler(content_types=['text'])
    def send_info(message):
        response = requests.get(url=f'http://ip-api.com/json/{message.text}').json()
        ip = response['query']
        country = response['country'] + " " + response['regionName'] + " " + response['city']
        location = response['lat']
        location2 = response['lon']
        timezone = response['timezone']
        zip = response['zip']
        org = response['org']
        print(response)
        bot.send_message(
            message.chat.id,
            f'Hello! Here is what I have found: \n IP: {ip} \n REGION: {country} \n COORDINATES: {location} {location2} \n TIMEZONE: {timezone} \n ZIP: {zip} \n ORGANIZATION: {org}'
            )

    bot.infinity_polling()


def main():
    telegram_bot(token)


if __name__ == '__main__':
    main()
