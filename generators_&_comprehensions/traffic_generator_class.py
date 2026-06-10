from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycles', None]


class Traffic:
    def __iter__(self):
        return self

    def __next__(self):
        vehicle = choice(vehicles)
        if vehicle is None:
            raise StopIteration

        color = choice(colors)

        return f"{color} {vehicle}"


def pluralize(count, str):
    if (count == 1):
        return str
    return f"{str}s"


# merge into traffic
count = 0
for count, vehicle in enumerate(Traffic(), start=1):
    print(f"Wait for {vehicle}...")

print(f"Merged after {count} {pluralize(count=count, str='vehicle')}!")
