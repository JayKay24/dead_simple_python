from interface_segragation import Worker, Human, Robot

class Manager:
  def assign_work(self, worker: Worker, duration: int, item: str) -> None:
    worker.work(duration, item)

def main():
  dave = Human("Dave")
  robot = Robot("i_9000")
  manager = Manager()

  manager.assign_work(dave, 5, "data aggregation")
  manager.assign_work(robot, 10, "car disassembly")

if __name__ == "__main__":
  main()
