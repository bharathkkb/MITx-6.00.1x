s = 'azcbobobegghakl'
l=len(s)
count=0;
for i in range(0,l):
    x=s[i]
    while x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        count+=1
        break
        
print count