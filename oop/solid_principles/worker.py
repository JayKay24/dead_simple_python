from typing import Protocol

class Worker(Protocol):
  def work(self, duration: int) -> None:
    ...

class Sleeper(Protocol):
  def sleep(self, duration: int) -> None:
    ...

class Eater(Protocol):
  def eat(self, duration: int) -> None:
    ...

class HumanWorker(Eater, Sleeper, Worker, Protocol):
  ...

class RobotWorker(Worker, Protocol):
  ...

class Human(HumanWorker):
  def __init__(self, name: str) -> None:
    self.name = name

  def work(self, duration: int) -> None:
    print(f"{self.name} is working for the next {duration} hours...")

  def sleep(self, duration: int) -> None:
    print(f"{self.name} is sleeping for the next {duration} hours...")

  def eat(self, duration: int) -> None:
    print(f"{self.name} is eating for the next {duration} minutes...")

class Robot(RobotWorker):
  def __init__(self, name: str) -> None:
    self.name = name

  def work(self, duration: int) -> None:
    print(f"{self.name} is working for the next {duration} hours...")

def main():
  dave_worker = Human("Dave")
  i_worker = Robot("i_9000")
  dave_worker.eat(15)
  dave_worker.work(8)
  dave_worker.sleep(8)
  i_worker.work(20)

if __name__ == "__main__":
  main()

