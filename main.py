print("""

 CALCULATOR

PRESS 1 TO ADDITION
PRESS 2 TO EXTRACTION
PRESS 3 TO MULTIPLICATION
PRESS 4 TO DIVISION

""")

islem = str(input("Choose process: "))

if islem == "1":
    sayi1 = int(input("Enter 1st number: "))
    sayi2 = int(input("Enter 2nd number: "))
    print("Conclusion:", sayi1 + sayi2)
elif islem == "2":
    sayi1 = int(input("Enter 1st number: "))
    sayi2 = int(input("Enter 2nd number: "))
    print("Conclusion:", sayi1 - sayi2)
elif islem == "3":
    sayi1 = int(input("Enter 1st number: "))
    sayi2 = int(input("Enter 2nd number: "))
    print("Conclusion:", sayi1 * sayi2)
elif islem == "4":
    sayi1 = int(input("Enter 1st number: "))
    sayi2 = int(input("Enter 2nd number: "))
    print("Conclusion:", sayi1/sayi2)
else:
    print("invalid transaction bro...")