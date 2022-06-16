class stek():
    mas = []
    def push(self):
        self.mas.append(input("Введите данные для добавления в стек:"))
    def pop(self):
        print(self.mas[len(self.mas)-1])
        self.mas.pop(len(self.mas)-1)
    def show(self):
        print(self.mas[len(self.mas)-1])
    def count(self):
        print("Колличество элементов в стеке:",len(self.mas))

class queue():
    mas = []
    def push(self):
        self.mas.append(input("Введите данные для добавления в очередь:"))
    def pop(self):
        print(self.mas[0])
        self.mas.pop(0)
    def show(self):
        print(self.mas[0])
    def count(self):
        print("Колличество элементов в очереди:",len(self.mas))

def showmenu():
    print("[1] Записать значение в стек")
    print("[2] Записать значение в очередь")
    print("[3] Удалить значение из стека")
    print("[4] Удалить значение из очереди")
    print("[5] Показать значение в стеке")
    print("[6] Показать значение в очереди")
    print("[7] Показать количество значений в стеке")
    print("[8] Показать количество значений в очереди")
    print("[0] Выход")

inp = 1
s = stek()
q = queue()
while inp != 0:
    showmenu()
    inp = int(input("Выберете пункт меню:"))
    if inp == 0:
        break
    elif inp == 1:
        s.push()
    elif inp == 2:
        q.push()
    elif inp == 3:
        s.pop()
    elif inp == 4:
        q.pop()
    elif inp == 5:
        s.show()
    elif inp == 6:
        q.show()
    elif inp == 7:
        s.count()
    elif inp == 8:
        q.count()
    print()
