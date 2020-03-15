def backToStrConvert(y):
    op=''
    for i in y:
        op=op+str(i)
    
    return op

def nonRepeat(s):
    sNew=s[0]
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            sNew=sNew+'.'
        else:
            sNew=sNew+s[i]
    return sNew
