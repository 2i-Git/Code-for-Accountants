# Compund Interest Calculater
# Input: Starting Amount and Interest Rate and Years

def CompoundYear(startingAmount, interestRate, years):
	currentAmount = int(startingAmount)
	rate = 1 + (float(interestRate) / 100)

	for i in range(int(years)):
		newAmount = currentAmount * rate
		currentAmount = newAmount

		print("Total after " + str(i + 1) + " years: " + str(currentAmount))

	return currentAmount

input_startingAmount = input("Enter starting amount: £")
input_interestRate = input("Enter interest rate: ")
input_years = input("Enter number of years: ")

total = CompoundYear(input_startingAmount, input_interestRate, input_years)

print("Total after " + input_years + " years: £" + str(total))