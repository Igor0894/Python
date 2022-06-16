import tkinter

import pyodbc
from datetime import datetime
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from datetime import datetime, date

class logger():
    def __init__(self,file, log_level):
        self.file = file
        self.user = ""
        self.log_level = log_level
    def open(self):
        self.f = open(self.file,'a')
    def date_time(self):
        today = str(date.today())
        time = datetime.now()
        current_time = str(time.strftime("%H:%M:%S"))
        self.now = today + " " + current_time
    def info(self,message):
        if self.log_level in ("info","debug"):
            self.open()
            self.date_time()
            self.f.write(self.now + " INFO (" + self.user + ") " + message + '\n')
            self.close()
    def error(self,message):
        self.open()
        self.f.write(self.now + " ERROR (" + self.user + ") " + message + '\n')
        self.date_time()
        self.close()
    def debug(self,message):
        if self.log_level in ("debug"):
            self.open()
            self.date_time()
            self.f.write(self.now + " DEBUG (" + self.user + ") " + message + '\n')
            self.close()
    def close(self):
        self.f.close()

class Sql:
    def __init__(self, database, server="localhost\SQLEXPRESS"):
        self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
                                   #"Uid="+user+";"
                                   #"Pwd="+password)
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now()
                                                         .strftime("%d/%m/%Y"))
    def insert_data(self,columns,data,table):
        dbCursor = self.cnxn.cursor()
        columns_str = ""
        data_str = ""
        for i in range(len(columns)):
            if i == len(columns) - 1:
                columns_str += "[" + columns[i] + "]"
                data_str += "'" +  data[i] + "'"
            else:
                columns_str += "[" + columns[i] + "],"
                data_str += "'" + data[i] + "',"
        query = "INSERT INTO " + table + " (" + columns_str + ") VALUES (" + data_str + ")"
        log.debug(query)
        dbCursor.execute(query)
        self.cnxn.commit()
    def delete_data(self,where,table):
        dbCursor = self.cnxn.cursor()
        query = "DELETE FROM " + table + " WHERE " + where
        #log.info("Удалена строка из таблицы: " + table + " где: " + where)
        log.debug(query)
        dbCursor.execute(query)
        self.cnxn.commit()
    def correct_data(self,table,column,data,where):
        dbCursor = self.cnxn.cursor()
        query = "UPDATE " + table + " SET " + column + " = '" + data + "' WHERE " + column + " = '" + where + "'"
        #log.info("Изменена строка из таблицы: " + table + " где: " + column + " = " + where + " на значение: " + data)
        log.debug(query)
        dbCursor.execute(query)
        self.cnxn.commit()
    def take_data(self,columns,mass,table):
        dbCursor = self.cnxn.cursor()
        for i in range (len(columns)):
            query = "SELECT [" + columns[i] + "] FROM [test].[dbo].[" + table + "]"
            log.debug("Запрос SQL на получение данных: "+str(query))
            dbCursor.execute(query)
            for result in dbCursor:
                #print(result[0])
                mass[i].append(result[0])
            log.debug("Полученный массив данных: " + str(mass))
        self.cnxn.commit()
    def take_data_where(self,columns,mass,table,where,where_column):
        dbCursor = self.cnxn.cursor()
        all_columns = ""
        for i in range(len(columns)):
            if i < len(columns) - 1:
                all_columns += columns[i] + ","
            else:
                all_columns += columns[i]
        query = "SELECT " + all_columns + " FROM " + table + " WHERE " + where_column + " = " + where
        # print(query)
        dbCursor.execute(query)
        for result in dbCursor:
            for i in range(len(columns)):
                mass[i].append(result[i])
        self.cnxn.commit()
    def take_data_where_and(self,columns,mass,table,where,where_column):
        dbCursor = self.cnxn.cursor()
        for i in range (len(columns)):
            query = "SELECT [" + columns[i] + "] FROM [test].[dbo].[" + table + "]" + " WHERE " + where_column[0] + " = '" + where[0] + "'"
            for j in range (1,len(where)):
                query += " AND " + where_column[j] + " = '" + where[j] + "'"
            log.debug(query)
            dbCursor.execute(query)
            for result in dbCursor:
                #print(result[0])
                mass[i].append(result[0])
            #print(mass[i])
        self.cnxn.commit()
    def take_data_where_and_for_login(self,columns,mass,table,where,where_pass):
        dbCursor = self.cnxn.cursor()
        for i in range (len(columns)):
            query = "SELECT [" + columns[i] + "] FROM [test].[dbo].[" + table + "]" + " WHERE login = '" + where + "' AND pass = HASHBYTES('MD5','" + where_pass + "')"
            dbCursor.execute(query)
            for result in dbCursor:
                #print(result[0])
                mass[i].append(result[0])
            #print(mass[i])
        self.cnxn.commit()
    def take_inner_data_where(self,columns,mass,table1,table2,where,where_from,on_table1,on_table2):
        dbCursor = self.cnxn.cursor()
        for i in range (len(columns)):
            query = "SELECT [" + columns[i] + "] FROM [test].[dbo].[" + table1 + "] INNER JOIN [test].[dbo].[" + table2 + "] ON " + table1 + "." + on_table1 + " = " + table2 + "." + on_table2 + " WHERE " + where_from + " = '" + where + "'"
            log.debug(query)
            dbCursor.execute(query)
            for result in dbCursor:
                #print(result[0])
                mass[i].append(result[0])
            #print(mass[i])
        self.cnxn.commit()

