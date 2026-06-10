from itertools import product
from string import ascii_uppercase as alphabet


def gen_license_plates():
    for letters in product(alphabet, repeat=3):
        letters = "".join(letters)
        if letters == 'GOV':
            continue

        for numbers in range(1000):
            yield f'{letters} {numbers:03}'


registrations = {}


def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return plate
    return None


license_plates = gen_license_plates()

# Fast forward through several results for testing purposes
for _ in range(4441888):
    next(license_plates)

name = "James Kinyua"
my_plate = new_registration(name)
print(my_plate)
print(registrations[name])
