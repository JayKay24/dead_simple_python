type MenuDict[K = str, V = int] = dict[K, V]

def checkout_EAFP(menu: MenuDict, order: str): # Easier to Ask for Forgiveness than Permission
  try:
    print(f"Your total is {menu[order]}")
  except KeyError:
    print("That item is not on the menu")

def checkout_LBYL(menu: MenuDict, order: str): # Look Before You Leap
  if order in menu:
    print(f"Your total is {menu[order]}")
  else:
    print("That item is not on the menu")

if __name__ == "__main__":
  menu = {"drip": 1.95, "cappuccino": 2.95, "americano": 2.49}
  checkout_EAFP(menu, "drip")
  checkout_EAFP(menu, "tea")
  checkout_LBYL(menu, "drip")
  checkout_LBYL(menu, "tea")