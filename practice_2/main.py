a = 10
b = 100
c = 5.5
d = 10.4
e = "Me"
f = "You"
g = True
h = False
i = None 
g = None

a = 10
b = 100 
c = a 
a = b
b = c 
print(f"a = {a}, b = {b}")
 
x = 3
y = 9 
One = 2*x+3*y 
Two = x**2+2*x*y+y**2 
Three = (2*x)/8-(13*y)/7
Four = y**(1/4*x-2*y)
Five = x % y 
Six = (y/x)**2
Seven = x>y  
Eight = (x**2)!= y 
print(Seven)

name = "milk"
price = 100 
print(f"{name} дорівнює {price} гривень")

x1 = 1
x2 = 2
x3 = 3
x4 = 4
zminna = ((x1>x3 )or (x2>x4) and not (x2 != x3) or (x1 == x4))
print(zminna)

height = int(input("Your height: "))
weight = int(input("Your weight: "))
bmi = weight/(height**2)
print(f"При вазі {weight} кг і рості {height} метрів Ваш BMI складає {bmi}")

r1 = 30
r2 = 36
area_p1 = 3.14*(r1**2)
area_p2 = 3.14*(r2**2)
diff = ((area_p2 - area_p1)/area_p1)
print(f"Друга піца на {diff:.2%} більша за першу")
