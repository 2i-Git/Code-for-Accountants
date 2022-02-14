# Compund Interest Calculater
# Input: Starting Amount and Interest Rate
# Input: Either Years or Target Amount

def CompoundYear(startingAmount, interestRate, years):
	currentAmount = int(startingAmount)
	rate = 1 + (float(interestRate) / 100)

	for i in range(int(years)):
		newAmount = currentAmount * rate
		currentAmount = newAmount

	return currentAmount

def CompoundTarget(startingAmount, interestRate, targetAmount):
	currentAmount = int(startingAmount)
	rate = 1 + (float(interestRate) / 100)
	years = 0

	while currentAmount < int(targetAmount):
		newAmount = currentAmount * rate
		currentAmount = newAmount

		years += 1

	return years

input_choice = input("Choose either (y)ears or (t)garet amount: ")

input_startingAmount = input("Enter starting amount: £")
input_interestRate = input("Enter interest rate: ")

if (input_choice == "y"):
	input_years = input("Enter number of years: ")
	total = CompoundYear(input_startingAmount, input_interestRate, input_years)
	print("Total after " + input_years + " years: £" + str(total))

if (input_choice == "t"):
	input_targetAmount = input("Enter target amount: £")
	years = CompoundTarget(input_startingAmount, input_interestRate, input_targetAmount)
	print("Would reach £" + input_targetAmount + " after " + str(years) + " years")