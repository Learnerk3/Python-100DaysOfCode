from tokenize import Double


print("Welcome to the tip Calculator.")
totalBillPayment = float(input("What was the total bill? $"))
toSplit = int(input("How many people to split the bill? "))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tipAmount = (totalBillPayment * tipPercentage) / 100
finalBillToPay = "{:.2f}".format((totalBillPayment + tipAmount) / toSplit)
print(f"Each person should pay: ${finalBillToPay}")
print(f"Each person should pay tip: ${'{:.2f}'.format(tipAmount)}")
