def digit_sum(n):
  if n >= 1:
    return digit_sum(n // 10) + n%10
  else:
    return 0

def run():
  N = int(input("Enter an int: "))
  print(f"sum of digits {N} is {digit_sum(N)}.")

if __name__ == "__main__":
  run()