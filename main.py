# This quiz helps with Rutgers alumni
# Fail once, you fail.

import sys

print("RUaRealFan of Rutgers?")
print()

print("Rutgers University is one of the best universities in the world.")

print("With so many notable alumni, it has been a stable university to help improve your life.")
print()

print("With that said, this quiz will determine your knowledge of Rutgers alumni.")
print()

print("This quiz has five questions.")
print()

print("Let’s begin.")
print()

user_name = input("What is your name?: ")
print("Hello,", user_name + ", here are the questions below!")
print()

while True:
    try:
        print("Question 1: Which One of These Basketball/NBA Players DID NOT play for Rutgers?")
        print("Press Either 1, 2, 3, or 4.")
        user_input = int(input("1. Dahntay Jones\n2. Roy Hinson\n3. Ron Harper Jr.\n4. Samuel Dalembert\n"))
    except ValueError:
        print("That's invalid, try again")
        print()
        continue
    if user_input >= 5 or user_input <= 0:
        print("That's invalid, try again")
        print()
        continue
    elif user_input == 1 or user_input == 2 or user_input == 3:
        print()
        print("Sorry, Dahntay Jones was famous for hurting Kobe,")
        print("Roy Hinson averaged 14 points a game during his eight year NBA career,")
        print("and Ron Harper Jr. is on a two-way contract with the Raptors as of this writing.")
        print("Nice try though.")
        print()
        sys.exit()
    if user_input == 4:
        print()
        print("Great, Dalembert went to Seton Hall. So, onto the next question")
        print()
    while True:
        try:
            print("Question 2: Which One of These Actors WENT to Rutgers?")
            print("Press Either 1, 2, 3, or 4.")
            user_input = int(input("1. Dulé Hill\n2. Robert Desiderio\n3. James Gandolfini\n4. Alec Baldwin\n"))
        except ValueError:
            print("That's invalid, try again")
            print()
            continue
        if user_input >= 5 or user_input <= 0:
            print("That's invalid, try again")
            print()
            continue
        elif user_input == 1 or user_input == 2 or user_input == 4:
            print()
            print("Sorry, Dulé Hill and Robert Desiderio went to Seton and Alec Baldwin went to NYU")
            print("Better luck next time.")
            print()
            sys.exit()
        if user_input == 3:
            print()
            print("Great, Mr. Tony Soprano. Next Question")
            print()
            while True:
                try:
                    print("Question 3: David Stern Was The Commissioner of What Sports League For 30 Years?")
                    print("Press Either 1, 2, 3, or 4.")
                    user_input = int(input("1. NFL\n2. MLB\n3. NBA\n4. NHL\n"))
                except ValueError:
                    print("That's invalid, try again")
                    print()
                    continue
                if user_input >= 5 or user_input <= 0:
                    print("That's invalid, try again")
                    print()
                    continue
                elif user_input == 1 or user_input == 2 or user_input == 4:
                    print()
                    print("Sorry, but the NFL, MLB and NBA has never had a 30+ year commissioner as of this writing.")
                    print("Stern has been longest-tenured commissioner in the big four sports. Better luck next time.")
                    print()
                    sys.exit()
                if user_input == 3:
                    print()
                    print("Good job, onto the next question")
                    print()
                    while True:
                        try:
                            print("Question 4: When James Gandolfini Went to Rutgers in 1983, What Was His Major?")
                            print("Press Either 1, 2, 3, or 4.")
                            user_input = int(input("1. Communications\n2. Business\n3. Psychology\n4. Sociology\n"))
                        except ValueError:
                            print("That's invalid, try again")
                            print()
                            continue
                        if user_input >= 5 or user_input <= 0:
                            print("That's invalid, try again")
                            print()
                            continue
                        elif user_input == 2 or user_input == 3 or user_input == 4:
                            print()
                            print("Sorry, Gandolfini is definitely a bro, but Communications was his major.")
                            print("I made it hard on purpose.")
                            print()
                            sys.exit()
                        if user_input == 1:
                            print()
                            print("Great, that degree certainly helped with his acting career.")
                            print()
                            while True:
                                try:
                                    print("Question 5: Jim Valvano Coached Which NCAA Div. I Men's Basketball Program?")
                                    print("Press Either 1, 2, 3, or 4.")
                                    user_input = int(input("1. Rutgers\n2. Saint Peters\n3. NC State\n4. N.C.\n"))
                                except ValueError:
                                    print("That's invalid, try again")
                                    print()
                                    continue
                                if user_input >= 5 or user_input <= 0:
                                    print("That's invalid, try again")
                                    print()
                                    continue
                                elif user_input == 1 or user_input == 2 or user_input == 4:
                                    print()
                                    print("Sorry, though confusing, Jimmy V played basketball in Rutgers in college.")
                                    print("Then, he became their assistant coach.")
                                    print("In the 1983 NCAA finals, he coached North Carolina State to a tile")
                                    print("So close, but till next time.")
                                    print()
                                    sys.exit()
                                if user_input == 3:
                                    print()
                                    print("Alright you all questions right! You R truly a Real Fan of Rutgers U.")
                                    print()
                                    sys.exit()