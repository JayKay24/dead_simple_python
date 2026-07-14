import asyncio
from aioconsole import ainput

# The upper bound for the range of numbers to check
BOUND: int = 10 ** 6


def collatz(n: int) -> int:
    """
    Calculates the length of the Collatz sequence for a given number.
    
    The Collatz conjecture states that if you take any positive integer:
    - if it's even, divide it by 2
    - if it's odd, multiply it by 3 and add 1
    Eventually, you will always reach 1. This function counts how many steps it takes.
    """
    steps: int = 0
    while n > 1:
        if n % 2:
            n = n * 3 + 1
        else:
            # Use integer division since we are working with integers
            n //= 2
        steps += 1
    return steps


async def length_counter(target: int) -> int:
    """
    Asynchronously counts how many numbers between 2 and BOUND have a Collatz
    sequence of the specified target length.
    
    It yields control to the event loop using `await asyncio.sleep(0)` on each iteration,
    preventing this CPU-bound task from blocking other async operations.
    """
    count: int = 0
    for i in range(2, BOUND):
        if collatz(i) == target:
            count += 1
        # Yield control back to the event loop so other tasks can run
        await asyncio.sleep(0)
    return count


async def get_input(prompt: str) -> int:
    """
    Asynchronously prompts the user for input and validates that it is a positive integer.
    """
    while True:
        n_str: str = await ainput(prompt)
        try:
            n: int = int(n_str)
        except ValueError:
            print("Value must be an integer")
            continue
        if n <= 0:
            print("Value must be greater than zero")
        else:
            return n


async def main() -> None:
    """
    The main asynchronous entry point of the script.
    """
    print("Collatz Sequence Counter")
    target: int = await get_input("Collatz sequence length to search for: ")
    print(f"Search in range 1-{BOUND}")

    # Use asyncio.gather to concurrently wait for both the user's guess
    # and the result of the length_counter computation.
    guess, count = await asyncio.gather(
        get_input("How many times do you think it will appear? "),
        length_counter(target)
    )

    if guess == count:
        print("Exactly right! I'm amazed.")
    elif abs(guess - count) < 100:
        print(f"You're close! it was {count}.")
    else:
        print(f"Nope. It was {count}.")


if __name__ == "__main__":
    # Run the main async function using the asyncio event loop
    asyncio.run(main())
