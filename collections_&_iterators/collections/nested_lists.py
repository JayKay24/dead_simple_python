def matrix_addition(matrix_1: list[list[int]], matrix_2: list[list[int]]):
  rows = len(matrix_1)
  cols = len(matrix_1[0])
  matrix_3 = [[None] * cols for r in range(rows)]

  # Addition of matrices
  for i in range(rows):
    for j in range(cols):
      matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
  
  print("The resultant matrix 3 is: ")
  for i in range(rows):
    for j in range(cols):
      print(f"{str(matrix_3[i][j]):~<5s}", end="")
    print()

def display_superheroes(r=2, c=2):
  lst: list[list[str]] = [[""] * 2 for i in range(2)]
  m = len(lst)
  n = len(lst[0])

  for i in range(m):
    for j in range(n):
      lst[i][j] = input("Enter the name of a superhero: ")
  print(lst)

def main():
  # display_superheroes()
  mat1 = [ 
    [1,2,8,4], 
    [5,6,7,8], 
    [3,2,1,4] 
  ]
  mat2 = [ 
    [2,5,4,2], 
    [1,5,2,6], 
    [9,4,7,2] 
  ]
  matrix_addition(mat1, mat2)

if __name__ == "__main__":
  main()