class TTab:
    def __init__(self, tab_name, t_control):
        self.tab = ttk.Frame(t_control)
        t_control.add(self.tab, text=tab_name)

class tab_table:
    def __init__(self, tab, columns_name, columns_width):
        self.tab = tab.tab
        columns1 = []
        for i in range(len(columns_name)):
            columns1.append('#' + str(i + 1))
        self.table = ttk.Treeview(self.tab)
        self.table.grid(row=0, column=0, rowspan=8, padx=5, pady=5)
        self.table['columns'] = columns1
        self.table.column("#0", width=0, stretch=NO)
        for i in range(len(columns_name)):
            self.table.column(columns1[i], anchor=CENTER, width=columns_width[i])
        self.table.heading("#0", text="", anchor=CENTER)
        for i in range(len(columns_name)):
            self.table.heading(columns1[i], text=columns_name[i], anchor=CENTER)
    def load_data(self,columns,table):
        all_data = []
        for i in range(len(columns)):
            data = []
            all_data.append(data)
        sql.take_data(columns,all_data,table)
        for i in range (len(all_data[0])):
            new_data = []
            for j in range (len(all_data)):
                mas = []
                mas.append(all_data[j][i])
                new_data.append(mas)
            self.table.insert(parent='', index='end', iid=i, text='', values=new_data)

