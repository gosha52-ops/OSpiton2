import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
    load_dotenv()
    msg = MIMEMultipart()
    msg["From"] = "georgrotaru@yandex.com"
    msg["To"] = "georgrotaru@yandex.com"
    msg["Subject"] = "Важное сообщения!"
    completed_module = ["Python Введение","Web Разроботка",]
    progress_module = ["Основы Python","Продвинутая верстка"]
    time = "3 года"
    text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. В процессе я выполнил модули: {completed_module}! Сейчас я работаю над модулями {progress_module}. Обучение мне нравится, я получил море знаний!"
    if not completed_module:
        text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями {progress_module}. Пока что я улучшаю свои навыки и узнаю много нового!"
    msg.attach(MIMEText(text, "plain"))
    server = smtplib.SMTP_SSL('smtp.yandex.com',465)
    password = os.getenv("PASSWORD")
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg["To"],msg.as_string())
    server.quit()


if __name__ == '__main__':
    main()