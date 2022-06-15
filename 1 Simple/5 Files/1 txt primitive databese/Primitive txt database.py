mas=[]


def printmenu():
    print("[1] Показать")
    print("[2] Открыть")
    print("[3] Сохранить")
    print("[4] Найти")
    print("[5] Фильтр по цене")
    print("[6] Фильтр по типу")
    print("[0] Выйти")

def show():
    global mas
    for i in range (len(mas)):
        print(mas[i],"\t")

def openfile():
    global mas
    mas=open('./text.txt').read()
    mas=mas.splitlines()
    for i in range (len(mas)):
        mas[i]=mas[i].split(" ")
        mas[i][2]=int(mas[i][2])

def write_safe():
    global mas
    type = str(input("Введите тип товара:")) + ' '
    name = str(input("Введите название товара:")) + ' '
    price = str(input("Введите цену товара:"))
    f = open('./text.txt','a')
    f.write('\n' + type + name + price)
    f.close
    openfile()

def find():
    global mas
    name_for_find = str(input("Введите название для поиска:"))
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if mas[i][j] == name_for_find:
                print("Товар:",mas[i][1],"в категории:",mas[i][0],"по цене:",mas[i][2])

def price_filter():
    global mas
    price = int(input("Введите цену:"))
    for i in range(len(mas)):
        if mas[i][2] == price:
            print("По цене:",price,"товар:",mas[i][1],"в категории:",mas[i][0])

def type_filter():
    global mas
    type = str(input("Введите тип товара:"))
    for i in range(len(mas)):
        if mas[i][0] == type:
            print("В категории:",mas[i][0],"товар:",mas[i][1],"по цене:",mas[i][2])

sel=1
while (sel != 0):
    printmenu()
    sel = int(input())
    if sel == 1:
        show()
    if sel == 2:
        openfile()
    if sel == 3:
        write_safe()
    if sel == 4:
        find()
    if sel == 5:
        price_filter()
    if sel == 6:
        type_filter()
