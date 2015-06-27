s = 'wipluggkkiqhtvaygx'

s=s+"!" #marking end of input string with a low ascii value char

l=len(s)

def comps(a,b): # a function which return true if the two chars given are in alphebetical order or equal
	first=ord(a)
	second=ord(b)
	if(first < second or first == second):
		return True
	else:
		return False

beg=True
temp=""
flen=0
for i in range(0,l-1):
	one=s[i]
	two=s[i+1]
	ch=comps(one,two)
	if(beg==True & ch==True):
		temp=""
		beg=False
		temp=temp+one
		
	elif(ch==True):
		temp=temp+one

	else:
		temp=temp+one
		tlen=len(temp)
		if(tlen>flen):
			finl=temp
			flen=tlen
		temp=""

print "Longest substring in alphabetical order is: " + finl