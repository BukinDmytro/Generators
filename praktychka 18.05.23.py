#1
'''
# спосіб НОМЕР 1 ( галімий )
n = int(input("Введіть число:"))
for i in range (1,n + 1):
    if i % 2 != 0:
        print(i)
    else:
        pass
# спосіб НОМЕР 2 ( НЕ галімий )

lst = [1,2,3,4,5,6]
print(iter(lst))

class OddIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 2
        return value

for num in OddIterator(lst):
    print(num)

# спосіб Альбіни ПЕРЕПИСАТИ ТА ПОДИВИТИСЬ ТАКОЖ

'''
#2
'''
class SquareGenerator:
    def __init__(self,n):
        if not isinstance(n,(int,float)):
            raise TypeError
        self.n = n
    def generator_square(self):
        for i in range(1 , int(self.n) + 1):
            yield i ** 2
#приклад використання
try:
    for num in SquareGenerator(20).generator_square():
        print(num)
except ValueError as e:
    print(e)
'''
#3
'''
lst = [1,2,3,4,5,6]
print(iter(lst))

class ListIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

for num in ListIterator(lst):
    print(num)
'''

#4

def multiply_by():
    def mult(x,n):
        return x * n
    return mult
m = multiply_by()
print(m(int(input()), int(input())))






