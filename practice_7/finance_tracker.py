transactions=[]
def add_transaction(transactions, amount, typee, category):  
    dict_transactions = {"a":amount, "b":typee, "c":category}
    return transactions.append(dict_transactions)

print(transactions)
    
def get_balance(transactions):
    balance = 0 
    for i in transactions:
        if i.get("b") == "дохід":
            balance += i.get("a")
        else:
            balance -= i.get("a")
    return balance 

add_transaction(transactions, 10000, "дохід", "зарплата")
add_transaction(transactions, 2500, "витрата", "їжа")
add_transaction(transactions, 1500, "витрата", "транспорт")

print(get_balance(transactions))

