import random

def roll_dice(*dice: tuple[int, ...]) -> tuple[int, ...]:
  return tuple(random.randint(1, d) for d in dice)

def roll_dice_recursive(*dice: tuple[int, ...]) -> tuple[int, ...]:
  if dice:
    roll = random.randint(1, dice[0])
    return (roll,) + roll_dice_recursive(*dice[1:])
  
  return ()

def roll_dice_keyword_only(*, sides=6, dice=1):
  return tuple(random.randint(1, sides) for _ in range(dice))

def roll_dice_positional_only(dice=1, sides=6, /):
  return tuple(random.randint(1, sides) for _ in range(dice))

def cup_of_dice():
  dice_cup = roll_dice_recursive(6, 6, 6, 6, 6)
  print(dice_cup)

  bunch_o_dice = roll_dice(20, 6, 8, 4)
  print(bunch_o_dice)

def players():
  print("Roll for initiative...")
  player1, player2 = roll_dice(4, 5)
  player3, *_ = roll_dice(20)
  print(f"Player 3 rolled {player3}")
  
  if player1 >= player2:
    print(f"Player 1 goes first (rolled {player1}).")
  else:
    print(f"Player 2 goes first (rolled {player2}).")

def main():
  # players()
  cup_of_dice()
  # try:
  #   # roll_dice_keyword_only(3, sides=2, dice=2)
  #   # roll_dice_positional_only(sides=4, dice=4)
  # except TypeError:
  #   # print("Only keyword arguments accepted")
  #   print("Only positional arguments accepted")
if __name__ == "__main__":
  main()
