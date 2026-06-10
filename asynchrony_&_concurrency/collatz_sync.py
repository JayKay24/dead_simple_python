BOUND = 10 ** 6


def collatz(n):
    steps = 0
    while n > 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n /= 2
        steps += 1
    return steps


def length_counter(target):
    count = 0
    for i in range(2, BOUND):
        if collatz(i) == target:
            count += 1
    return count


def get_input(prompt):
    while True:
        n = input(prompt)
        try:
            n = int(n)
        except ValueError:
            print("Value must be an integer")
            continue
        if n <= 0:
            print("Value must be greater than zero")
        else:
            return n


def main():
    print("Collatz Sequence Counter")
    target = get_input("Collatz sequence length to search for: ")
    print(f"Search in range 1-{BOUND}")
    count = length_counter(target)
    guess = get_input("How many times do you think it will appear? ")

    if guess == count:
        print("Exactly right! I'm amazed.")
    elif abs(guess - count) < 100:
        print(f"You're close! it was {count}.")
    else:
        print(f"Nope. It was {count}.")


if __name__ == "__main__":
    main()
