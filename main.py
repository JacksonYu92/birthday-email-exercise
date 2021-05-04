##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib



month = dt.datetime.now().month
day = dt.datetime.now().day
today = (month, day)


data = pandas.read_csv("birthdays.csv")
birthday_dict ={(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_ppl = birthday_dict[today]

    letter_number = random.randint(1,3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        letter_to_send = "".join(line.replace('[NAME]', birthday_ppl["name"]).replace("Angela", "Jackson") for line in letter)
        # letter_to_send = letter.read()
        # letter_to_send.replace("[NAME]", birthday_ppl)
        # print(letter_to_send)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_ppl.email,
            msg=f"Subject:Happy Birthday\n\n{letter_to_send}"
        )





