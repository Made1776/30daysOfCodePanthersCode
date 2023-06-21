def centimeters_to_inches(centimeters):
    inches = centimeters / 2.54
    return inches

def kilometers_to_miles(kilometers):
    miles = kilometers / 1.60934
    return miles

centimeters = 10
inches = centimeters_to_inches(centimeters)
print(f"{centimeters} centimeters is equal to {inches} inches.")

kilometers = 10
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles.")