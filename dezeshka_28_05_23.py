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
