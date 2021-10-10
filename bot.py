import telebot
import schedule
from time import sleep
import random
import datetime
from threading import Thread
f = open("ids.txt", 'r')
users = list(set([int(line.strip()) for line in f.readlines()]))
f.close()
bot = telebot.TeleBot("2099273366:AAFcJbLn-cAmvHRrFv7fF5cPkyaIC_XGtRY")
telegrams = ["https://t.me/joinchat/esRHkO3R-5gzZDRi", "https://t.me/joinchat/w4iVhwgSV4QwNWVi", "https://t.me/joinchat/a7wTE1i-pUo0Mzky", "https://t.me/joinchat/--2l4qvx580zZDEy"]
type_of_videos = ["https://www.youtube.com/watch?v=2SC-egblD0A", "https://us02web.zoom.us/j/87270669952?pwd=VG1KRndGMDB1TmdpRmFpOTU3TmFUdz09" + "\n" + "Идентификатор конференции: 872 7066 9952" + "\n" + "Код доступа: 973675"]

@bot.message_handler(commands=['start'])
def get_user_id(message):
    if message.from_user.id not in users:
        users.append(message.from_user.id)
    id = message.from_user.id
    f = open("ids.txt", 'w')
    result = ""
    for user in users:
        result += str(user) + "\n"
    f.write(result)
    f.close()
    print(len(users))
    try:
        bot.send_message(id, "Добавил тебя в расссылку. Ожидай ссылки за пять минут до начала занятия")
    except telebot.apihelper.ApiException:
        print("work")


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start")

def send_messages():
    for user_id in users:
        ind_telegrams = random.randint(0, 3)
        ind_videos = random.randint(0, 1)
    try:
        bot.send_message(user_id, "Ссылки на сегодняшнее занятие" + "\n" + "Занятие по ссылке: " + type_of_videos[ind_videos] +
                             "\n" + "Telegram: " +  telegrams[ind_telegrams])
    except telebot.apihelper.ApiException:
        print("work")

def send_messages_solutions():
    for user_id in users:
        ind_videos = random.randint(0, 1)
        try:
            bot.send_message(user_id, "Ссылки на разбор" + "\n" + "Занятие по ссылке: " + type_of_videos[ind_videos])
        except telebot.apihelper.ApiException:
            print("work")
def testing_message():
    print(datetime.datetime.now())
    for user_id in users:
        try:
            bot.send_message(user_id, "Тестируем рассылку, не обращайте внимание, извините что потревожили, это последний раз")
        except telebot.apihelper.ApiException:
            print("work")
    print(datetime.datetime.now())
def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)
if __name__ == "__main__":
    schedule.every().saturday.at("18:09").do(send_messages)
    schedule.every().saturday.at("10:00").do(send_messages)
    schedule.every().saturday.at("12:20").do(send_messages_solutions)
    schedule.every().saturday.at("19:45").do(send_messages_solutions)
    schedule.every().sunday.at("15:18").do(testing_message)
    Thread(target=schedule_checker).start()
    bot.infinity_polling(timeout=10, long_polling_timeout = 5)
