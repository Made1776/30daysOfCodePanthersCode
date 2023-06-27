# Beat the Panther - Challenge #07
# Validate the email address.

import re

def validateEmailAddress(emailAddress):
  # Define regular expression for an email address
  regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{1,3}$"
  if re.match(regex, emailAddress):
    print("Valid email address!")
  else:
    print("Invalid email address!") 

# Tests
validateEmailAddress("mc@lovin01@epn.edu.ec")
validateEmailAddress("mc.lovin01@epn")
validateEmailAddress("mc.lovin01@epn.edu.ec")