menu: dict[str, int] = {"drip": 1.95, "cappuccino": 2.95}

print(menu)
print(menu["drip"])

menu["americano"] = 2.49
print(menu)

del menu["americano"]
print(menu)