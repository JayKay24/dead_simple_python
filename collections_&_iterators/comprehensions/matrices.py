def main():
  matrix = [
    [1, 4, 8, 3],
    [2, 5, 6, 3],
    [7, 9, 5, 8],
  ]
  print(matrix[2]) # extract a row
  print([row[1] for row in matrix]) # extract column 2

if __name__ == "__main__":
  main()