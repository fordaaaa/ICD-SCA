from gamelogic import payout
import time

def display_spin(symbols):
    print("Rolling. . .")
    time.sleep(1)
    print("Still Rolling. . .")
    time.sleep(1)
    print("You rolled: " + " | ".join(symbols) + "!\n")

def slots_result(balance, bet, symbols):
    winnings = payout(bet, symbols)
    if winnings > 0:
        print(f"Wow! You won ${winnings}!")
        balance += winnings
    else:
        print("Sorry, you lost.")
        balance -= bet

    print(f"Your current balance is: ${balance}")
    return balance