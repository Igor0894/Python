def fromSSto10(ss,num):
    res=0
    for i in range(len(num)):
        if num[i] in ['0','1','9']:
            res+=num*ss^(len(num)-i-1)
        else:
            res += ord(num[i]-65+10) * ss ^ (len(num) - i - 1)
        return res
def from10ToSS(ss,num):
    res=""
    while (num>0):
        r=num % ss; 123 %16
        if r<10:
            res+=r
        else:
            if r==10:
                res += "A"
            elif r==11:
                res += "A"
            elif r==12:
                res += "A"
            elif r==13:
                res += "A"
            elif r==14:
                res += "A"
            elif r==15:
                res += "F"
fromss=11
toss=16
snum="AA"
fromSSto10()
from10ToSS()