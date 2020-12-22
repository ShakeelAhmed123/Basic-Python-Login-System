import random

user_file = {}
operation = ""
print("#####################")
print("#    Login Screen   #")
print("#####################")

def start_screen():
    operation = input("Input operation, '1' for Login or '2' for Signup or 3 to quit > ")

    if operation == "1":
        login()

    elif operation == "2":
        sign_up()





def sign_up():
        new_username = input("Enter your Username > ")

        if new_username in user_file:
            print("Username already exists")

        else:
            print("Prove that you are not a robot")

            cap = captcha()

            if cap is True:

                confirm_new_username = input("Confirm Username > ")

                if new_username == confirm_new_username:
                    new_password = input("Enter Password > ")
                    confirm_new_password = input("Confirm Password > ")

                    if new_password == new_username:
                        print("Password cannot be the same as the Username.")

                    else:
                        if new_password == confirm_new_password:
                            user_file[new_username] = new_password
                            print("User created, you may now login")

                        else:
                            print("Passwords do not match")

                else:
                    print("Usernames do not match")
            else:
                print("Captcha is incorrect")


def captcha():
    int1 = random.randint(1, 100)
    int2 = random.randint(1, 100)

    user_ans = int(input(f"{int1} + {int2} = "))
    answer = int1 + int2
    if user_ans == answer:
        print("You are not a robot.")
        return True



def login():
    login = input("Enter Username > ")
    password = input("Enter Password > ")

    print("Prove that you are not a robot")

    cap = captcha()

    if cap is True:

        if login in user_file and user_file[login] == password:
            print(f"Logged in as {login}")

        else:
            print("User does not exist or wrong password/username")

    else:
        print("Captcha is wrong.")


while operation != "3":
    start_screen()