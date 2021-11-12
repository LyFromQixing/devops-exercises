def input_matrix(N, M):
  print()
  matrix = [[0 for i in range(M)] for i in range(N)]
  for i in range(N):
    for j in range(M):
      matrix[i][j] = int(input("Insert the value of A[" + str(i+1) + "][" + str(j+1) + "]: "))
  return matrix

def result_matrix(N, M):

  # Counting the total of positive numbers
  count = 0
  matrix = input_matrix(N, M)
  for i in range(N):
    for j in range(M):
      if matrix[i][j] > 0:
        count += 1
  if count > 0:
    print()
    print("There are " + str(count) + " positive numbers in matrix A.")
    
  # Showing the matrix
  for i in range(N):
    print()
    for j in range(M):
      print(matrix[i][j], end=" ")

N = int(input("Insert N: "))
M = int(input("Insert M: "))

result_matrix(N, M) 
