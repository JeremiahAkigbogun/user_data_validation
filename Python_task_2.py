import string
import random


def user_details():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    user_email = input("Please enter your email address: ")

    details = [first_name, last_name, user_email]
    return details


def gen_password(details):
    characters = string.ascii_lowercase
    length = 5
    random_password = '' .join(random.choice(characters)for i in range(length))
    password = str(details[0][0:2] + details[1][-2:] + random_password)
    return password


status = True
container = []

while status:
    details = user_details()

    password = gen_password(details)
    print("your password is: " + password)

    password_like = input("Do you like the generated password? Yes or No: (Note that characters are case sensitive) ")

    password_loop = True
    while password_loop:
        if password_like == 'Yes':
            details.append(password)
            container.append(details)
            print("Your details has been recorded. ")
            print(details)

            password_loop = False

        else:
            user_password = input("Enter password of 7 or more characters: ")
            password_len = True
            while password_len:
                if len(user_password) >= 7:
                    details.append(user_password)
                    container.append(details)
                    print("Your details has been recorded. ")
                    print(details)

                    password_len = False

                    password_loop = False
                else:
                    print("Your password has less than 7 characters")
                    user_password = input("Enter password of 7 or more characters: ")


def fresh_user():
    new_user = input("Would you like to enter te details of a new user? Yes or No. ")
    if new_user == 'No':

        status = False
        for item in details:
            print(item)

        else:
            status = True

            return new_user



fresh_user()