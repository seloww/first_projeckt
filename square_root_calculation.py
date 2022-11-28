print("SQUARE ROOT CALCULATION")
print("plz like this cuz i want this")

x = int(input("Enter an number:"))
a=0
b=x/2

while True:
    a=(b+x/b)/2
    if (b==a):
        break
    else:
        b=a

print(b)