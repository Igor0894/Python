import pickle
class car():
    ID = ""
    firm = ""
    model = ""
    price_in = 0
    price_out = 0
    sell = 0
    delta = 0
    def __init__(self,ID,firm,model,price_in):
        self.ID = ID
        self.firm = firm
        self.model = model
        self.price_in = price_in

    def add(self):
        self.ID=input("Госномер:")
        self.firm = input("Марка:")
        self.model = input("Модель:")
        self.price_in = int(input("Цена закупки:"))

    def show(self):
        print("Госномер:",self.ID,"Марка:",self.firm,"Модель:",self.model,"Цена закупки:",self.price_in)

    def show_sell(self):
        print("Госномер:",self.ID,"Марка:",self.firm,"Модель:",self.model,"Цена закупки:",self.price_in,"Цена продажи:",self.price_out,"Прибыль от продажи:",self.delta)

    def sell(self):
        self.price_out = int(input("Введите цену продажи:"))
        self.delta = self.price_out - self.price_in
        print("Прибыль от продажи автомобиля:",self.delta)

class allcars():
    allcar = []
    sellscar = []

    def show(self):
       for i in self.allcar:
           i.show()

    def show_sells(self):
       for i in self.sellscar:
           i.show_sell()

    def add(self):
       ID = input("Госномер:")
       firm = input("Марка:")
       model = input("Модель:")
       price_in = int(input("Цена закупки:"))
       new_car = car(ID,firm,model,price_in)
       self.allcar.append(new_car)

    def delcar(self):
        k = 0
        ID = input("Введите госномер:")
        for i in self.allcar:
           if i.ID == ID:
               print("Будет удалён автомобиль:")
               i.show()
               break
           k += 1
        if k != len(self.allcar):
           self.allcar.pop(k)
        else:
           print("Автомобиль не найден")

    def findcar(self):
        k = 0
        ID = input("Введите госномер:")
        for i in self.allcar:
            if i.ID == ID:
               i.show()
               break
            k += 1
        if k == len(self.allcar):
            print("Автомобиль не найден")

    def savecar(self):
        with open(r"C:\Users\igor.kornaukhov\AppData\Local\Programs\Python\Python37\Lib\data1.txt", 'wb') as pickle_out:
            pickle.dump(self.allcar, pickle_out)
        with open(r"C:\Users\igor.kornaukhov\AppData\Local\Programs\Python\Python37\Lib\data2.txt", 'wb') as pickle_out:
            pickle.dump(self.sellscar, pickle_out)

    def loadcar(self):
        with open(r"C:\Users\igor.kornaukhov\AppData\Local\Programs\Python\Python37\Lib\data1.txt", 'rb') as pickle_in:
            self.allcar = pickle.load(pickle_in)
        with open(r"C:\Users\igor.kornaukhov\AppData\Local\Programs\Python\Python37\Lib\data2.txt", 'rb') as pickle_in:
            self.sellscar = pickle.load(pickle_in)

    def sellcar(self):
        k = 0
        ID = input("Введите госномер продаваемого авто:")
        for i in self.allcar:
           if i.ID == ID:
               i.show()
               i.sell()
               self.sellscar.append(i)
               self.allcar.pop(k)
               print("Автомобиль продан")
               break
           k += 1
           if k == len(self.allcar):
               print("Автомобиль не найден")

    def pribyl(self):
        money = 0
        for i in self.sellscar:
            money += i.delta
        print("Общая прибыль:",money)


def showmenu():
    print("[1] Показать автомобиль")
    print("[2] Сохранить")
    print("[3] Открыть")
    print("[4] Добавить")
    print("[5] Найти")
    print("[6] Продать авто")
    print("[7] Удалить")
    print("[8] Отчет о проданных авто")
    print("[9] Прибыль")
    print("[0] Выход")

c = allcars()

while True:
    showmenu()
    v=int(input("Выберете элемент меню:"))
    if v == 0:
        break
    if v == 1:
        c.show()
    if v == 2:
        c.savecar()
    if v == 3:
        c.loadcar()
    if v == 4:
        c.add()
    if v == 5:
        c.findcar()
    if v == 6:
        c.sellcar()
    if v == 7:
        c.delcar()
    if v == 8:
        c.show_sells()
    if v == 9:
        c.pribyl()
    print()
