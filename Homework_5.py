# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'Сколько кАБВонфет конфет нужно взяаБвть взять первому игроку?'

# new_text = list(filter(lambda elem: not 'абв' in elem.lower(), text.split()))
# print(*new_text)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Вариант 1. Для двух игроков

# from random import randint

# count = 2021 
# min_step = 1
# max_step = 28
# player = randint(1,2) 
# while count > 0:
#     step = int(input(f'На столе {count} конфет. Игрок {player}, введите количество конфет от 1 до 28: '))
#     if min_step<=step<=max_step and step <= count:
#         count -=step
#         if count > 0:
#             if player == 1:
#                 player = 2
#             else:
#                 player = 1
#     else:
#         print('Вы ввеели некорректное количество конфет. Попробуйте снова.')
# print(f'Последним взял конфеты игрок {player}. Поздравляю, Вы победили!')

# Вариант 2. Для одного игрока и бота

# from random import randint

# def win_strategy (curr_player, curr_count, min_s = 1, max_s = 28):
#     while curr_count > 0:
#         if curr_player == 1:
#             step = int(input(f'На столе {curr_count} конфет. Игрок, введите количество конфет от 1 до 28: '))
#         else:
#             step = 29-step
#             if step > curr_count:
#                 step = randint(1,curr_count)
#             print(f'Ваш противник взял {step} конфет.')
#         if min_s<=step<=max_s and step <= curr_count:
#             curr_count -=step
#         if curr_count > 0:
#             if curr_player == 1:
#                 curr_player = 2
#             else:
#                 curr_player = 1
#         else:
#             print('Вы ввели некорректное количество конфет. Попробуйте снова.')
#     return player

# count = 2021
# min_step = 1
# max_step = 28
# player = randint(1,2)
# if player == 1:
#     step = int(input(f'Вы делаете первый ход. Введите количество конфет от 1 до 28: '))
#     count -= step
#     player = 2
# else:
#     print('Ваш противник ходит первым. Он взял 20 конфет.')
#     count -= 20
#     player = 1
# if count > 2001:
#     if player == 1:
#         win_strategy(player, count)
#     else:
#         step = 29-step
#         print(f'Ваш противник взял {step} конфет.')
#         count -= step
#         player = 1
#         win_strategy(player, count)
# else:
#     while count > 0:
#         if player == 1:
#             step = int(input(f'На столе {count} конфет. Игрок, введите количество конфет от 1 до 28: '))
#         else:
#             step = randint(min_step,max_step)
#             if step > count:
#                 step = randint(1,count)
#             print(f'Ваш противник взял {step} конфет.')
#         if min_step<=step<=max_step and step <= count:
#             count -=step
#             if count > 0:
#                 if player == 1:
#                     player = 2
#                 else:
#                     player = 1
#         else:
#             print('Вы ввели некорректное количество конфет. Попробуйте снова.')
# if player == 1:
#     print('Игрок, поздравляю, вы победили!')
# else:
#     print('Увы! Победил ваш противник!')

# 3.  Создайте программу для игры в ""Крестики-нолики"".

# def show_field (matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             print(field[i][j],end=' ')
#         print()

# def make_step (player, matrix):
#     index = int(input(f'Выберите номер клетки, в которую хотите поставить {player}:'))
#     flag = True
#     while flag:
#         for i in range(len(matrix)):
#             for j in range(len(matrix)):
#                 if index == matrix[i][j]:
#                     matrix[i][j] = player
#                     flag = False
#                     break
#     return player, matrix

# def checking (matrix, curr_count):
#     if matrix[0][0] == matrix[0][1] == matrix[0][2] or matrix[1][0] == matrix[1][1] == matrix[1][2] or matrix[2][0] == matrix[2][1] == matrix[2][2] or matrix[0][0] == matrix[0][1] == matrix[0][2] or matrix[0][1] == matrix[1][1] == matrix[2][1] or matrix[2][0] == matrix[2][1] == matrix[2][2] or matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[0][2]:
#         curr_count = 0
#     else:
#         curr_count -= 1
#     return curr_count

# field = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

# flag = True
# while flag:
#     symbol = input('Выберите X или 0 для начала игры: ').lower()
#     if symbol == 'x' or symbol == '0':
#         flag = False
#     else:
#         print('Некорректный ввод. Попробуйте еще раз.')

# count = 9
# while count > 0:
#     if symbol == 'x':
#         show_field(field)
#         make_step(symbol, field)
#         count = checking(field,count)
#         symbol = '0'
#     else:
#         show_field(field)
#         make_step(symbol, field)
#         count = checking(field,count)
#         symbol = 'x'
# print('Игра окончена.')
# show_field (field)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open ('HW5_orig.txt','r') as data: # Взятие входных данных из файла и формирование списка
#     for line in data:
#         text = line
# text = [i for i in text]

# count = 1
# new_text = list()
# for i in range(1,len(text)): # Сжатие данных
#     if text[i] == text [i-1]:
#         count +=1
#     else:
#         new_text.append(count)
#         new_text.append(text[i-1])
#         count = 1
# else:
#     new_text.append(count)
#     new_text.append(text[i-1])

# new_text = ' '.join(str(i) for i in new_text) # Преобразование сжатых данных в строку

# with open ('HW5_changed.txt', 'w') as data: # Запись сжатых данных в файл
#     data.write(new_text)

# with open ('HW5_changed.txt', 'r') as data: # Открытие файла с сжатыми данными и создание списка
#     for line in data:
#         text_compress = list(line.split())
    
# for i in range (len(text_compress)): # Преобразование эелементов-чисел в тип integer
#     if text_compress[i].isdigit():
#         text_compress[i] = int(text_compress[i])

# text_origin = '' # Восстановление оригинального текста
# for i in range(0,len(text_compress),2):
#     text_origin += text_compress[i+1]*text_compress[i]

# with open ('HW5_changed.txt', 'a') as data: # Запись восстановленного текста в файл
#     data.write('\n' + text_origin)


