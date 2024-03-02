#!/usr/bin/env python3

import time

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)  # Sleep for 1 second between countdown
    print("Happy New Year!")

    # code goes here!
    pass

def square_integers(numbers):
    return [num ** 2 for num in numbers]

    # code goes here!
    pass

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

    # code goes here!
    pass
