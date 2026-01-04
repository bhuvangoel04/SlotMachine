import random
import time
import sys

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 100

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
} # multiplier for each symbol

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if symbol != column[line]: # mismatch
                break
        else:
            winnings += values[symbol] * bet 
            winning_lines.append(line + 1)

    return winnings, winning_lines
   
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            print(column[row], end=" | " if i < len(columns) - 1 else "")
        print() 
        
def deposit():
    while True:
        amount  = input("Enter deposit amount:")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET:
                break
            else:
                print(f"Deposit needs to be withing bet range {MIN_BET} - {MAX_BET} INR")
        else:
            print("Please enter a valid amount")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines (1-3).")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("Enter bet amount per line: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        totalBet = bet * lines
        if(totalBet > balance):
            print(f"You do not have enough balance to bet that amount. Your current balance is {balance} INR.")
        else:            
            break 
    print(f"You are betting {bet} INR on {lines} lines. Total bet is {totalBet} INR.")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_values)
    balance += winnings - totalBet
    if(winnings > 0):
        print(f"You won {winnings} INR. Updated Balance is {balance} INR. You got some luck this time, Wanna try again?")
    else:
        print(f"You lost. Updated Balance is {balance} INR. No worries , try again!")
    return balance

def main():
    print("Welcome to the Slot Machine!", end="", flush=True)
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()
    bar = ["▖", "▘", "▝", "▗"]
    print("Initializing ", end="", flush=True)
    for i in range(10):
        sys.stdout.write(bar[i % len(bar)])
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\b")
        
    print()
    balance = deposit()
    while True:
        print(f"Your current balance is {balance} INR.")
        balance = spin(balance)
        if balance <= 0:
            print("You have run out of balance! Game over.")
            break
        answer = input("Do you want to play again? (y/n): ")
        if answer.lower() != 'y':
            break
        else:
            print("You got this! Let's go again!")
            print("Need to add more money to your balance first.")
            balance = deposit()
        
    

main()
