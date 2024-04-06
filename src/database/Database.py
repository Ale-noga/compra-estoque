from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self):
        self.stock_list = []
        
    def print_stock(self):
        if len(self.stock_list) == 0:
            print("\n----------------EMPTY STOCK----------------")
        for stock in self.stock_list:
            print(
                "\n------------\nPRODUCT: " + str(stock.get_name()) + " - " + str(stock.get_model()) +
                "\nMANUFACTURER: " + str(stock.get_manufacturer().get_brand()) +
                "\nCODE: " + str(stock.get_code()) + 
                "\nQTD: " + str(stock.get_quantity()) + 
                "\n------------"
            )
    
    def print_product(self, code):
        product = self.get_product(code)
        return (
            "Name: " + str(product.get_name()) + " - " + str(product.get_model()) + 
            ", Manufacturer: " + str(product.get_manufacturer().get_brand()) + 
            ", Price: " + str(product.get_price()) + 
            ", Quantity: " + str(product.get_quantity())
        )
        
    def get_product(self, code):
        for stock in self.stock_list:
            if stock.get_code() == code:
                return stock
        return None
    
    @abstractmethod
    def add_stock(self, stock):
        pass
    
    @abstractmethod
    def remove_stock(self, units, stock):
        pass
    
    def quantity_per_product(self, code):
        for stock in self.stock_list:
            if stock.get_code() == code:
                return stock.get_quantity()
        return 0
    
    def get_stock_list(self):
        return self.stock_list
    
    def set_stock_list(self, stock_list):
        self.stock_list = stock_list        