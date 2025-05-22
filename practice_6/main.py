#1
import geometry 
print(geometry.rectangle_area(5,5))

#2
import converter 
print(converter.uah_to_usd(1000, 39.5))
print(converter.usd_to_uah(25, 39.5))

#3
import taxes 
print(taxes.calculate_vat(10000))
print(taxes.calculate_income_tax(10000))

#4
import math
print(math.sqrt(121))
print(math.sin(math.pi/2))

#5
import random
b = random.randint(1,6)
a = random.randint(1,6)
c = a+b
print(f"Kubik_1: {b}")
print(f"Kubik_2: {a}")
print(f"Suma: {c}")

#6
import datetime
a = input("рррр-мм-дд:  ")
b = datetime.datetime.strptime(a, "%Y-%m-%d") 
td = datetime.datetime.now()
print(td)

#7 
# Зробити імітацію гри в рулетку:
# 1.Створити програму, яка моделює гру в рулетку. Початковий баланс гравця — 10 000 грн. На кожному кроці гравець ставить 100 грн на певний результат. Гра триває, доки:
# залишаються гроші (баланс ≥ 100 грн) або
# не перевищено 1000 ітерацій
# 2.Використати модуль random для моделювання виграшу або програшу на кожному кроці.
# 3.Вести облік балансу після кожної гри.
# 4.Після завершення гри побудувати графік балансу по кожній ітерації за допомогою matplotlib.
# Правила рулетк рулетки:
# Кожен раунд гравець ставить ставку на 1 з 37 клінтинок.
# Якщо гравець вгадав він отримує виграш у розмірі 36*ставка

