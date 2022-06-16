f=open('C:/test/text4.txt','r')
a=str(f.read())
f.close()
b=str()
b1=str()
max=0
max1=0

for i in range (len(a)-1):
    if a[i]!=a[i+1]:
        if max1==0:
            b1+=a[i]
            max1 += 1
        b1+=a[i+1]
        max1+=1
    else:
        if max1>=max:
            b=b1
            max=max1
        b1=""
        max1=0

print("Строка",b,",в которой",max," неповторяющихся символов")
