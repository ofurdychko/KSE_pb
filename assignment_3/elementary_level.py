list_1=[1,2,3,4,5,6,7,8,9,10,11]
# Elementary level (5 tasks):
    # 1. Sum of Numbers: Calculate the sum of numbers in a list.
a = sum(list_1)
    # 2. Find Minimum: Determine the smallest number in a list.
b = min(list_1) 
    # 3. List Reversal: Reverse the elements in a list.
c = list_1[::-1]
    # 4. Print Odd Numbers: Display all odd numbers from a list.
d=[]
for i in list_1: 
    if i % 2 != 0: 
        d.append(i)
    # 5. Multiply List: Multiply each element in a list by a given number.
e = []
x = 3  # just an example
for i in list_1: 
    e.append(x*i)


ls = [a,b,c,d,e]
print("Elementary-level:")
for i, v in enumerate(ls):
    print(f"Task{i+1}: {v}")


