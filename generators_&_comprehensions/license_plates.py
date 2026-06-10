from itertools import product
from string import ascii_uppercase as alphabet

license_plates = (
    f'{letters} {numbers:03}'
    for letters in (
        "".join(chars)
        for chars in product(alphabet, repeat=3)
    )
    if letters != 'GOV'
    for numbers in range(1000)
)

registrations = {}


def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return True
    return False


# Fast-forward through several results for testing purposes.
for _ in range(4441888):
    next(license_plates)

name = "James K Njuguna"
my_plate = new_registration(name)
print(registrations[name])
