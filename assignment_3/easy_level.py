list_1 =[1,2,3,4,5,6,7,8,9,10,11] 
# Easy level (10 tasks):
    # 1. Filter by Condition: Extract numbers greater than X from a list.
a=[]
X = 9 # just an example
for i in list_1:
    if i > X:
        a.append(i)
    # 2. Average of Positive Numbers: Find the average of positive numbers.
b_list=[]
for i in list_1:
    if i >0: 
        b_list.append(i)
b = sum(b_list)/len(b_list)
    # 3. Maximum in Filtered List: Find the maximum of numbers less than X.
c = max(b_list)
    # 4. Aggregate Conditional Sum: Sum of numbers divisible by Y.
d_list=[]
y = 3  # just an example
for i in list_1: 
    if i % y == 0:
        d_list.append(i)
d = sum(d_list)
    # 5. List of Squares: Create a list of squares of each number.
e=[]
for i in list_1:
    i2 = i**2
    e.append(i2)
    # 6. Extract Positive Numbers: Create a new list with only positive numbers from a given list.
f=[]
for i in list_1:
    if i >0:
        f.append(i)
    # 7. Filter Strings by Prefix: Find all strings in a list that start with a specified prefix.
list_words = ["uncomfortable", "untouchable", "unforgetable", "curious"] # just an example
list_pre = []
for i in list_words:
    if i.startswith("un"):
        list_pre.append(i)
g = list_pre 
    # 8. Sum of First N Numbers: Calculate the sum of the first N numbers in a list.
N=5
h = 0 
# "m" - sum_of_list 
for i in range(N):  
# for i in range(n) or (n+1)???
    h += list_1[i]
    # 9. Find All Palindromes: Extract all palindrome strings from a list.
j = []
list_exampples = ["level", "world", "madam", "python", "racecar", "noon", "hello"] # just an example
for i in list_exampples:
    if i == i[::-1]: 
        j.append(i)
    # 10. Check Divisibility: From a list of numbers, create a new list of booleans where each
            #element indicates whether the corresponding number is divisible by a given divisor.
k = []
z = 5 # just an example
for i in list_1:
    if i%z == 0:
        k.append(True)
    else: 
        k.append(False)



# print("Easy-level:")
# print(f"Task1: {a}")
# print(f"Task2: {b}")
# print(f"Task3: {c}")
# print(f"Task4: {d}")
# print(f"Task5: {e}")
# print(f"Task6: {f}")
# print(f"Task7: {g}")
# print(f"Task8: {h}")
# print(f"Task9: {j}")
# print(f"Task10: {k}")

ls = [a,b,c,d,e,f,g,h,j,k]
print("Easy-level:")
for i, v in enumerate(ls):
    print(f"Task{i+1}: {v}")