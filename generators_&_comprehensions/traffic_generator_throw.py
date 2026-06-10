from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle']

def traffic():
  while True:
    vehicle = choice(vehicles)
    color = choice(colors)

    try:
      yield f"{color} {vehicle}"
    except ValueError:
      print(f"Skipping {color} {vehicle}...")
      continue
    except GeneratorExit:
      print("No more vehicles.")
      raise

def wash_vehicle(vehicle):
  if 'semi' in vehicle:
    raise ValueError("Cannot wash vehicle.")
  print(f"Washing {vehicle}")

def pluralize(count, str):
  if count == 1:
    return str
  
  return f"{str}s"

def car_wash(traffic, limit):
  count = 0
  for vehicle in traffic:
    try:
      wash_vehicle(vehicle)
    except Exception as e:
      traffic.throw(e)
    else:
      count += 1
    if count >= limit:
      traffic.close()

queue = traffic()
car_wash(queue, 5)
