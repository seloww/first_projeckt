print("Is it a triangle ??? ")

a = int(input("Give value for a: "))
b = int(input("Give value for b: "))
c = int(input("Give value for c: "))

if abs(b-c) < a and a < b+c:
    print("It can be triangle but u cant be a man")

else:
    print("it cant be triangle but u can be a man ")