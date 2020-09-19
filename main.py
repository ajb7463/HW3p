def digit_sum(n):
  if n >= 1:
    return digit_sum(n // 10) + n%10
  else:
    return 0

def run():
  x = int(input("Enter an int: "))
  print(f"sum of digits {x} is {digit_sum(x)}.")

if __name__ == "__main__":
  run()