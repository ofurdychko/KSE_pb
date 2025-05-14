a = int(input(" "))
if (a%2) == 0:
  print("Парне")

  a = float(input(" "))
if a >= 90:
  print("відмінник")
if a >= 75 and a <= 89:
  print ("молодець")
else:
  print("старайся більше")

  a_tax = 0
for a in range(10,101,5):
  a_tax = 1.2*a
  print(f"ціна без ПДВ: {a}грн -> з ПДВ: {a_tax}грн")

  a1 = float(input(""))
a2 = float(input(""))
a3 = float(input(""))
if a3>a2 and a3>a1:
  print(f"{a3}")
elif a2>a3 and a2>a1:
  print(f"{a2}")
elif a1>a3 and a1>a2:
  print(f"{a1}")

  a = 0
for i in range(1000,5001,300):
  a += 1
  print(f"місяць{a}: {i}")

  year = int(input(""))
if (year%4 == 0) and not (year%100 == 0 or year%400 == 0):
  print("Високосний")
else:
  print("Звичайний рік")

  a=1
while a < 20:
  a += 1
  if a%4 != 0:
    print(a)
  else: 
    continue
  
  a=10000
c=0
while a > 0:
  c+=1
  print(f"місяць{c}, залишок: {a} ")
  a = a-1200
  a = 1.02*a

  b=0
while True:
  a = float(input("Введіть ваш місячний дохід або '0' для виходу:  "))
  if a > 0:
    b += a
    print(f"Ваш дохід збережено:{b}")
  elif a == 0:
    print(" ")
    break
  else:
    print("Дохід не може бути від’ємним")
    continue