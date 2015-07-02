

balance =320000

annualInterestRate = 0.2
minp=0
init=balance
while(balance>0):
	minp=minp+10
	balance=init
	for i in range(1,13):
		balance=balance-minp
		intrst=balance*(annualInterestRate/12)
		balance=balance+intrst
	
	

print minp


	
	

