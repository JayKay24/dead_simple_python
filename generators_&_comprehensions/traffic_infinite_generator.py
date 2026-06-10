from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle']

def traffic():
  while True:
    vehicle = choice(vehicles)
    color = choice(colors)

    try:
      yield f"{color} {vehicle}"
    except GeneratorExit:
      print("No more vehicles.")
      raise

def pluralize(count, str):
  if count == 1:
    return str
  
  return f"{str}s"

def car_wash(traffic, limit):
  count = 0
  for vehicle in traffic:
    print(f"Washing {vehicle}")
    count += 1
    if count >= limit:
      traffic.close()

queue = traffic()
car_wash(queue, 5)
