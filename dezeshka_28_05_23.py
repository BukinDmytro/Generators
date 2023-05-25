#1

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