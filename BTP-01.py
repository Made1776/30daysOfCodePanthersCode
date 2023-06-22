# Beat the Panther - Challenge #01
# Check the validity of a credit card
# number using the Luhn Algorithm.

# Returns 'True' if the 'cardNumber'
# string contains a valid credit number
# and 'False' otherwise
def isValid(cardNumber):
  # Store individual digits of the
  # card number string into a list
  n = len(cardNumber)
  digits = []
  for i in range(n):
    digits.append(int(cardNumber[i]))

  # Starting with the second digit 
  # from the right (of index 'n - 2'),
  # double every other digit on the list
  for i in range(n - 2, -1, -2):
    digits[i] *= 2
    # If doubling a digit results in a
    # two-digit number, add the digits,
    # to obtain a single digit, equivalent 
    # to subtracting 9 from the result
    if digits[i] >= 10:
      digits[i] -= 9

  # The 'cardNumber' is valid if the sum of
  # the resulting values on the list is 
  # divisible by 10 
  sum = 0
  for i in range(n):
    sum += digits[i]
  if sum % 10 == 0:
    return True
  else:
    return False

def test(cardNumber):
  if isValid(cardNumber):
    print('Credit card number IS valid.')
    print('Proceed, agent.')
  else:
    print('Credit card number IS NOT valid.')
    print('Abort, agent!')
