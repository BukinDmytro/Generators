#1
'''
def generate_num(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    current = 2
    while True:
        if generate_num(current):
            yield current
        current +=1
gen = prime_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''

#2
'''
def average_closure():
    numbers = []
    def add_number(number):
        numbers.append(number)
    def get_avg():
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    return add_number , get_avg

add_num , get_average = average_closure()
add_num(10)
add_num(5)
add_num(100)
print(get_average())
'''

#3

import random

class PasswordGenerator:
    def __init__(self,length,characters):
        self.length = length
        self.characters = characters

    def generate_password(self):
        password = ''.join(random.choice(self.characters) for i in range(self.length))
        return password

password_gen = PasswordGenerator(length = 8 , characters = ":GYE^%#($Whgeuihgeew[qifjdio857345238911")

print(password_gen.generate_password())
print(password_gen.generate_password())
print(password_gen.generate_password())