class TAuto:
    def __init__(self):
        self.window_login = Tk()
        self.window_login.title("Авторизация")
        self.window_login.geometry("400x100")
        self.lbl_login = Label(self.window_login, text="Введите имя пользователя:", font=("Arial Bold", 10))
        self.lbl_login.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.txt_login = Entry(self.window_login, width=20)
        self.txt_login.grid(row=0, column=1, padx=5, pady=5)
        self.lbl_pass = Label(self.window_login, text="Введите пароль пользователя:", font=("Arial Bold", 10))
        self.lbl_pass.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.txt_pass = Entry(self.window_login, width=20)
        self.txt_pass.grid(row=1, column=1, padx=5, pady=5)
        self.btn_login = Button(self.window_login, text="Войти", command=self.login)
        self.btn_login.grid(row=1, column=2, padx=5)
        self.good_login = False
        self.all_roles = ["Администратор","Менеджер"]
        while not self.good_login:
            self.window_login.mainloop()

    def login(self):
        user = self.txt_login.get()
        password = self.txt_pass.get()
        self.user_group = []
        try:
            sql.take_data_where_and_for_login(["group"],[self.user_group],"Users",user,password)
            if self.user_group[0] in self.all_roles:
                log.info("Выполнен вход, пользователь: " + user + " , роль: " + self.user_group[0])
                log.user = user
                self.good_login = True
                self.window_login.destroy()
                self.main()
        except Exception:
            log.info("Неудачная попытка входа, пользователь: " + user)
            messagebox.showerror('Ошибка авторизации', 'Имя пользователя и/или пароль не найдены')

    def main(self):
        self.window = Tk()
        self.window.title("АРМ " + self.user_group[0] + "а")
        self.window.geometry("800x400")
        self.tab_control = ttk.Notebook(self.window)
        if self.user_group[0] in ["Менеджер"]:
            tab_contract = TTab('Договора',self.tab_control)
            tab_cars = TTab('Автомобили',self.tab_control)
            tab_peoples = TTab('Физ.лица',self.tab_control)
            tab_marks = TTab("Марки",self.tab_control)
            tab_models = TTab("Модели",self.tab_control)
            #tab_colors = TTab("Цвета",self.tab_control)
            tab_lists = TTab("Справочники", self.tab_control)
            def colors():
                colors_window = list("Цвета автомобилей","Цвет","Color","Color",200)
            btn_colors = Button(tab_lists.tab, text="Цвета автомобилей", command=colors)
            btn_colors.grid(row=0, column=0, padx=5, pady=5)
            def marks():
                marks_window = list("Марки автомобилей","Марка","Mark","Marks",200)
            btn_marks = Button(tab_lists.tab, text="Марки автомобилей", command=marks)
            btn_marks.grid(row=1, column=0, padx=5, pady=5)
            def posts():
                posts_window = list("Должности","Должность","Post","Posts",400)
            btn_posts = Button(tab_lists.tab, text="Должности", command=posts)
            btn_posts.grid(row=2, column=0, padx=5, pady=5, sticky=E + W)
            def transmissions():
                transmissions_window = list("Типы трансмиссий","Трансмиссия","Transmission","Transmission",300)
            btn_transmissions = Button(tab_lists.tab, text="Типы трансмиссий", command=transmissions)
            btn_transmissions.grid(row=3, column=0, padx=5, pady=5, sticky=E + W)

        def add_user():
            self.window_add_user = Tk()
            self.window_add_user.title("Добавление пользователя")
            self.window_add_user.geometry("400x100")
            lbl_login = Label(self.window_add_user, text="Логин:", font=("Arial Bold", 10))
            lbl_login.grid(row=0, column=0, padx=5, pady=5, sticky="e")
            txt_login = Entry(self.window_add_user, width=20)
            txt_login.grid(row=0, column=1, padx=5, pady=5, sticky="w")
            lbl_pass = Label(self.window_add_user, text="Пароль:", font=("Arial Bold", 10))
            lbl_pass.grid(row=1, column=0, padx=5, pady=5, sticky="e")
            txt_pass = Entry(self.window_add_user, width=20)
            txt_pass.grid(row=1, column=1, padx=5, pady=5, sticky="w")
            lbl_role = Label(self.window_add_user, text="Роль:", font=("Arial Bold", 10))
            lbl_role.grid(row=2, column=0, padx=5, pady=5, sticky="e")
            combo_roles = Combobox(self.window_add_user, width=20)
            combo_roles.grid(row=2, column=1, padx=5, pady=5, sticky="w")
            combo_roles['values'] = self.all_roles
            def add_user_btn():
                login = txt_login.get()
                password = txt_pass.get()
                group = combo_roles.get()
                if group in self.all_roles and login != "" and password != "":
                    query = "INSERT INTO Users ([login],[pass],[group]) VALUES ('" + login + "',HASHBYTES('MD5','" + password + "'),'" + group + "')"
                    log.info("Добавлен пользователь: " + login + " Роль: " + group)
                    log.debug("INSERT INTO Users ([login],[pass],[group]) VALUES ('" + login + "',HASHBYTES('MD5','password'),'" + group + "')")
                    dbCursor = sql.cnxn.cursor()
                    dbCursor.execute(query)
                    sql.cnxn.commit()
                    table_users.table.delete(*table_users.table.get_children())
                    table_users.load_data(["login", "group"], "Users")
                    self.window_add_user.destroy()
                else:
                    log.info("Неудачная попытка добавления пользователя: " + txt_login.get() + " с ролью: " + combo_roles.get())
                    log.debug("INSERT INTO Users ([login],[pass],[group]) VALUES ('" + login + "',HASHBYTES('MD5','password'),'" + group + "')")
                    messagebox.showerror('Ошибка добавления нового пользователя', 'Не заполнены все поля')
            btn = Button(self.window_add_user, text="Добавить", command=add_user_btn)
            btn.grid(row=0, column=2, padx=5, pady=5, sticky="n")

        def del_user():
            row_id = int(table_users.table.focus())
            selected_item = table_users.table.selection()
            value = table_users.table.item(selected_item, option="values")
            if value[0] != log.user:
                sql.delete_data("login = '" + value[0] + "'","Users")
                table_users.table.delete(row_id)
                log.info("Удалён пользователь " + value[0])
            else:
                messagebox.showerror('Ошибка удаления пользователя', 'Вы пытаетесь удалить свою учётную запись')
                log.info("Неудачная попытка удаления пользователя: " + value[0])

        if self.user_group[0] in ["Администратор"]:
            tab_users = TTab("Пользователи", self.tab_control)
            table_users = tab_table(tab_users, ["Пользователь", "Роль"], [150, 200])
            table_users.load_data(["login", "group"], "Users")
            btn_users_add = Button(tab_users.tab, text="Добавить", command=add_user)
            btn_users_add.grid(row=0, column=1, padx=5, pady=5, sticky=E+W+S+N)
            btn_users_del = Button(tab_users.tab, text="Удалить", command=del_user)
            btn_users_del.grid(row=1, column=1, padx=5, pady=5, sticky=E+W+S+N)

        self.tab_control.pack(expand=1, fill='both')
        if self.good_login:
            self.window.mainloop()

