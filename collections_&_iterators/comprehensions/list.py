def main():
  print(demarcate("cities"))
  cities = ["belmont", "new york", "paris", "buenos aires"]
  print([city[:3] for city in cities])
  print([city.title() for city in cities])
  print([(city, len(city)) for city in cities])
  print([[city, len(city)] for city in cities])

  print(demarcate("sublists"))
  parent_list = [[1, 2, 11, 13], [12, 34, 56, 10], [13, 77, 89], [56, 78]]
  print([sum(sublist) for sublist in parent_list])
  print([max(sublist) for sublist in parent_list])

  print(demarcate("heights"))
  heights = [12, 45, 78, 77, 12, 14, 54]
  heights_cm = [ht * 2.54 for ht in heights]
  print(heights_cm)

  print(demarcate("weights"))
  weights = [2900, 3450, 6678, 2348, 800, 8999, 90]
  print([(wt // 1000, wt % 1000) for wt in weights])

  print(demarcate("cubes"))
  L_ints = [3, 5, 7, 1, 8, 9, 4]
  print([n ** 3 for n in L_ints if n % 2 == 0])

  print(demarcate("doubles"))
  L_pos_neg = [32, -51, 63, 11, 86, -9, 66, 88, 97]
  print([n * 2 for n in L_pos_neg if n > 0])

  print(demarcate("even & odd numbers"))
  print([n for n in L_pos_neg if n % 2 == 0]) # even
  print([n for n in L_pos_neg if n % 2 != 0])  # odd

  print(demarcate("palindromes"))
  words = ["apple", "civic", "board", "noon", "moon", "lamp", "madam"]
  print([word for word in words if is_palindrome(word)])

  print(demarcate("ternary"))
  print([n if n > 0 else 0 for n in L_pos_neg])
  print([n // 2 if n % 2 == 0 else n * 3 for n in L_pos_neg if n > 0])

  print(demarcate("nested lists"))
  L3 = [[] * 3 for n in range(3)]
  L4 = [[0] * 3 for n in range(4)]
  L3[0].append(9)
  L4[1].pop()
  print(L3)
  print(L4)

  print("matrices")
  rows = 3
  columns = 4
  print([[None] * columns for r in range(rows)])
  

def is_palindrome(word: str) -> bool:
  n = len(word)
  l = 0
  r = n - 1

  while l <= r:
    if word[l] != word[r]:
      return False
    l += 1
    r -= 1

  return True

def demarcate(d_title: str, repetitions=5) -> str:
  return f"{"-" * repetitions} ({d_title}) {"-" * repetitions}"

if __name__ == "__main__":
  main()
