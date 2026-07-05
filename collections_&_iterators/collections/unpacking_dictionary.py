def main():
  menu = {"drip": 1.95, "cappuccino": 2.95, "americano": 2.49}
  # a, b, c = menu # default unpacks keys
  # a, b, c = menu.values()
  (a_name, a_price), (b_name, b_price), *_ = menu.items()
  print(a_name)
  print(b_name)
  print(b_price)
  print(menu.items())

if __name__ == "__main__":
  main()