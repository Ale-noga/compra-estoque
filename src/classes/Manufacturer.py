class Manufacturer:
    def __init__(self):
        self.department = None
        self.brand = None

    def get_department(self):
        return self.department
    
    def get_brand(self):
        return self.brand
    
    def set_department(self, department):
        self.department = department
    
    def set_brand(self, brand):
        self.brand = brand