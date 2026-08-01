from typing import Protocol

class Worker(Protocol):
  """Interface for entities that can work."""
  def work(self, duration: int, item: str) -> None:
    """Perform work on the given item for the specified duration."""
    ...

class Sleeper(Protocol):
  """Interface for entities that can sleep."""
  def sleep(self, duration: int) -> None:
    ...

class Eater(Protocol):
  """Interface for entities that can eat."""
  def eat(self, duration: int) -> None:
    ...

class HumanWorker(Eater, Sleeper, Worker, Protocol):
  """Interface for a human worker who needs to eat, sleep, and work."""
  ...

class RobotWorker(Worker, Protocol):
  """Interface for a robot worker who only needs to work."""
  ...

class Human(HumanWorker):
  """
  A concrete Human class implementing the HumanWorker interface.
  Humans must implement eat, sleep, and work methods.
  """
  def __init__(self, name: str) -> None:
    self.name = name

  def work(self, duration: int, item: str) -> None:
    print(f"{self.name} is working on {item} for the next {duration} hours...")

  def sleep(self, duration: int) -> None:
    print(f"{self.name} is sleeping for the next {duration} hours...")

  def eat(self, duration: int) -> None:
    print(f"{self.name} is eating for the next {duration} minutes...")

class Robot(RobotWorker):
  """
  A concrete Robot class implementing the RobotWorker interface.
  Robots only need to implement the work method, adhering to the Interface Segregation Principle.
  """
  def __init__(self, name: str) -> None:
    self.name = name

  def work(self, duration: int, item: str) -> None:
    print(f"{self.name} is working on {item} for the next {duration} hours...")

def main():
  """
  Demonstrates the Interface Segregation Principle.
  Different workers only implement the interfaces they actually need.
  """
  dave_worker = Human("Dave")
  i_worker = Robot("i_9000")
  
  # A human worker performs all activities
  dave_worker.eat(15)
  dave_worker.work(8, "reports")
  dave_worker.sleep(8)
  
  # A robot worker only performs work
  i_worker.work(20, "car assembly")

if __name__ == "__main__":
  main()

