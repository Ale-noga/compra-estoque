class Product():
    def __init__(self, name, price, model, manufacturer):
        self.name = name
        self.price = price
        self.model = model
        self.manufacturer = manufacturer
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_model(self):
        return self.model
    
    def get_manufacturer(self):
        return self.manufacturer
    
    def set_name(self, name):
        self.name = name
        
    def set_price(self, price):
        self.price = price
    
    def set_model(self, model):
        self.model = model
    
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
        