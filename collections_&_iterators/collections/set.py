raffle = {"James", "Denis", "Simon"}

raffle.add("Daniel")
raffle.add("Denis")
print(raffle)

raffle.discard("Simon")
print(raffle)

winner = raffle.pop()
print(winner)
print(raffle)