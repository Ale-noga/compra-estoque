from ..classes.Manufacturer import Manufacturer
from ..classes.Stock import Stock
from ..database.service.Transactions import Transaction

def App():
    op = 0
    transactions = Transaction()
    
    print(" ___   ___        ___        ___  ___               ___               ___  ___   ___  ___             ")
    print("|   |=|_.'   .'|=|_.'   .'|=|_.' |   | |`.     .'| |   |   .'|   .'|=|_.' |   |=|_.' |   | |`.     .'|")
    print("`.  |      .'  |      .'  |  ___ |   | |  `. .'  | |   | .'  | .'  |      `.  |      |   | |  `. .'  |")
    print("  `.|=|`.  |   |      |   |=|_.' |   | |   | |   | |   | |   | |   |        `.|=|`.  |   | |   | |   |")
    print(" ___  |  `.`.  |  ___ |   |  ___ `.  | |   | |   | |  .' |   | `.  |  ___  ___  |  `.`.  | |   | |   |")
    print(" `._|=|___|  `.|=|_.' |___|=|_.'   `.|=|___| |___| |.'   |___|   `.|=|_.'  `._|=|___|  `.|=|___| |___|=|_.' 1.0.0\n\n")
    
    print("\t--------- SCE-UNICSUL 1.0.0 ---------")

    print("\nTYPE THE OPTION:")
    
    while op != 4:
        print("\n1 - NEW BUY | 2 - NEW SALE | 3 - OPEN DATABASE | 4 - EXIT")
        op = int(input())
        
        if op == 1:
            transactions = new_purchase(transactions)
        elif op == 2:
            new_sale(transactions)
        elif op == 3:
            print_transaction(transactions)
        elif op == 4:
            print("\nThank you for using SCE")
        else:
            print("\nInvalid option")
    

def new_purchase(transactions):
    p1 = Stock(0, None, None, 0, None, None)
    f1 = Manufacturer()
    
    print("Product name:")
    p1.set_name(input())
    
    print("Product price:")
    p1.set_price(float(input()))
    
    print("Product model:")
    p1.set_model(input())
    
    print("Product code:")
    p1.set_code(int(input()))
    
    print("Product quantity:")
    p1.set_quantity(int(input()))
    
    print("Product department:")
    f1.set_department(input())
    
    print("Product brand:")
    f1.set_brand(input())
    
    p1.set_manufacturer(f1)
    
    transactions.new_purchase(p1)
    
    return transactions

def print_transaction(transactions):
    transactions.print_stock()
    
def new_sale(transactions):
    print("\nSalesman:")
    seller = input()
    
    print("\nProduct code:")
    code = int(input())
    
    print("\nProduct: " + "\n" + str(transactions.print_product(code)))
    
    print("\nQuantity:")
    quantity = int(input())
    
    print("\nTotal purchase value: " + str(transactions.total_purchase_value(code, quantity)))
    
    print("\nPaying value:")
    value = float(input())
    
    transactions.transaction(quantity, value, seller, code)