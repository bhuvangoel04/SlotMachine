def deposit():
    while True:
        amount  = input("Enter deposit amount:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 99:
                break
            else:
                print("Minimum deposit is 100 INR")
        else:
            print("Please enter a valid amount")
    return amount

def main();
    balance = deposit()
    
main()

