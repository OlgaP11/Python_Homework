# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# from random import randint

# def rand_num(num):
#     num = randint(0,10)
#     return num

# length = int(input('Input length of list: '))
# nums = [rand_num(i) for i in range(length)]
# print(nums)

# new_nums = list()
# for i,elem in enumerate(nums):
#     if i%2 != 0:
#         new_nums.append(elem)

# print(new_nums)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return factorial (n-1) * n

# user_num = int(input('Input integer number: '))
# factorials = [(i,factorial(i)) for i in range(1,user_num+1)]
# print(factorials)

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# num = int (input('Input number: '))
# formula = lambda x: round(((1+1/x)**x), 2)
# numbers = [formula(i) for i in range(1,num+1)]
# print(numbers)
# print (f"Sum of list's numbers is {sum(numbers)}")



