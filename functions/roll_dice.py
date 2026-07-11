import random

def roll_dice(sides=6, dice=1) -> tuple[int, ...]:
  return tuple(random.randint(1, sides) for _ in range(dice))

def roll_dice_recursive(sides: int, dice: int) -> tuple[int, ...]:
  if dice < 1:
    return ()
  
  roll = random.randint(1, sides)
  return (roll,) + roll_dice_recursive(sides, dice - 1)

def main():
  print("Roll for initiative...")
  max_val = 20
  player1, player2 = roll_dice(sides=max_val, dice=2)
  player3, *_ = roll_dice(dice=5)
  print(f"Player 3 rolled {player3}")
  
  if player1 >= player2:
    print(f"Player 1 goes first (rolled {player1}).")
  else:
    print(f"Player 2 goes first (rolled {player2}).")

if __name__ == "__main__":
  main()
