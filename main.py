import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "Your App Password Key"

date_now = dt.datetime.now()
today = (date_now.month, date_now.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=MY_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}\n\n Best Regards\n From Farhan"
        )
