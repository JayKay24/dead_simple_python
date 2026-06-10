from time import sleep

sleepy = (sleep(t) for t in [1, 2, 3, 4, 5])
print("Calling...")
next(sleepy)
print("Done!")