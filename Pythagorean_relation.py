print("Pythagorean says 'is it a right triangle?'")

a = int(input("Give value for long edge: "))
b = int(input("Give value for other edge: "))
c = int(input("Give value for last edge: "))

if a**2 + b**2 == c**2:
    print("Pythagorean said 'it is a right triangle'")
else:
    print("Pythagorean said 'it isnt a right triangle broe'")