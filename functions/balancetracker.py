import os

def load_balance(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            balance = file.read()
            return float(balance)
    return 100.0 

def save_balance(filename, balance):
    with open(filename, 'w') as file:
        file.write(str(balance))