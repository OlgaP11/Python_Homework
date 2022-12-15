# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

#num = int (input('Input number of the day: '))
#if 1 <= num <= 5:
#    print ('It is the weekday.')
#elif 6 <= num <= 7:
#    print ('It is the day off.')
#else:
#    print ('The week has 7 days. Try again.')

# 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#for x in [True,False]:
#    for y in [True,False]:
#        for z in [True,False]:
#            statement_1 = not (x or y or z)
#            statement_2 = not x and not y and not z
#            print('NOT',x,'OR',y,'OR',z,'=','NOT',x,'AND NOT',y,'AND NOT',z,'=>', statement_1 == statement_2)


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#num_1 = float(input('Input coordinate X which is not 0: '))
#num_2 = float(input('Input coordinate Y which is not 0: '))
#if num_1 == 0 or num_2 == 0:
#    print ("X and Y don't have to be 0.")
#elif num_1 > 0 and num_2 > 0:
#    print ('The point is in the quarter 1.')
#elif num_1 > 0 and num_2 < 0:
#    print ('The point is in the quarter 2.')
#elif num_1 < 0 and num_2 < 0:
#    print ('The point is in the quarter 3.')
#else:
#    print ('The point is in the quarter 4.')

# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

#quater = int (input ('Input number of quater: '))
#if quater == 1:
#    print (f'In quater {quater} x > 0 and y > 0')
#elif quater == 2:
#    print (f'In quater {quater} x > 0 and y < 0')
#elif quater == 3:
#    print (f'In quater {quater} x < 0 and y < 0')
#elif quater == 4:
#    print (f'In quater {quater} x < 0 and y > 0')
#else:
#    print ('There are only 4 quaters.')

# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

#a_x = float(input('Input coordinate X of point A:'))
#a_y = float(input('Input coordinate Y of point A:'))
#b_x = float(input('Input coordinate X of point B:'))
#b_y = float(input('Input coordinate Y of point B:'))
#distance = ((b_x-a_x)**2 + (b_y-a_y)**2)**0.5
#print (round(distance, 2))