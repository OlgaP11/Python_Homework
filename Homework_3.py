# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# from random import randint

# def creat_list (length):
#     new_list = list ()
#     for i in range (length):
#         new_list.append(randint (-100, 100))
#     return new_list

# user_length = int(input('Input length of list: '))
# user_list = creat_list(user_length)
# print (user_list)
# user_sum = 0
# for i in range(1, user_length, 2):
#     user_sum += user_list[i]
# print (user_sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint

# def multiplication_elems (specified_range, specified_list):
#     multies = list()
#     multi_2_elems = 0
#     j = len(specified_list) - 1
#     for i in range (specified_range):
#         multi_2_elems = specified_list[i] * specified_list[j]
#         j -= 1
#         multies.append(multi_2_elems)
#         multi_2_elems = 0
#     return multies

# length = randint(5, 10)
# new_list = list ()
# for i in range(length):
#     new_list.append(randint(-10,10))
# print (new_list)

# if length%2 == 0:
#     print(multiplication_elems (len(new_list)//2, new_list))   
# else:
#     print(multiplication_elems (len(new_list)//2, new_list))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

#from random import random, randint

# length = 6
# numbers = list()
# for i in range(0, length):
#     numbers.append(round(randint(0,10) + random (),2))
# print (numbers)

# max_frac_part = 0
# min_frac_part = numbers[0]%1

# for i in range(0, length-1):
#     if numbers[i]%1 > max_frac_part:
#         max_frac_part = numbers[i]%1
#     elif numbers[i]%1 < min_frac_part:
#         min_frac_part = numbers[i]%1
# diff_between_frac_part = round(max_frac_part - min_frac_part, 2)
# print (diff_between_frac_part)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def binary_system (num):
#     result = ''
#     while num != 0:
#         result = str(num%2) + result
#         num = num // 2
#     return result

# user_num = int(input('Input number: '))
# print (f'Numbers {user_num} in binary system is {binary_system(user_num)}')

# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def fib (num):
#     if num in [1,2]:
#         return 1
#     else:
#         return fib (num-1) + fib (num -2)

# num = 8
# fib_list = list((0,))
# for i in range (1,num+1):
#     fib_list.append((-1)**(i+1)*fib(i))
# fib_list.reverse()
# for i in range (1,num+1):
#     fib_list.append(fib(i))

# print(fib_list)
