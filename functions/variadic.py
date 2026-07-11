from collections.abc import Callable
def call_something_else(func: Callable, *args: int, **kwargs):
  return func(*args, **kwargs)

def say_hi(name: str) -> None:
  print(f"Hello, {name}!")

def main():
  call_something_else(say_hi, name="Bob")

if __name__ == "__main__":
  main()