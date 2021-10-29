class car:
    def __init__(self,brand,model,color,price):
        self.color = color
        self.brand = brand
        self.model = model
        self.price = price
    def is_expensive(self):
        if self.price > 2000:
            return True
        else:
            return False
