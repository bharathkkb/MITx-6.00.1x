s = 'azcbobobegghakl'
l=len(s)
count=0;
for i in range(0,l):
    while i<l+2:
        x=s[i:i+3]
        if x=='bob':
                count+=1
        break
                
        
print count