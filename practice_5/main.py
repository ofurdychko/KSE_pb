# 1
def calculate_vat(price):
  return 1.2 * price

print(calculate_vat(100))

# 2
def usd_to_uah(amount):
  print(amount * 39.5)

usd_to_uah(1000)

# 3
def monthly_salary(hours, rate):
  return hours*rate

print(monthly_salary(20, 0.5))

# 4
def apply_discount(price, discount):
  return price - price * discount/100

print(apply_discount(40000, 50))

# 5
def profit(revenue, cost, tax):
  return revenue - cost - (revenue - cost) * tax/100 
print(profit(100000,50000,20))

# 6
quantities = [2,3,4]
prices = [15,20,30]
def weighted_average_price(prices, quantities):
  total = 0 
  summa = sum(quantities)
  final = 0  
  for i, number in enumerate(quantities):
    total += prices[i] * quantities[i]
  final = total/summa
  return final

print(weighted_average_price(prices,quantities))


# 7
def calculate_wacc(e,d, re, rd, t):
  wacc = (e/(e+d))*re+(d/(d+e))*rd*(1-t/100)
  return wacc
print(calculate_wacc(100,100,10,10,50))


# 8
def monthly_payment(p, r, m):
  monthly_payment = p*((1-(1+r/100)**(-m)))/r
  return monthly_payment

print(monthly_payment(1000,5,12))





# 9
from itertools import count
def analyze_prices(prices):
  a=0
  count = 0 
  for i in prices:
    a+=i
  avg=a/len(prices)
  for j in prices:
    if j<avg:
      count+=1
  return min(prices), max(prices), avg, count
print(analyze_prices([100, 200, 300, 400]))
# input_data = input(" ")
# a = input_data.split(",")
# slited_data = []
# for i in a:
#   int(i)
#   append(splited_data)
# print(splited_data)

# 10
def adjust_for_inflation(income, inflation_rates):
  list_1 = []
  a = income
  for i in inflation_rates: 
    a = (i+1) * a
    list_1.append(a)
  return list_1 

print(adjust_for_inflation(10000, [0.08, 0.1, 0.07]))


# 11
dict = {}
dict["1"] = "a"
dict["2"] = "b"
dict["3"] = "c" 

print(dict)