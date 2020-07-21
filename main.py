def factorial(n):
  a = n
  while a>1:
    n = n*(n-1)
    a -= 1
  factorial_of_n = n
  print(factorial_of_n)

factorial(5)