class list:
    def __init__(self, name, column_name, column_data, table, column_width):
        self.window = Tk()
        self.window.title(name)
        width = int(column_width / 200 * 400)
        self.window.geometry(str(width) + "x300")
        self.column_name = column_name
        self.column_width = column_width #200
        self.new_table()
        self.load_data([column_data],table)
        def add_data():
            self.window_add = Tk()
            self.window_add.title("Добавление " + self.column_name)
            self.window_add.geometry("400x100")
            lbl_data = Label(self.window_add, text=self.column_name + ":", font=("Arial Bold", 10))
            lbl_data.grid(row=0, column=0, padx=5, pady=5, sticky="e")
            txt_data = Entry(self.window_add, width=20)
            txt_data.grid(row=0, column=1, padx=5, pady=5, sticky="w")
            def add_btn():
                data = txt_data.get()
                #value = table_users.table.item(selected_item, option="values")
                res = []
                query = "select count(*) FROM Color WHERE Color = '" + data + "'"
                dbCursor = sql.cnxn.cursor()
                dbCursor.execute(query)
                for result in dbCursor:
                    res.append(result[0])
                sql.cnxn.commit()
                query = "INSERT INTO " + table + " ([" + column_data + "]) VALUES ('" + data + "')"
                if data != "" and res[0] == 0:
                    log.info("Добавлено значение: " + data + " в справочник: " + name)
                    log.debug(query)
                    dbCursor = sql.cnxn.cursor()
                    dbCursor.execute(query)
                    sql.cnxn.commit()
                    self.table.delete(*self.table.get_children())
                    self.load_data([column_data],table)
                    self.window_add.destroy()
                else:
                    log.info("Неудачная попытка добавления значения: " + data + " в справочник: " + name)
                    log.debug(query)
                    messagebox.showerror('Ошибка добавления данных', 'Не введено значение или такое значение уже имеется')
            btn = Button(self.window_add, text="Добавить", command=add_btn)
            btn.grid(row=0, column=2, padx=5, pady=5, sticky="n")
        btn_add = Button(self.window, text="Добавить", command=add_data)
        btn_add.grid(row=0, column=1, padx=5, pady=5, sticky=E + W + S + N)
        def del_data():
            try:
                selected_item = self.table.selection()
                #value = self.table.item(selected_item, option="values")
                value = self.table.item(selected_item, option="text")
                self.window_del = Tk()
                self.window_del.title("Удаление " + self.column_name)
                self.window_del.geometry("350x100")
                #lbl_data = Label(self.window_del, text="Вы уверены, что хотите удалить " + column_name + " '" + value[0] + "'    ?", font=("Arial Bold", 10))
                lbl_data = Label(self.window_del,
                                 text="Вы уверены, что хотите удалить " + column_name + " '" + value + "'    ?",
                                 font=("Arial Bold", 10))
                lbl_data.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
                def del_btn():
                    #sql.delete_data(column_data + " = '" + value[0] + "'", table)
                    sql.delete_data(column_data + " = '" + value + "'", table)
                    log.info("Удалён " + column_name + " " + value)
                    self.table.delete(*self.table.get_children())
                    self.load_data([column_data], table)
                    self.window_del.destroy()
                def close_window():
                    self.window_del.destroy()
                btn_yes = Button(self.window_del, text="Да", command=del_btn)
                btn_yes.grid(row=1, column=0, padx=5, pady=5, sticky=E + W + S + N)
                btn_no = Button(self.window_del, text="Нет", command=close_window)
                btn_no.grid(row=1, column=1, padx=5, pady=5, sticky=E + W + S + N)
            except Exception:
                self.window_del.destroy()
                messagebox.showerror('Ошибка удаления', 'Не выбран ' + column_name)
        btn_del = Button(self.window, text="Удалить", command=del_data)
        btn_del.grid(row=1, column=1, padx=5, pady=5, sticky=E + W + S + N)
        def correct_data():
            try:
                #row_id = int(self.table.focus())
                selected_item = self.table.selection()
                #value = self.table.item(selected_item, option="values")
                value = self.table.item(selected_item, option="text")
                self.window_correct = Tk()
                self.window_correct.title("Изменение " + self.column_name)
                self.window_correct.geometry("300x150")
                lbl_data = Label(self.window_correct,
                                 text="Измените значение " + column_name + " :",
                                 font=("Arial Bold", 10))
                lbl_data.grid(row=0, column=0, padx=5, pady=5)
                txt_data = Entry(self.window_correct, width=40)
                txt_data.grid(row=1, column=0, padx=5, pady=5, sticky="w")
                #txt_data.insert(0, value[0])
                txt_data.insert(0, value)
                def correct_btn():
                    data = txt_data.get()
                    #sql.correct_data(table, column_data, data, value[0])
                    sql.correct_data(table, column_data, data, value)
                    #self.table.delete(row_id)
                    #log.info("Изменён " + column_name + " '" + value[0] + "' на: '" + data + "'")
                    log.info("Изменён " + column_name + " '" + value + "' на: '" + data + "'")
                    self.table.delete(*self.table.get_children())
                    self.load_data([column_data], table)
                    self.window_correct.destroy()
                btn_correct = Button(self.window_correct, text="Изменить", command=correct_btn)
                btn_correct.grid(row=2, column=0, padx=5, pady=5, sticky=E + W + S + N)
            except Exception:
                self.window_correct.destroy()
                messagebox.showerror('Ошибка изменения', 'Не выбран ' + column_name)

        btn_del = Button(self.window, text="Удалить", command=del_data)
        btn_del.grid(row=1, column=1, padx=5, pady=5, sticky=E + W + S + N)
        btn_correct = Button(self.window, text="Изменить", command=correct_data)
        btn_correct.grid(row=2, column=1, padx=5, pady=5, sticky=E + W + S + N)

    def new_table(self):
        #columns1 = ['#1']
        self.table = ttk.Treeview(self.window,selectmode='browse')
        scrl = ttk.Scrollbar(self.window,orient="vertical", command=self.table.yview)
        scrl.grid(row=0, column=0, rowspan=8, sticky=E + S + N)
        self.table.configure(yscrollcommand=scrl.set)
        self.table.grid(row=0, column=0, rowspan=8, padx=5, pady=5)
        #self.table['columns'] = columns1
        #self.table.column("#0", width=0, stretch=NO)
        self.table.column("#0", width=self.column_width)
        #self.table.column(columns1[0], anchor=CENTER, width=self.column_width)
        #self.table.heading("#0", text="", anchor=CENTER)
        self.table.heading("#0", text=self.column_name, anchor=CENTER)
        #self.table.heading(columns1[0], text=self.column_name, anchor=CENTER)

    def load_data(self, column, table):
        data = []
        sql.take_data(column, [data], table)
        for i in range(len(data)):
            #self.table.insert(parent='', index='end', iid=i, text='', values=(data[i]))
            self.table.insert(parent='', index='end', text=data[i])

log = logger('log.txt',"debug")
sql = Sql('test')
autodiller = TAuto()
