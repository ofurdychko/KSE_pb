list_1 = [1,2,3,4,5,6,7,8,9,10,11]
# Medium level (10 tasks):
    # 1. Filter by Multiple Conditions: Numbers divisible by X but not by Y.
a = []
x = 2 # just an example
y = 3 # just an example
for i in list_1:
    if (i%x == 0) and (i%y == 0):
        a.append(i)
    # 2. Nested List Flattening: Flatten a list of lists into a single list.
b = []
lists_in_list = [[1,2],[3,4],[5,6],[7,8],[9,10],[11]] # just an example
for i in lists_in_list:
    for i_2 in i:
        b.append(i_2)
    # 3. Complex String Manipulation: Extract and capitalize particular substrings.
string_list = ["apple pie", "orange juice", "banana split", "ice cream", "grape soda"] # just an example
c = []
for i in string_list: 
    splited = i.split()
    splited[0]=splited[0].upper()
    splited_together = ' '.join(splited)
    c.append(splited_together)
    # 4. Multi-level Sorting: Sort by descending, then by frequency.
d = [5, 5, 2, 9, 5, 7, 3, 9, 3, 1] # just an example
d.sort(reverse=True)
dict_d = {}
for i in d:
    if i in dict_d:
        dict_d[i] += 1
    else:
        dict_d[i] = 1
len_d = len(d)
for i in range(len_d):
    for i_2 in range(i + 1, len_d):
        freq_1 = d[i]
        freq_2 = d[i_2]
        if (dict_d[freq_2] > dict_d[freq_1]) or (dict_d[freq_2] == dict_d[freq_1] and freq_2 > freq_1):
            d[i], d[i_2] = d[i_2], d[i]
    # 5. Combine Lists Conditionally: Merge two lists based on conditions.
list_2 = [12,13,14,0,15,16]  # just an example
list_3 = [17,18,19,20,21,22,23] # just an example
e =  []
lists = [list_1,list_2,list_3]
for i in lists:
    if all(i_2>0 for i_2 in i):
         e += i
#   приклад ще однієї умови 
#   if len(i)>6:   
#       e += i
    # 6. Dictionary Aggregation: Sum values in a dictionary by key.
dict_list = [{"banana": 2},{"apple": 5},{"orange": 4},{"banana": 1},{"apple":4}] # just an example
f = {}
for i in dict_list:
    for key in i: 
        if key in f: 
            f[key] += i[key]
        else:
            f[key]= i[key]
    # 7. Conditional Element Replacement: Replace elements based on condition.
g = [1,2,3,4,5,6,7,8,9,10,11] # similar to list_1
for i in range(len(g)):
    if g[i]%3 == 0:
        g[i] = "лишнє"
    # 8. Count String Lengths: Count the number of strings with length greater than X.
list_str = ["apple", "banana", "orange"] # just an example
word_len = 5 # just an example
h = 0 
for i in list_str:
    if len(i) > word_len:
        h += 1 
    # 9. Concatenate Alternating: Merge strings alternately from two lists
list_word = ["num_1: ","mun_2: ","num_3: ","num_4: ","num_5: "] # just an example
list_num = [10,20,30,40,50] # just an example
j = []
for i in range(len(list_word)):
        j.append(list_word[i] + str(list_num[i]))
    # 10. Multiply If: Multiply numbers by Y if greater than X. 
k = []
x=5 # just an example
y=2 # just an example
for i in list_1:
    if i > x:
        k.append(i*y)


ls = [a,b,c,d,e,f,g,h,j,k] 
print("Medium-level:")
for i, v in enumerate(ls):
    print(f"Task{i+1}: {v}")