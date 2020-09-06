from you import User
import math
import random

def main():

    while True:
        print("Welcome to your very own password locker")
        print('/n')
        print("Type in a short code to select your option:to create new user use 'nu': To login to your account use 'li' or 'ex' to exit current activity")
        code = input().lower()

        if code == 'nu':
            print("create user name please")
            created_user = input()

            print("create password now")
            created_pass = input()

            print("Confirm password")
            confirm_pass = input()

            while confirm_pass != created_pass:
                print("Invalid password, better luck next time")
                print("Enter your password again")
                created_pass = input()
                print("Confirm your password")
                confirm_pass = input()

            else:
                print(f"Amazing {created_user}! account created")
                print("Head over to login")
                print("Username please")
                inputted_user = input()
                print("Password")
                inputted_password = input()

            while inputted_user != created_user or inputted_password != created_pass:
                print("Invalid username or password, better luck next time")
                print("Username again")
                inputted_user = input()
                print("Password again")
                inputted_password = input()

            else:
                print(f"Welcome {inputted_user} to your account")

            if code == 'li':
                print("Welcome buddy")
                print("Enter username")
                main_user = input()

                print("Enter password here")
                main_password = input()

            while main_user != 'testuser' or main_password != '01234':
                print("Wrong username or password . Username 'testuser' and password '01234'") #enter username in text form and password as digit details
                print("Enter username")
                main_user = input()

                print("Enter password again")
                main_password = input()

            else:
                print("Login complete")
                print("\n")
                print("\n")

            if code == 'ex':
                break
            else:
                print("Enter a valid code to proceed")

if __name__ == '__main__':
    main()
