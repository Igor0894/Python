import pyodbc
from tkinter import *
from tkinter import ttk

class Sql:
    def __init__(self, database, server="localhost\SQLEXPRESS"):
        self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
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
        dbCursor.execute(query)
        self.cnxn.commit()
    def delete_data(self,where,table):
        dbCursor = self.cnxn.cursor()
        query = "DELETE FROM " + table + " WHERE " + where
        dbCursor.execute(query)
        self.cnxn.commit()
    def correct_data(self,table,column,data,where):
        dbCursor = self.cnxn.cursor()
        query = "UPDATE " + table + " SET " + column + " = '" + data + "' WHERE " + column + " = '" + where + "'"
        dbCursor.execute(query)
        self.cnxn.commit()
    def take_data(self,columns,mass,table):
        dbCursor = self.cnxn.cursor()
        for i in range (len(columns)):
            query = "SELECT [" + columns[i] + "] FROM " + table
            dbCursor.execute(query)
            for result in dbCursor:
                #print(result[0])
                mass[i].append(result[0])
        self.cnxn.commit()
    def take_data_where(self,columns,mass,table,where,where_column):
        dbCursor = self.cnxn.cursor()
        all_columns = ""
        for i in range (len(columns)):
            if i < len(columns) - 1:
                all_columns += columns[i] + ","
            else:
                all_columns += columns[i]
        query = "SELECT " + all_columns + " FROM " + table + " WHERE " + where_column + " = " + where
        #print(query)
        dbCursor.execute(query)
        for result in dbCursor:
            for i in range(len(columns)):
                mass[i].append(result[i])
        self.cnxn.commit()
    def take_all_data_where(self,mass,table,where,where_column):
        dbCursor = self.cnxn.cursor()
        query = "SELECT * FROM " + table + " WHERE " + where_column + " = " + where
        #print(query)
        dbCursor.execute(query)
        for result in dbCursor:
            #print(result)
            for i in result:
                mass.append(i)
        self.cnxn.commit()
    def take_data_where_and(self,columns,mass,table,where,where_column):
        dbCursor = self.cnxn.cursor()
        for i in range (len(columns)):
            query = "SELECT [" + columns[i] + "] FROM [test].[dbo].[" + table + "]" + " WHERE " + where_column[0] + " = '" + where[0] + "'"
            for j in range (1,len(where)):
                query += " AND " + where_column[j] + " = '" + where[j] + "'"
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
            dbCursor.execute(query)
            for result in dbCursor:
                #print(result[0])
                mass[i].append(result[0])
            #print(mass[i])
        self.cnxn.commit()

class Rights:
    def __init__(self):
        self.logins = [[],[]]
        sql.take_data(["Login","ID_Login"], [self.logins[0],self.logins[1]], "Logins")
        self.roles_for_logins = []
        self.id_usergroup_for_logins = []
    def find_user_groups(self):
        for i in range (len(self.logins[1])):  #поиск id ролей и соответствующих id пользовательскиъ групп
            self.roles_for_logins.append([])
            self.id_usergroup_for_logins.append([])
            self.roles_for_login(self.logins[1][i],self.roles_for_logins[i],self.id_usergroup_for_logins[i])
        self.user_groups = []
        for i in self.id_usergroup_for_logins: #загрузка данных соответствующих пользовательскиъ групп
            for j in i:
                if isinstance(j,int):
                    self.user_groups.append(self.user_groups_for_role(str(j)))
        self.rights = [] #сюда записываю права [таблица,название полей,данные полей,разрешение]
        self.load_all_rights()
    def load_all_rights(self):
        for i in range(len(self.user_groups)):  # загрузка разрешений на доступ по данным всех пользовательских] групп
            self.rights.append([[]])
            self.load_one_rights(str(self.user_groups[i][1][0]),i,0,legacy=0)
    def load_one_rights(self,id_table,i,table,legacy): #(id таблицы, пользовательская группа, порядковый номер таблицы в массиве, наследование)
            table_name = []
            id_slavetable = []
            self.load_tables(id_table, table_name, id_slavetable)
            self.rights[i][table].append(table_name[0])
            self.rights[i][table].append([])
            sql.take_data_where(["COLUMN_NAME"], mass=[self.rights[i][table][1]], table='INFORMATION_SCHEMA.COLUMNS',
                                where="'" + table_name[0] + "'",
                                where_column='TABLE_NAME')
            if legacy == 0:
                key = self.user_groups[i][2][0]
                key_value = str(self.user_groups[i][3][0])
                self.rights[i][table].append([])
                sql.take_all_data_where(mass=self.rights[i][table][2], table=table_name[0],
                                        where="'" + key_value + "'",
                                        where_column=key)
            elif legacy == 1:
                [key,key_value] = self.find_key(self.rights[i][table-1][1],self.rights[i][table][1],self.rights[i][table-1][2])
                self.rights[i][table].append([])
                sql.take_all_data_where(mass=self.rights[i][table][2], table=table_name[0],
                                        where="'" + key_value + "'",
                                        where_column=key)
            if id_slavetable[0] != None and len(self.rights[i][table][2]) > 0:
                self.rights[i].append([])
                self.load_one_rights(str(id_slavetable[0]),i,table+1,1)
            #print(self.rights)
    def find_key(self,columns_parent,columns_child, values_parent): #поиск полей и их значений по которым наследуется доступ в таблицах
        for i in range(len(columns_parent)):
            for j in columns_child:
                if columns_parent[i] == j:
                    return [columns_parent[i],str(values_parent[i])]
    def print_rights(self):
        for i in range(len(self.rights)): #перебор по пользователбским группам
            print("У пользовательской группы " + str(self.user_groups[i][0][0]) + " следующие права доступа:")
            for j in range(len(self.rights[i])): #перебор по правам пользователя
                    print("В таблице " + str(self.rights[i][j][0]) + " по следующим столбцам " +  str(self.rights[i][j][1]) + " доступ к данным " + str(self.rights[i][j][2]))
    def load_tables(self,id_table,table_name,id_slavetable):
        sql.take_data_where(columns=["Table_Name", "ID_SlaveTable"], mass=[table_name,id_slavetable], table="Tables",
                where=("'" + id_table + "'"), where_column="ID_Table")
    def roles_for_login(self,login,roles,id_usergroup):
        sql.take_data_where(columns=["Name_Login_Group","ID_UserGroup"],mass=[roles,id_usergroup],table="Logins_Groups",where=str(login),where_column="ID_Login")
    def user_groups_for_role(self,id_usergroup):
        name_group = []
        id_table = []
        id_field = []
        field_value = []
        act_add = []
        act_del = []
        act_upd = []
        act_full = []
        legacy = []
        sql.take_data_where(columns=["Name_Group","ID_Table","ID_Field","Field_Value","Act_Add","Act_Del","Act_Upd","Act_Full","Legacy"],
                            mass=[name_group,id_table,id_field,field_value,act_add,act_del,act_upd,act_full,legacy],
                            table="User_Groups",where=id_usergroup,
                            where_column="ID_UserGroup")
        return name_group,id_table,id_field,field_value,act_add,act_del,act_upd,act_full,legacy

sql = Sql('test2')
test_rights = Rights()
test_rights.find_user_groups()
test_rights.print_rights()
