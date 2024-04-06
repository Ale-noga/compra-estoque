from .Product import Product

class Stock(Product):
    def __init__(self, code, category, name, price, model, manufacturer):
        super().__init__(name, price, model, manufacturer)
        self.code = code
        self.category = category
        self.quantity = 0
        
    def get_code(self):
        return self.code
    
    def get_category(self):
        return self.category
    
    def get_quantity(self):
        return self.quantity
    
    def set_code(self, code):
        self.code = code
        
    def set_category(self, category):
        self.category = category
        
    def set_quantity(self, quantity):
        self.quantity = quantity