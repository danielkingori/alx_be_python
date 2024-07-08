class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def stock_value(self):
        return self.price * self.quantity
      
itm1 = Product("sugar",10,100)
itm2 = Product("carrot",30,5)

print(f"the stock is {itm1.stock_value()}") 