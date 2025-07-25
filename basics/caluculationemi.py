principle =int(input("Enter principle amount: "))
rate = float(input("Enter interest rate: "))
time = int(input("Enter time in years: "))
emi = (principle * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)
i = emi-principle
print("The principle amount is:", principle)
print( "Intrest to be paid is:", int (i))
print("The EMI is:", int(emi))