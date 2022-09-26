import random
num=random.randint(0,200)
ans=int(input("Guess the numero"))
while (num!=ans):
    if (num<ans):
        print("decrease")
        answer=int(input("play again"))
    elif (num>ans):
        print("increase")
        answer = int(input("play again"))
print("tttrue")
