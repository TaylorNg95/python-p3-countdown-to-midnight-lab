# your code goes here!

import time

def countdown(int):
    start = int
    while(start > 0):
        print(f'{start} SECOND(S)!')
        start -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(int):
    start = int
    while(start > 0):
        print(f'{start} SECOND(S)!')
        start -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')
countdown_with_sleep(5)