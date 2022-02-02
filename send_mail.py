import smtplib
from config import *


def send_mail(msg):




    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_MAIL, PASSWORD)
    server.sendmail(SENDER_MAIL, REC_MAIL, msg)
