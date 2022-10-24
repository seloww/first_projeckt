print (" WELCOME TO FACTORIAL ")

number = int(input(" Enter a number for factorial: "))
conc=1
for i in range(number-1):
    conc= conc*number
    number = number - 1

print(conc)