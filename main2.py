#Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)
# Два варианта получилось

import os
os.system('CLS') #очистка экрана
n = int(input('Введите целое трехзначное число: '))
m = int(n)
if len(str(n))==3: #длина числа
   m1 = m % 10
   m2 = m % 100 // 10
   m3 = m // 100

   print(f'Сумма цифр трехзначного числа -> {m1 + m2 + m3}')
else:
   print("Число не является трехзначным ")


# import os 
# os.system('CLS') #очистка экрана
# n = int(input('Введите целое трехзначное число: '))
# if len(str(n))==3: #длина числа
#     print("Сумма цифр целого трехзначного числа равна: ",n//100 + n%100//10 + n%100%10) 
# else:
#     print("Число не является трехзначным ")
