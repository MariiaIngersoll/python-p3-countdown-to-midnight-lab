import time

def countdown(number):
    i = number
    while i > 0:
        print(f'{i} SECOND(S)!')
        i -= 1
    if i == 0:
        print("HAPPY NEW YEAR!")
        
countdown(10)



def countdown_with_sleep(number):
    i = number
    while i > 0:
        print(f'{i} SECOND(S)!')
        time.sleep(1)
        i -= 1
    if i == 0:
        print("HAPPY NEW YEAR!")
        
countdown_with_sleep(10)