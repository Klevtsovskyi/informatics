#T17_22
#Обчислення n-го числа Фібоначчі. Рекурсивний та нерекурсивний варіант
#Використано декоратори @benchmark та @trace

from t17_11_benchmark_v3 import *
from t17_21_trace import *

d = input('Відслідковувати виклики? [y/n]')[0]
debug = d == 'y'

def fibrec(n):
    '''Обчислення n-го числа Фібоначчі. Рекурсивний варіант.
    '''
    if n <= 1:
        rez = 1
    else:
        rez = fibrec(n-1) + fibrec(n-2)
    return rez

@trace(debug)           #Декоратор для трасування функції
@benchmark              #Декоратор для вимірювання часу роботи функції
def fibrecursive(n):
    '''Виклик рекурсивної функцї обчислення n-го числа Фібоначчі.

    Необхідно описати доадткову функцію для вимірювання загального часу роботи
    рекурсивного варіанту обчислення чисел Фібоначчі.
    Якщо поставити декоратор перед функцією fibrec, ми побачимо послідовність
    з замірів часу для виконання кожного окремого рекурсивного виклику.
    '''
    return fibrec(n)

@trace(debug)           #Декоратор для трасування функції
@benchmark              #Декоратор для вимірювання часу роботи функції
def fibiter(n):
    '''Обчислення n-го числа Фібоначчі. Нерекурсивний варіант.
    '''
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    return a

        
def fibgen(n):
    '''Генератор-функція чисел Фібоначчі до n.'''
    i = 0
    a, b = 1, 1
    while True:
        i = i + 1
        if i > n:                   #якщо дійшли до n              
            raise StopIteration     #зупиняємось
        yield b
        a, b = b, a + b

@trace(debug)           #Декоратор для трасування функції
@benchmark              #Декоратор для вимірювання часу роботи функції
def fibgenerator(n):
    '''Виклик генератора-функцї для обчислення n-го числа Фібоначчі.

    Необхідно описати доадткову функцію для вимірювання загального часу роботи
    генератора-функції обчислення чисел Фібоначчі.
    Якщо поставити декоратор перед функцією fibgen, ми побачимо послідовність
    з замірів часу для виконання кожного окремого виклику генератора-функції.
    '''
    for x in fibgen(n):
        pass
    return x



fs = [fibiter, fibrecursive, fibgenerator]    #список функцій для обчислення числа Фібоначчі
n = int(input('n=? '))
for f in fs:
    print('\n{}'.format(f.__name__))
    print('fib({0}) = {1}'.format(n,f(n)))
