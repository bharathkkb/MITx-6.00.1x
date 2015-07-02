
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
tp=0
for i in range(1,13):
	minp=balance*monthlyPaymentRate
	tp=tp+minp
	balance=balance-minp
	intrst=balance*(annualInterestRate/12)
	balance=balance+intrst
	print("Month: "+str(i))
	print("Minimum monthly payment: "+str(round(minp,2)))
	print("Remaining balance: "+str(round(balance,2)))

print("Total paid: "+str(round(tp,2)))
print("Remaining balance: "+str(round(balance,2)))