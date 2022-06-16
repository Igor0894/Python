class years_rpd:
    def __init__(self,data,year):
        self.data = data
        self.year = year
    def rpd_count(self):
        self.rpd = {}
        ind_kafedra = 10
        ind_year = 1
        for i in range (len(self.data)):
            if self.data[i][ind_year] == self.year:
                if self.rpd.get(self.data[i][ind_kafedra]) == None:
                    self.rpd[self.data[i][ind_kafedra]] = 1
                else:
                    self.rpd[self.data[i][ind_kafedra]] += 1

class csv_table:
    data=[]
    file=""
    def __init__(self,file):
        self.file=file
    def readfile(self):
        self.data = open(self.file).read()
        self.data = self.data.splitlines()
        for i in range (len(self.data)):
            self.data[i] = self.data[i].split(";")
    def show_table(self):
        print(self.data)
    def repair(self):
        for i in range (len(self.data)):
            j = len(self.data[i]) - 1
            while self.data[i][j].count("@") > 1 and j > 1:
                if self.data[i][j - 1].count("@") > 1:
                    self.data[i][j - 1] += self.data[i][j]
                    self.data[i].pop(j)
                j = j - 1
    def lines_max(self):
        print(len(self.data))
    def rpd_count(self):
        rpd = {}
        rpd1 = {}
        ind_kafedra = 10
        status_rpd = 4
        for i in range (len(self.data)):
            if self.data[i][status_rpd] == "Готово":
                if rpd.get(self.data[i][ind_kafedra]) == None:
                    rpd[self.data[i][ind_kafedra]] = 1
                else:
                    rpd[self.data[i][ind_kafedra]] += 1
        print("Количество кафедр с разработанными РПД в статусе готово:")
        print(len(rpd))
        print(rpd)
        for i in range (len(self.data)):
            if self.data[i][status_rpd] == "В работе" or self.data[i][status_rpd] == "На доработке":
                if rpd1.get(self.data[i][ind_kafedra]) == None:
                    rpd1[self.data[i][ind_kafedra]] = 1
                else:
                    rpd1[self.data[i][ind_kafedra]] += 1
        print()
        print("Количество кафедр с разработанными РПД в статусе в работе/на доработке:")
        print(len(rpd1))
        print(rpd1)
    def rpd_max_teacher(self):
        rpd = {}
        ind_teacher = 15
        for i in range (len(self.data)):
            if rpd.get(self.data[i][ind_teacher]) == None:
                rpd[self.data[i][ind_teacher]] = 1
            else:
                rpd[self.data[i][ind_teacher]] += 1
        max = 0
        teacher = ""
        for i in rpd:
            if rpd[i] > max:
                max = rpd [i]
                teacher = i
        print("Больше всего РПД (",max,") сделал преподаватель:",teacher)
        print("Количество преподавателей:",len(rpd))
    def rpd_max_wait(self):
        rpd = {}
        ind_teacher = 15
        status_rpd = 4
        for i in range (len(self.data)):
            if self.data[i][status_rpd] != "Готово":
                if rpd.get(self.data[i][ind_teacher]) == None:
                    rpd[self.data[i][ind_teacher]] = 1
                else:
                    rpd[self.data[i][ind_teacher]] += 1
        max = 0
        teacher = ""
        for i in rpd:
            if rpd[i] > max:
                max = rpd[i]
                teacher = i
        print("Больше всего долгов по РПД (", max, ") у преподавателя:", teacher)
        print("Количество должников:", len(rpd))
    def all_teacher(self):
        rpd = {}
        ind_teacher = 15
        status_rpd = 4
        for i in range(1,len(self.data)):
            if rpd.get(self.data[i][ind_teacher]) == None:
                rpd[self.data[i][ind_teacher]] = 1
            else:
                rpd[self.data[i][ind_teacher]] += 1
        print("Все преподаватели (",len(rpd),"), которые когда-либо делали РПД:")
        for i in rpd:
            print(i)
    def rpd_for_years(self):
        rpd_for_years = []
        years = {}
        ind_year = 1
        kafedras = {}
        all_years_kafedras = {}
        for i in range(1,len(self.data)):
            if years.get(self.data[i][ind_year]) == None:
                years[self.data[i][ind_year]] = 1
            else:
                years[self.data[i][ind_year]] += 1
        for i in years:
            new_year = years_rpd(self.data,i)
            rpd_for_years.append(new_year)
            new_year.rpd_count()
        for i in range(len(rpd_for_years)-1,0,-1):
            print("С года",rpd_for_years[i].year,"по год",rpd_for_years[i-1].year,"в следующих кафедрах увеличивается число РПД:")
            for j in rpd_for_years[i].rpd:
                if rpd_for_years[i-1].rpd.get(j) != None:
                    if rpd_for_years[i].rpd[j] < rpd_for_years[i-1].rpd[j]:
                        if kafedras.get(j) == None:
                            kafedras[j] = 1
                        else:
                            kafedras[j] += 1
                        if all_years_kafedras.get(j) == None:
                            all_years_kafedras[j] = 1
                        else:
                            all_years_kafedras[j] += 1
            for i in kafedras:
                print(i,"увеличивается на",kafedras[i])
            kafedras = {}
            print()
        max = 0
        kafedra = ""
        for i in all_years_kafedras:
            if all_years_kafedras[i] > max:
                max = all_years_kafedras[i]
                kafedra = i
        print("Максимально увеличилось РПД (",max,") у кафедры:",kafedra)



tab=csv_table("O:\\Учёба\\Python\\13 Парсинг CSV\\text.csv")
tab.readfile()
tab.repair()

# выполнение задач

def showmenu():
    print("[1] Показать таблицу")
    print("[2] Показать количество обработанных строк")
    print("[3] Показать какие кафедры сколько разработали РПД (в статусе готово), сколько еще осталось доработать( статус в работе, на доработке)")
    print("[4] Показать кто из преподавателей сделал больше всего РПД")
    print("[5] Показать кто является максимальным задолженником по РПД")
    print("[6] Показать список всех преподавателей, которые когда-либо делали РПД")
    print("[7] Выявить тенденцию по годам у какой кафедры увеличивается число РПД")
    print("[0] Выход")

inp = 1
while inp != 0:
    showmenu()
    inp = int(input("Выберете пункт меню:"))
    print()
    if inp == 0:
        break
    elif inp == 1:
        tab.show_table()
    elif inp == 2:
        tab.lines_max()
    elif inp == 3:
        tab.rpd_count()
    elif inp == 4:
        tab.rpd_max_teacher()
    elif inp == 5:
        tab.rpd_max_wait()
    elif inp == 6:
        tab.all_teacher()
    elif inp == 7:
        tab.rpd_for_years()
    print()
