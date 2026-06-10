from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

def traffic():
  while True:
    vehicle = choice(vehicles)

    if vehicle is None:
      return
    
    color = choice(colors)
    
    yield f"{color} {vehicle}"

def pluralize(count, str):
  if count == 1:
    return str
  
  return f"{str}s"

# merge into traffic
count = 0
for count, vehicle in enumerate(traffic(), start=1):
  print(f"Wait for {vehicle}")

print(f"Merged after {count} {pluralize(count=count, str='vehicle')}!")
