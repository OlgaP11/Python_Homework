# 1. Вычислить число c заданной точностью d.

# from math import pi

# d = 0.001
# count = 0
# while d < 1:
#     d *= 10
#     count += 1
# print (round(pi, count))

# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def div_by_prime_number (user_list, user_num, prime_num):
#     while user_num%prime_num == 0:
#         user_list.append(prime_num)
#         user_num = user_num // prime_num
#     else:
#         if user_num > 1:
#             user_list.append(user_num)

# num = int (input('Input number form 0 till 100: '))
# list_prime_nums = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
# factors = list ()

# for i in range (len(list_prime_nums)):
#     if num%list_prime_nums[i]==0:
#         div_by_prime_number(factors,num,list_prime_nums[i])
#         break

# print(f'The list of prime factors is: {factors}')

# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# def count_repeat(user_list, num):
#     count = 0
#     for i in range (len(user_list)):
#         if num == user_list[i]:
#             count+=1
#     return count

# numbers = [1, 2, 3, 5, 1, 5, 6]
# new_list = []
# for i in range (len(numbers)):
#     if count_repeat(numbers, numbers[i]) == 1:
#         new_list.append(numbers[i])
# print (new_list)

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# from random import randint

# k = int (input('Input natural degree: '))
# for n in range (k, -1, -1):
#     a = randint(0,101)
#     if a != 0 and n != 0:
#         print(f'{a}*x^{n} + ', end ='')
#     elif a == 0:
#         print (f'x^{n} + ', end ='')
#     elif n == 0:
#         print(f'{a} = 0')

# 5.Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# with open ('HW_4_1.txt', 'r') as data_1:
#     for line in data_1:
#         statment_1 = line
#         print(statment_1)

# with open ('HW_4_2.txt', 'r') as data_2:
#     for line in data_2:
#         statment_2 = line
#         print(statment_2)

# statment_1 = list (statment_1.split())
# print(statment_1)
# statment_2 = list (statment_2.split())
# print(statment_2)

# new_statment = list()

# for i in range (0, len(statment_1), 4):
#     if statment_1[i].isdigit and statment_2[i].isdigit:
#         new_statment.append(int(statment_1[i]) + int(statment_2[i]))

# with open ('HW_4_SUM.txt', 'w') as data:
#     data.write(f'{new_statment[0]}*x^2+{new_statment[1]}*x+{new_statment[2]} = 0')

