def coke_cash():
    cokes_str = input("How many cokes would you like to buy? ")
    cokes_int = int(cokes_str)
    amount_due = cokes_int * 50
    
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin_str = input("Coin: ")
        coin_int = int(coin_str)
        amount_due = amount_due - coin_int
        
    change_owed = abs(amount_due)
    print(f"Change owed: {change_owed}")
    if change_owed > 0:
        print("Outputting change...")
        
    print("Thank you! have a nice day :)")

coke_cash()

