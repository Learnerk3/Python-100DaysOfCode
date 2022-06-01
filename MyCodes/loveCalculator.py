print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


fullName = (name1 + name2).lower()
wordOne = "TRUE"
wordTwo = "LOVE"

count1 = 0
count2 = 0
loveScore = ""

for i in wordOne.lower():
    count1 += fullName.count(i)
# print(count1)

for j in wordTwo.lower():
    count2 += fullName.count(j)
# print(count2)

loveScore = int(str(count1) + str(count2))
# print(loveScore)

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")




