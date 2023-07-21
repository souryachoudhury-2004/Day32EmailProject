# MONDAY MOTIVATIONAL QUOTE PROJECT

import sendEmail
import datetime
import random
import time

sender = sendEmail.Mailer()

while True:

    current_time = datetime.datetime.now()
    day_of_week = current_time.weekday()+1
    hour = current_time.hour

    if day_of_week == 1 and 7 <= hour <= 8:

        with open("quotes.txt", "r") as quotes:
            quotes_list = quotes.readlines()
            random_quote = random.choice(quotes_list)
            sender.post("souryachoudhury24@gmail.com", f"Subject: Motivational Monday Quote\n\n{random_quote}")

    time.sleep(3600)















