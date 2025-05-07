from gamelogic import spin_slots, get_symbols
from inputhandler import display_spin, slots_result
from balancetracker import load_balance, save_balance

def balance_check(balance):
    if balance <= 0:
        print("You got kicked out of the casino!")
        return False
    return True

def main():
    balance_file = "balance.txt"
    balance = load_balance(balance_file) 
    bet = 5
    symbols = get_symbols()  # gamelogic.py symbols

    while True:
        if not balance_check(balance):
            break

        input("Press Enter to spin the slots...")
        symbols_spun = spin_slots(symbols)
        display_spin(symbols_spun)
        balance = slots_result(balance, bet, symbols_spun)

        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input, put 'yes' or 'no'.")

        if play_again != 'yes':
            break

    save_balance(balance_file, balance) 
    print("Thank you for playing! Your final balance is: $" + str(balance))

if __name__ == "__main__":
    main()