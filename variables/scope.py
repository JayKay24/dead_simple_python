high_score = 10
spam = True

def order():
  eggs = 12

  def cook():
    nonlocal eggs

    if spam:
      print("Spam!")
    
    if eggs:
      eggs -= 1
      print("...and eggs.")
  
  cook()

def score():
  global high_score
  new_score = 465
  if new_score > high_score:
    high_score = new_score

def main():
  # score()
  # print(high_score)
  order()

if __name__ == "__main__":
  main()
