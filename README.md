# Dead Simple Python Exercises

A collection of Python scripts, exercises, and examples exploring core Python concepts and idioms. This repository contains my progress as I work through the exercises and examples from the book [Dead Simple Python](https://a.co/d/01x3HC9t) by Jason C. McDonald. It serves as a learning space for mastering advanced Python features such as generators, asynchronous programming, custom iterators, decorators, bitwise operations, and type linting.

## Repository Structure

The project is organized into folders representing different Python topics:

*   **`asynchrony_&_concurrency/`**: Experiments in asynchronous programming using `asyncio` and `aioconsole`. Includes:
    *   [collatz_async.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/asynchrony_&_concurrency/collatz_async.py): An asynchronous implementation of the Collatz sequence length counter.
    *   [collatz_sync.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/asynchrony_&_concurrency/collatz_sync.py): The synchronous version of the Collatz sequence counter.
*   **`binary_&_serialization/`**: Code dealing with low-level representation of numbers and bitwise manipulation. Includes:
    *   [bitwise_shift.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/binary_&_serialization/bitwise_shift.py): Demonstration of bitwise shift operators.
    *   [negative_binary.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/binary_&_serialization/negative_binary.py): Looking at two's complement and negative binary operations.
    *   [print_integer.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/binary_&_serialization/print_integer.py): Octal, hex, and binary representation formatting.
*   **`collections_&_iterators/`**: Implementations of custom iterable classes, queue management, and iteration utilities. Includes:
    *   [cafequeue.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/collections_&_iterators/cafequeue.py): Custom double-ended queue system for a cafe.
    *   [specials_iteration.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/collections_&_iterators/specials_iteration.py): Implementations of custom iterators and iterables.
*   **`generators_&_comprehensions/`**: Infinite generators, coroutines, subgenerators (`yield from`), and list/dictionary comprehensions. Includes:
    *   [traffic_infinite_generator.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/generators_&_comprehensions/traffic_infinite_generator.py): Infinite generation of traffic elements using generator `.close()` and `.throw()` mechanics.
    *   [license_generator.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/generators_&_comprehensions/license_generator.py): Using standard library `itertools` to generate license plate sequences.
*   **Root Scripts**:
    *   [global_cordinates.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/global_cordinates.py): A class implementing geographic coordinates with custom magic methods (`__repr__`, `__str__`, `__eq__`, `__hash__`).
    *   [coffee_order_recipe.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/coffee_order_recipe.py): Modeling class methods, static methods, and custom decorators in Python.
    *   [text_adventure.py](file:///Users/jamesnjuguna/Downloads/books/personal_projects/Dead_Simple_Python/text_adventure.py): A text-based adventure script showcasing decorator wrappers (`functools.wraps`).

---

## Setup & Getting Started

### 1. Prerequisites
Ensure you have Python 3.13+ installed.

### 2. Activate the Virtual Environment
Activate the local virtual environment from the root directory:

```bash
source ./bin/activate
```

### 3. Install Dependencies
Install the required packages for linting, formatting, and async utilities:

```bash
pip install -r requirements.txt
```

---

## Quality Tools

This repository is configured with tooling to maintain clean, pep8-compliant code.

*   **Linting**: Run `flake8` to inspect the code for styling issues:
    ```bash
    flake8 .
    ```
*   **Formatting**: Format your code automatically using `autopep8`:
    ```bash
    autopep8 --in-place --recursive --exclude "bin,include,lib,lib64,share,venv,.venv,env,.env,.git,__pycache__" .
    ```
*   **Static Type Checking**: Check type annotations using `mypy`:
    ```bash
    mypy .
    ```
