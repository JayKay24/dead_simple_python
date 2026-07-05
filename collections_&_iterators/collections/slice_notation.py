def main():
  orders = [
    "caramel macchiato",
    "drip",
    "pumpkin spice latte",
    "drip",
    "cappuccino",
    "americano",
    "mocha latte",
  ]
  print(orders[-1])

  three_four_five = orders[3:6]
  print(three_four_five)

  after_third = orders[4:]
  print(after_third)

  next_two = orders[:2]
  print(next_two)

  last_three = orders[-3:]
  print(last_three)

  last_two_but_not_last = orders[-3:-1]
  print(last_two_but_not_last)

  every_other = orders[1::2]
  print(every_other)

  reverse = orders[::-1]
  print(reverse)

  every_other_reverse = orders[-2::-2]
  print(every_other_reverse)

  three_to_five_reverse = orders[5:2:-1]
  print(three_to_five_reverse)

if __name__ == "__main__":
  main()