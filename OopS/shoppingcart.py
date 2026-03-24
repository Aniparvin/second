class ShoppingCartIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        # Return a new iterator each time iteration starts
        return ShoppingCartIterator(self.items)
cart = ShoppingCart()
cart.items.extend(("Apple", "Banana", "Orange", "grape", "kiwi"))

for item in cart:
    print(item)

