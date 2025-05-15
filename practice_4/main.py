#1
nums = [3, 7, 2, 9, 5]
total = 0
i = 0
for num in nums:
  total+=num
  i += 1 
  
mid = total/i
print("Середнє арифметичне:",  mid)


#2
nums = [4, 7, 2, 4, 8, 9, 2, 10, 3, 8]
a = set(nums)
nums = list(a)
b = nums[::-2]
print(b)

#3
grades = [
    [90, 85, 88],
    [75, 80, 79],
    [95, 92, 96],
    [88, 85, 84]
]
b=[]
for raw in grades: 
  mid = sum(raw)/len(raw)
  b.append(mid)
a=max(b)
for index, mid_mark in enumerate(b):
  if mid_mark == a: 
    break
print(f"{grades[index]}, {index+1}:{mid_mark}")

#4
prices = {
    "apple": 12,
    "banana": 8,
    "milk": 25,
    "bread": 20
}
prices_2 = prices.values()
a = sum(prices_2)
print(a)


#5
people = {
    "Anna": "Kyiv",
    "Bohdan": "Lviv",
    "Oksana": "Kyiv",
    "Dmytro": "Odesa"
}

people_2 = {}
a = list(set(people.values()))
print(a)
for i in a:
  people_2[i]=[]
print(people_2)
for key,value in people.items():
  people_2[value].append(key)
print(people_2)



# name = people.keys()
# city = people.values()

#6