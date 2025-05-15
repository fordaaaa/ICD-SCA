import random

def spin_slots(symbols):
    return random.choices(symbols, k=3)

def payout(bet, symbols):
    payout_dict = {
        "A": 10,
        "B": 5,
        "C": 5,
        "D": 5,
        "E": 5,
        "F": 5,
        "1": 10,
        "2": 5,
        "3": 5,
        "4": 5,
        "5": 5,
        "6": 5
    }
    if symbols[0] == symbols[1] == symbols[2]:  # checking if the symbols are matching
        return bet * payout_dict.get(symbols[0], 0)  
    return 0  

def get_symbols():
    return ["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6"]