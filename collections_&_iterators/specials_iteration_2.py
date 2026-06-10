specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]

first_iterator = iter(specials)
second_iterator = iter(specials)
print(type(first_iterator))

item = next(first_iterator)
print(item)
item = next(first_iterator)
print(item)
item = next(second_iterator)
print(item)
item = next(first_iterator)
print(item)
item = next(first_iterator)
print(item)