#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if (number < 0):
    ld = ld * -1
print(f'Last digit of {number} is ', end='')
print(f'{ld}', end=' ')
if (ld > 5):
    print('and is greater than 5')
if (ld == 0):
    print('and is 0')
if (ld < 6 and ld != 0):
    print('and is less than 6 and not 0')
