def func(A, B):
  for i in range(A, B+1):
    f = (i**2) - (2*i) + 5
    result = print("f(" + str(i) + ") = " + str(f))
  return result

A = int(input("Insert A: "))
B = int(input("Insert B: "))
func(A, B)
