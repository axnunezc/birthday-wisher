import smtplib
from datetime import datetime
import pandas
import random

email = "axelbirthdaywisher@gmail.com"
password = "yrmfzxsnmizmejyt"

now = datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", person["name"])

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)

    try:
        connection.sendmail(from_addr=email, to_addrs=person["email"], msg=f"Subject:Happy Birthday\n\n{new_content}")
    except NameError:
        print("It is not anyone's birthday")