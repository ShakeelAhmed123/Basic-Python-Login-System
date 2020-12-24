import random

file = open("usernames.txt")  # Pretty important as it creates the file if its not there
file.close()

operation = ""
print("#####################")
print("#    Login Screen   #")
print("#####################")


def start_screen():
    operation_select = input("Input operation, '1' for Login or '2' for Signup or 3 to quit > ")

    if operation_select == "1":
        login()

    elif operation_select == "2":
        sign_up()

    elif operation_select == "3":
        exit()


def sign_up():
    username = input("Please input your desired username > ")
    uname_recheck = input("Please confirm your username > ")

    password = input("Please input your desired password > ")
    pass_recheck = input("Please confirm you password > ")

    user_file = open("usernames.txt", "a")
    print("Prove that you are not a robot:")

    cap = captcha()

    if cap is True:
        if username == uname_recheck and password == pass_recheck:
            user_file.write(username)
            user_file.write(" ")
            user_file.write(password)
            user_file.write("\n")
            user_file.close()
            print("Account successfully created, you may now login")
        else:
            print("Your usernames or passwords do not match! Please try again.")
    else:
        print("Captcha is incorrect")


def captcha():
    try:
        int1 = random.randint(1, 100)
        int2 = random.randint(1, 100)

        user_ans = int(input(f"{int1} + {int2} = "))
        answer = int1 + int2
        if user_ans == answer:
            print("You are not a robot.")
            return True

    except ValueError:
        print("Invalid Value")


def login():
    username = input("Enter Username > ")
    password = input("Enter Password > ")

    print("Prove that you are not a robot")

    cap = captcha()

    if cap is True:
        for line in open("usernames.txt", "r").readlines():  # Reads the lines in the u_name file
            login_info = line.split()  # Splits the text on the space, and store the results in a list of two strings

            if username == login_info[0] and password == login_info[1]:
                print(f"Logged in as {username}")

            else:
                print("User does not exist or wrong password/username")

    else:
        print("Captcha is wrong.")


while operation != 3:
    start_screen()
