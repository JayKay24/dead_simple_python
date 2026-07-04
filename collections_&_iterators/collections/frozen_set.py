raffle = {"Kyle", "Denis", "Jason"}
prev_winners = frozenset({"Denis", "Simon"})

raffle -= prev_winners
print(raffle)

winner = raffle.pop()
print(winner)
print(raffle)