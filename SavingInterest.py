IntPercent = float(input("Interest Rate: (%) "))
Balance = int(input("Balance: "))
Months = int(input("How many months? "))

IntMoney = (Balance*Months)*(IntPercent/100/12)
Total = Balance + IntMoney
print("******************RESULT******************")
print("Total amount: ", Total)