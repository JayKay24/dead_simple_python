import random

def roll_dice(sides: int) -> int:
  return random.randint(1, sides)

def main():
  print("Roll for initiative...")
  max_val = 20
  player1 = roll_dice(max_val)
  player2 = roll_dice(max_val)
  
  if player1 >= player2:
    print(f"Player 1 goes first (rolled {player1}).")
  else:
    print(f"Player 2 goes first (rolled {player2}).")

if __name__ == "__main__":
  main()
