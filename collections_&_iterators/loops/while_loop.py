def main():
  number = None

  while number is None:
    try:
      number = int(input("Enter a number: "))
    except ValueError:
      print("You must enter a number.")

  print(f"You entered {number}")

if __name__ == "__main__":
  main()
