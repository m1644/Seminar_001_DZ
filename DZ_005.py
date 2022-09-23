# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

print('Введите координаты точки А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите координаты точки B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

from math import sqrt
print('Расстояние между точками A и B: ', round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2)) 
