specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]

print(specials[1])

drink = specials.pop(1)
print(drink)
print(specials)

specials.append("cold brew")
print(specials)

specials.insert(1, "americano")
print(specials)