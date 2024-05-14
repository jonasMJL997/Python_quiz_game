print("welcome to my computer quiz !")

playing = input("do you wanna play?")

if playing != "yes":
    quit()

print("okay let's play ")
score = 0
answer = input("what does UI stand for? ")
if answer == "user interface":
    print("correct well done !")
    score += 1
else:
    print("incorrect")

answer = input("what does UX stand for? ")
if answer == "user experience":
    print("correct well done !")
    score += 1
else:
    print("incorrect")

answer = input("what does B2B stand for? ")
if answer == "user business to business":
    print("correct well done !")
    score += 1
else:
    print("incorrect")

answer = input("what does B2C stand for? ")
if answer == "user business to customers":
    print("correct well done !")
    score += 1
else:
    print("incorrect")

print("you got" + str(score) + " questions correct !" )
print("you got" + str((score / 4) * 100) + "%,")

if score == + 2:
    print("congratulation")

else:
    print("try again do you want?")

if playing != "yes":
    quit()
