# ; ### Завдання 3
# ; Створити модуль taxes.py, який містить:

# ; * функцію calculate_vat(amount) — розрахунок ПДВ (20%)
# ; * функцію calculate_income_tax(amount) — розрахунок податку на дохід (18%)

# ; Використати модуль для обчислення податків з доходу 15 000 грн.


def calculate_vat(amount):
    b = 0.2*amount
    return b

def calculate_income_tax(amount):   
    a = amount*1.18
    return a 