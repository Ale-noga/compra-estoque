from ..Database import Database

class Transaction(Database):    
    def add_stock(self, product):
        self.stock_list.append(product)
        
    def remove_stock(self, units, product):
        product.set_quantity(product.get_quantity() - units)
        
    def new_purchase(self, product):
        self.add_stock(product)
        print("----------------")
        print("PURCHASE MADE")
        print("Product name: " + str(product.get_name()) + 
            " - " + str(product.get_manufacturer().get_brand()) + 
            " - " +  str(product.get_model())
        )
        print("Product code: " + str(product.get_code()))
        print("----------------")
    
    def total_purchase_value(self, code, quantity):
        return self.get_product(code).get_price() * quantity
    
    def new_sale(self, units, value, seller, product):
        self.remove_stock(units, product)
        print("----------------")
        print("SALE MADE")
        print("Product name: " + str(product.get_name()))
        print("Total purchase: " + str(value))
        print("----------------")
        
    def unauthorized_sale(self, message):
        print("----------------")
        print("UNAUTHORIZED SALE")
        print("Message: " + message)
        print("----------------")
    
    def transaction(self, units, value, seller, code):
        if super().quantity_per_product(code) > 0 and super().quantity_per_product(code) >= units:
            product = super().get_product(code)
            if value >= (product.get_price() * units):
                self.new_sale(units, (product.get_price() * units), seller, super().get_product(code))
            else:
                self.unauthorized_sale("INSUFFICIENT BALANCE")
        else:
            self.unauthorized_sale("INSUFFICIENT STOCK")