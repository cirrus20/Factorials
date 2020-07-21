def factorial(n):
  if n == 1:
    return 1
  return(n*factorial(n-1))


def main():
  n = int(input("Enter a number: "))
  factorial_of_n = factorial(n)
  print("The factorial is " + str(factorial_of_n)

if __name__ == "__name__":
  main()