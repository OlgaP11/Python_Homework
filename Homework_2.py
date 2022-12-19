# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# def find_sum (number):
#     sum = 0
#     while number != 0:
#         digit = number % 10
#         sum += digit
#         number = number // 10
#     return sum

# num = float(input('Input number: '))
# if num%1 == 0:
#     user_sum = find_sum (num)
# else:
#     rest = num%1
#     while rest % 1 != 0:
#         rest *= 10
#     num = num // 1
#     user_sum = find_sum (rest) + find_sum (num)

# print (round(user_sum))

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return factorial (n-1) * n

# user_num = int(input('Input integer number: '))
# factorials = list (range(1, user_num + 1))
# num = 1
# for i in range(0, user_num):
#     factorials[i] = factorial(num)
#     num += 1
# print (factorials)

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# num = int (input('Input number: '))
# numbers = list(range (1, num+1))
# n = 1
# for i in range (0, num-1):
#     numbers[i] = round(((1+1/n)**n), 2)
#     n += 1
# print (numbers)
# print (f"Sum of list's numbers is {sum(numbers)}")

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# length = int (input("Input length of the list: "))
# numbers = list (range (-length, length))
# print (numbers)

# data = open ('HW2_file.txt', 'r')
# multi = 1
# for line in data:
#     multi *= numbers[int(line)]
# print (multi)

# 5. Реализуйте алгоритм перемешивания списка.

# import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range (1,len(numbers)):
#     r = random.randrange (0, len(numbers)-1)
#     temp = numbers [i]
#     numbers [i] = numbers [r]
#     numbers [r] = temp

# print (numbers)