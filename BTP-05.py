# Beat the Panther - Challenge #05
# Validate the hacked password.

def validatePassword(password):
  # Password has at least 8 characters?
  if len(password) < 8:
    return print("Invalid password!")
  # Password has at least one upper case
  # and lower case character?
  if password.islower() or password.isupper():
    return print("Invalid password!")
  # Password has at least one number?
  atLeastOneNumber = False
  for character in password:
    if character.isnumeric():
      atLeastOneNumber = True
    # Password must not have a white spaces
    if character.isspace():
      return print("Invalid password!")
  if not atLeastOneNumber:
    return print("Invalid password!")

  return print("Valid password!")

# Tests
validatePassword("hello")
validatePassword("hellohello")
validatePassword("Hellohello")
validatePassword("Hello he11o")
validatePassword("Hellohe11o")