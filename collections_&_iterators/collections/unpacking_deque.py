from collections import deque

def main():
  customers = deque(["Kyle", "Simon", "James"])
  customers.append("Daniel")
  *_, second_to_last, last = customers
  print(second_to_last)
  print(last)

if __name__ == "__main__":
  main()