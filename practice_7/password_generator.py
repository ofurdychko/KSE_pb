def generate_password(length= 12, allow_symbols=False): 
    import random
    import string
    list_of_values = []
    if allow_symbols == False:
        list_of_values = string.ascii_letters + string.digits 
        return "".join(random.choices(list_of_values, k=length))
    else: 
        list_of_values = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choices(list_of_values, k=length))
 
# print(generate_password(length= 12, allow_symbols=False))