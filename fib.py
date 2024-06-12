def fib(n):
  if n <= 2:
    return 1
  return fib(n-1) + fib(n-2)

if __name__ == "__main__":
  n = int(input("enter a number: "))
  f = fib(n)
  print(f"fib({n}) = {f}")
