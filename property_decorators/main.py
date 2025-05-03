class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Invalid price! Must be non-negative.")

    @price.deleter
    def price(self):
        print("Price deleted")
        del self._price

# Example usage:
p = Product(100)
print("Initial price:", p.price)

p.price = 150
print("Updated price:", p.price)

del p.price
