y=0
x=0
alive=0

# 12*12
a=[ [" ","  А","  Б","  В","  Г","  Д","  Е","  Ж","  З","  И","  К",""],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,3],
    [4,0,0,0,0,0,0,0,0,0,0,4],
    [5,0,0,0,0,0,0,0,0,0,0,5],
    [6,0,0,0,0,0,0,0,0,0,0,6],
    [7,0,0,0,0,0,0,0,0,0,0,7],
    [8,0,0,0,0,0,0,0,0,0,0,8],
    [9,0,0,0,0,0,0,0,0,0,0,9],
    [" ","  А","  Б","  В","  Г","  Д","  Е","  Ж","  З","  И","  К",""]]

b=[ [" ","  А","  Б","  В","  Г","  Д","  Е","  Ж","  З","  И","  К",""],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,0,0,0,0,0,3],
    [4,0,0,0,0,0,0,0,0,0,0,4],
    [5,0,0,0,0,0,0,0,0,0,0,5],
    [6,0,0,0,0,0,0,0,0,0,0,6],
    [7,0,0,0,0,0,0,0,0,0,0,7],
    [8,0,0,0,0,0,0,0,0,0,0,8],
    [9,0,0,0,0,0,0,0,0,0,0,9],
    [" ","  А","  Б","  В","  Г","  Д","  Е","  Ж","  З","  И","  К",""]]

def printarr():
    global a
    for i in a:
        for j in i:
            print("{:3}".format(j),end=" ")
        print()
    print()

def fill():   #расстановка живых клеток
    global a,alive
    print("Введите количество живых клеток:", end=" ")
    quant=int(input())
    while quant !=0:
        print("Введите координату живой клетки (например Б5):", end=" ")
        pos=str(input())
        if check_pos(pos)!=1:
            yx(pos)
            if a[y][x]=='  X':
                print("Координата занята!")
            else:
                a[y][x]='  X'
                alive+=1
                quant-=1
                printarr()

def check_pos(pos):   #проверка правильности введенных координат
    ch=0
    b = 'АБВГДЕЖЗИК'
    c = '0123456789'
    if len(pos) != 2 or (pos[0] not in b) or (pos[1] not in c):
        # or pos[2]not in[1,2,3,4,5,6,7,8,9,10]:
        print("Вы ввели значение в неправильном формате. Пример=Г5.")
        ch=1
        return ch

def yx(pos):  #конвертация координат в индексы
    global y,x
    b = 'АБВГДЕЖЗИК'
    y = int(pos[1]) + 1
    x = 0
    for i in range(10):
        if b[i] == pos[0]:
            x = int(i) + 1
    #print("y=",y,"x=",x) #местоположение в матрице

def birth():
    global a,b,alive
    for i in range (1,11):
        for j in range (1,11):
            b[i][j]=a[i][j]
            if a[i][j]==0:
                count=0
                if a[i+1][j]=='  X':
                    count+=1
                if a[i-1][j]=='  X':
                    count+=1
                if a[i][j+1]=='  X':
                    count+=1
                if a[i][j-1]=='  X':
                    count+=1
                if a[i+1][j+1]=='  X':
                    count+=1
                if a[i-1][j-1]=='  X':
                    count+=1
                if a[i+1][j-1]=='  X':
                    count+=1
                if a[i-1][j+1]=='  X':
                    count+=1
                if count==3:
                    b[i][j]='  X'
                    alive+=1

def dead():
    global a,b,alive
    alive=0
    for i in range (1,11):
        for j in range (1,11):
            if a[i][j]=='  X':
                alive+=1
                count=0
                if a[i+1][j]=='  X':
                    count+=1
                if a[i-1][j]=='  X':
                    count+=1
                if a[i][j+1]=='  X':
                    count+=1
                if a[i][j-1]=='  X':
                    count+=1
                if a[i+1][j+1]=='  X':
                    count+=1
                if a[i-1][j-1]=='  X':
                    count+=1
                if a[i+1][j-1]=='  X':
                    count+=1
                if a[i-1][j+1]=='  X':
                    count+=1
                if count<2 or count>3:
                    b[i][j]=0
                    alive-=1
    for i in range (1,11):
        for j in range (1,11):
            a[i][j]=b[i][j]

def life():
    global alive
    while alive!=0:
        birth()
        printarr()
        dead()
        printarr()
        print("Нажмите Enter для продолжения",end=" ")
        next=str(input())


printarr()
fill()
life()
