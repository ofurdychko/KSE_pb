# 1
a = input("Введи любий текст(in English):" )
dict_1 = {} 
ignore = [" ", "!", "?", "@", ".", ",", "-"]
# print(a)
for i in a: 
  if i in ignore: 
    continue 
  # print(i)
  if i in dict_1:
    dict_1[i] += 1
  else:
    dict_1[i] = 1 

print(dict_1)
  

# 2
n = int(input("Enter some number:" ))
def even_squares(n):
  res = []
  for i in range(n+1):
    if i%2 == 0:
      res.append(i**2)
  return res

print(even_squares(n))
 



#  3
one_to_ten = {} 

for i in range(1,11):
  list_1 = []
  for x in range(1,11):
    list_1.append(i*x)
  one_to_ten[i] = list_1 

print(one_to_ten)



# 4
list_1 = "Tokyo Seoul London Sofia Tokyo Sydney London".split(" ")
dict_1 = {}
for i in list_1: 
  if i in dict_1:
    dict_1[i] += 1
  else:
    dict_1[i] = 1 
print(dict_1) 
max_val = max(dict_1.values())
ls2 = []
for key,value in dict_1.items():
  if value == max_val:
    ls2.append(key)
print(ls2)
print(min(ls2))


# 5
s = float(input("Enter S - principal:" ))
r = float(input("Enter r - interest rate:" ))
n = int(input("Enter n - monthes:" ))
fin = s*(1+r)**n
print(fin)




# 6
expenses = {
    "Понеділок": 350,
    "Вівторок": 400,
    "Середа": 300,
    "Четвер": 500,
    "П’ятниця": 450,
    "Субота": 700,
    "Неділя": 600
}
a = expenses.values()
print(sum(a))

max_day = max(expenses.values())
print(max_day)

avg_day = sum(a)/len(a)
print(avg_day)


