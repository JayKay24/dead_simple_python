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
      display_matrix(matrix_3, i, j)
    print()

def display_matrix(matrix: list[list[int]], i: int, j: int) -> None:
  print(f"{str(matrix[i][j]):~<5s}", end="")

def display_superheroes(r=2, c=2):
  lst: list[list[str]] = [[""] * 2 for i in range(2)]
  m = len(lst)
  n = len(lst[0])

  for i in range(m):
    for j in range(n):
      lst[i][j] = input("Enter the name of a superhero: ")
  print(lst)

def matrix_multiplication(matrix_1: list[list[int]], matrix_2: list[list[int]]) -> list[list[int]]:
  row1 = len(matrix_1)
  col1 = len(matrix_1[0])
  row2 = len(matrix_2)
  col2 = len(matrix_2[0])
  matrix_3 = [[0] * col2 for i in range(row1)]

  for i in range(row1):
    for j in range(col2):
      for k in range(col1):
        matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j]
  
  print("The resultant matrix 3 is: ")
  for i in range(row1):
    for j in range(col2):
      display_matrix(matrix_3, i, j)
    print()

def main():
  # display_superheroes()
  # mat1 = [ 
  #   [1,2,8,4], 
  #   [5,6,7,8], 
  #   [3,2,1,4] 
  # ]
  # mat2 = [ 
  #   [2,5,4,2], 
  #   [1,5,2,6], 
  #   [9,4,7,2] 
  # ]
  # matrix_addition(mat1, mat2)
  mat1 = [ [2,1,4,3], [5,2,7,1], [3,1,4,2] ]

  mat2 = [ [1,2], [3,4], [2,5], [6,2] ]
  matrix_multiplication(mat1, mat2)

if __name__ == "__main__":
  main()