class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"name: {self.name}, deposit: {self.deposit}, loan: {self.loan}"


class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "To be sold"

    def __str__(self):
        return f"ID: {self.ID}, price: {self.price}, owner: {self.owner.name}, status: {self.status}"

    def sell(self, customer, loan=0):
        if loan == 0:
            self.owner.deposit += self.price
            self.owner = customer
            self.status = "sold"
            print(f"The house with ID {self.ID} has been sold to {customer.name}.")
        else:
            self.owner = customer
            self.status = "sold with a loan"
            customer.loan += loan
            print(f"The house with ID {self.ID} has been sold to {customer.name} with a loan of {loan}.")


owner = Person("Owner")
customer = Person("customer")
house = House("019011728", 500000, owner)

print(owner)
print(customer)
print(house)

print("")

print("sold")
house.sell(customer)
print(owner)
print(customer)
print(house)

print("")

print("sold on loan:")
house.sell(customer, loan=200000)
print(owner)
print(customer)
print(house)
