from typing import Final
from Clean_Code_Python.functional_programming import is_even, doubled

numbers: Final = [1, 2, 3, 4, 5]
even_numbers: Final = filter(is_even, numbers)
print(list(map(doubled, even_numbers)))
