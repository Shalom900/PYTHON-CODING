import random
import string
import smtplib
from email.mime.text import MIMEText
from passlib.hash import sha256_crypt
def get_hashed_password():
    user_password = input("Enter your Password: ")
    return sha256_crypt.using(rounds=1000).hash(user_password)
def verify_password(hashed_password, user_input):
    return sha256_crypt.verify(user_input, hashed_password)

def generate_random_password(length=12):
    Character = string.ascii_letters + string.digits + string.punctuation
    Password = ''.join(random.choice(Character) for i in range(length))
    return Password

def send_email(to_address, subject, body):
    from_address = "shalomobinna900@gmail.com"
    password = "your_password"

    message = MIMEText(body)
    message["subject"] = subject
    message["From"] = from_address
    message["To"] = to_address
    
Shalom_1 = str(input("Input your name:  "))
try:
    input_Age =(input("input your AGE:   "))
    Age = input_Age.split()
    Shalom_2 = (Age)
except ValueError:
    print("Error Please provide the correct value")
    
try:
    input_string = input("Input your birth month, day and year (e.g. 'August 15 2001'):   ")
    month, day, year = input_string.split()
    Shalom_3 = (month, int(day), int(year))
except ValueError:
    print("Please provide the input in the correct format, e.g., 'August 21 2001'")

random_password = generate_random_password()
print("Random Password:", random_password)


hashed_password = get_hashed_password()

login_attempt = input("CONFIRM YOUR PASSWORD: ")
if verify_password(hashed_password, login_attempt):
    print("Password is correct!")
else:
    print("Incorrect password.")


try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_address, password)
            server.sendmail(from_address, to_address, message)
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")

user_email = input("Enter recipient's email address:  ")
subject = input("Enter email subject: ")
body = input("Enter email body:  ")

send_email(user_email, subject, body)





    
