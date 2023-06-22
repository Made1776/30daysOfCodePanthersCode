# Beat the Panther - Challenge #03
# Find the (impossible) magic number.

def findMagicNumber(a, b):
  lowerLimit = a + 1 if a % 2 == 0 else a
  upperLimit = b - 1 if b % 2 == 0 else b
  # Magic number is odd
  for i in range(lowerLimit, upperLimit + 1, 2):
    mn = f"The magic number between {a:d} and {b:d} is {i:d}"
    nmn = f"There is no magic number between {a:d} and {b:d}"
    # Magic number is divisible by 3
    if i % 3 == 0:
      # Sum of magic number digits is 7
      summg = 0
      for digit in str(i):
        summg += int(digit)
      if summg == 7:
        return print(mn)
  return print(nmn)

# Test
a = 1
b = 10000000
findMagicNumber(a, b)