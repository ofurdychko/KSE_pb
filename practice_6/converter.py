# Завдання 2
# Створити модуль converter.py, який містить дві функції:
# uah_to_usd(amount_uah, rate)
# usd_to_uah(amount_usd, rate)
# Використати ці функції у main.py, щоб конвертувати 1000 грн у долари при курсі 39,5 і навпаки.

def uah_to_usd(amount_uah, rate):
    a = amount_uah/rate 
    return a


def usd_to_uah(amount_usd, rate):
    b = amount_usd*rate
    return b