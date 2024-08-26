class ShoppingCart:
    def __init__(self):
        self.cart={}

    def add_item(self ,name,price,Quantity):
        self.name=name
        self.price=price
        self.Quantity=Quantity

        if name in self.cart:
            self.cart[name]["quantity"]+=Quantity
        else:
            self.cart[name]={"price":price,"quantity":Quantity}


    def remove_item(self,name):
        if name in self.cart:
            del self.cart[name]
        else:
            print("not found") 

    def calculate_total(self):
        total_cost=0
        for item,keys in self.cart.items():
            total_cost+= keys["price"]*keys["quantity"]
        return total_cost

    def display_cart(self):
        for item,keyss in self.cart.items():
            print(f"{item}:{keyss["price"]}:{keyss["quantity"]}")

        print(f"total={self.calculate_total()}")  

    def __str__(self):
        return f"{self.name}:{self.cart[self.name]["price"]}:{self.cart[self.name]["quantity"]}"      


test=ShoppingCart()
test.add_item("sss", 1, 6)
test.add_item("aa", 2, 8)
test.display_cart()




               

