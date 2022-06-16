vvod=""
mas=[]
buff=0
num=0
digit=0

while vvod!="exit":
    print("Введите команду:",end="\t")
    vvod=str(input())
    if "push" in vvod:
        for i in range (len(vvod)-1,4,-1):
            digit=int(vvod[i])
            buff+=(digit*(10**num))
            num+=1
        mas.append(buff)
        num=0
        buff=0
    if "pop" in vvod:
        if len(mas)>0:
            print(mas[len(mas)-1])
            mas.pop(len(mas)-1)
        else:
            print("error")
    if "back" in vvod:
        if len(mas)>0:
            print(mas[len(mas)-1])
        else:
            print("error")
    if "size" in vvod:
        print(len(mas))
    if "clear" in vvod:
        mas.clear()
        print("ok")

print("bye")
