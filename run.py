from you import User
import math
import random

def main():

    while true:
        print("Welcome to your very own password locker")
        print('/n')
        print("Type in a short code to select your option:to create new user use 'NU':To login to your account use 'LI' or 'EX' to exit current activity")
        code = input().lower
        print('\n')

        if code == 'NU':
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
                print('\n')
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
                print('\n')        

























if __name__ == '__main__':
    main()
