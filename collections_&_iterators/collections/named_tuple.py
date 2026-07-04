from collections import namedtuple

CoffeeOrder = namedtuple("CoffeeOrder", ("item", "addons", "to_go"))

order = CoffeeOrder("pumpkin spice latte", ("whipped cream",), True)

print(order.item)
print(order[2])