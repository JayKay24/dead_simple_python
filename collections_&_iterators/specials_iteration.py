specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]

first_iterator = specials.__iter__()
second_iterator = specials.__iter__()
print(type(first_iterator))

item = first_iterator.__next__()
print(item)
item = first_iterator.__next__()
print(item)
item = second_iterator.__next__()
print(item)
item = first_iterator.__next__()
print(item)
item = first_iterator.__next__()
print(item)