class Bucket:
    def __init__(self):
        self.price = 0
        self.items = {}

    def add_item(self, item, amount):
        self.price += amount * products[item]
        self.items.update({item: amount})

    def remove_item(self, item, amount):
        if amount < self.items[item]:
            self.price -= amount * products[item]
        else:
            del self.items[item]

        self.items[item] = self.items[item] - amount

    def current_items(self):
        return self.items

    def calculate_total(self):
        return self.price


products = {"water": 1, "butter": 2, "oil": 3, "bread": 4}

bucket = Bucket()

bucket.add_item("water", 3)
bucket.add_item("oil", 2)
bucket.add_item("butter", 4)

bucket.remove_item("butter", 2)

print(bucket.current_items())
print(bucket.calculate_total())
