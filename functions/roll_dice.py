import random

def roll_dice(*dice: tuple[int, ...]) -> tuple[int, ...]:
  return tuple(random.randint(1, d) for d in dice)

def roll_dice_recursive(sides=6, dice=1) -> tuple[int, ...]:
  def roll():
    return random.randint(1, sides)

  if dice < 1:
    return ()
  return (roll(),) + roll_dice_recursive(*dice[1:])
  
  return ()

def roll_dice_keyword_only(*, sides=6, dice=1):
  return tuple(random.randint(1, sides) for _ in range(dice))

def roll_dice_positional_only(dice=1, sides=6, /):
  return tuple(random.randint(1, sides) for _ in range(dice))

def make_dice_cup(sides=6, dice=5):
  def roll():
    return tuple(random.randint(1, sides) for _ in range(dice))
  
  return roll

def cup_of_dice():
  dice_cup = roll_dice_recursive(6, 6)
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
  roll_for_damage = make_dice_cup(sides=8, dice=5)
  damage = roll_for_damage()
  print(damage)
if __name__ == "__main__":
  main()
