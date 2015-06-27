

balance =320000

annualInterestRate = 0.2
init=balance
minb=balance/12
maxb=(balance*(1+(annualInterestRate/12))**12)/12
minp=(minb+maxb)/2

def calcb(bal,air,minp): #this fuction return the remaining balance after a year
	for x in range(0,12):
		bal=bal-minp
		intrst=bal*(air/12)
		bal=bal+intrst
	return bal


while(abs(balance)>0):
	balance=init
	balance=calcb(balance,annualInterestRate,minp)
	balance=round(balance,2) #rounding so as to prevent some floating point errors
	
	if(balance>0):  #if the returning bal is less then we set the min bal value to min payment
		minb=minp
		minp=(minb+maxb)/2
	elif(balance<0): #if the returning bal is great then we set the max bal value to min payment
		maxb=minp
		minp=(minb+maxb)/2
	else: #if its not either we have arrived upon the right value
		break

print round(minp,2)



	
	

