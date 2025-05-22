import random 
import matplotlib.pyplot as plt 

a = 10000
b = 100 
c=0
balans_history = []
iteractions = []

while a>=100 and c<=1000: 
    c += 1
    if random.randint(1,36) == random.randint(1,36):
        a = a+b*36
    else:
        a = a-b
    print(f"Баланс_гри_{c}: {a}") 
    balans_history.append(a)
    iteractions.append(c)
plt.plot(iteractions, balans_history)
plt.title("Баланс гравця під час гри")
plt.xlabel("Номер раунду")
plt.ylabel("Баланс (грн)")
plt.show()



    


