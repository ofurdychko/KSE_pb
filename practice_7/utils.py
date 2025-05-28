def is_prime(n):
    for r in range(2,n):
        if n%r != 0:
            continue
        else:
            return False 
    return True

# print(is_prime(11))
