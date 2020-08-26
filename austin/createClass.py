class Light:
    def __init__(self,type,price):
        self.type = type
        self.price = price
    def __repr__(self):
        return self.type + ' $' + str(self.price)
light1 = Light("LED", 1.99)
print(light1)