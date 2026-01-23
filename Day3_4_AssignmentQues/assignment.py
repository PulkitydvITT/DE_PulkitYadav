# function that takes two functions and a value as arguments.and return tuple as a result.

def func1(x):
    return x**2

def func2(x):
    return x**3

def func(func1, func2, values):
    result1 = func1(values)
    result2 = func2(values)
    return (result1, result2)

answer = func(func1, func2, 3)
print(answer)

# a simple iterator that iterates over a list of numbers.
 
class MyClass:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value
    
nums = MyClass([1,2,3,4,5])

for n in nums:
    print(n)

print()

#  generator function that yields squares of numbers up to a given limit.  
def square_generator(limit):
    for i in range(1, limit + 1):
        yield i * i

for it in square_generator(5):
    print(it)

# closure function that generates a series of numbers starting from a given base. 

def outer(base):
    current = base

    def inner():
        nonlocal current
        value = current
        current += 1
        return value

    return inner

a = outer(1)
print(a())
print(a())
print(a())
print(a())