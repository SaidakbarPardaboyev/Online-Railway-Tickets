import mysql.connector as mys
import os


class Database:
    def __init__(self,Username,Password):
        self.con = mys.connect(host='localhost', username=Username, password=Password)
        self.kursor = self.con.cursor()
        self.D_Name = "Online_Railway_Tickets"
        self.T1_name = "Users"
        self.T2_name = "Trains"
        self.T3_name = "Orders"

        self.Create_db()
        self.Create_Tables()

    def Create_db(self):
        buyruq = f"Create database if not exists {self.D_Name}"
        self.kursor.execute(buyruq)

    def Create_Tables(self):
        self.kursor.execute(f"use {self.D_Name}")
        self.kursor.execute("Show tables")
        tables = self.kursor.fetchall()
        if tables != [('orders',), ('trains',), ('users',)]:
            self.kursor.execute(f"use {self.D_Name}")
            buyruq = f"""Create table if not exists {self.T1_name}(id int primary key auto_increment NOT NULL,Name varchar(100)
                        NOT NULL, Surname varchar(100) NOT NULL, Email varchar(100) NOT NULL, Password varchar(100) NOT NULL,
                        ID_number varchar(100))"""
            self.kursor.execute(buyruq)

            buyruq = f"""Create table if not exists {self.T2_name}(id int primary key auto_increment NOT NULL,Name varchar(100)
                        NOT NULL, Capacity int NOT NULL, Free int NOT NULL, Price int NOT NULL, Sanasi date NOT NULL,
                        Vaqti varchar(20) NOT NULL, FromA varchar(100) NOT NULL, ToB varchar(100) NOT NULL)"""
            self.kursor.execute(buyruq)

            self.Inserting()

            buyruq = f"""Create table if not exists {self.T3_name}(id int primary key auto_increment NOT NULL,User_id int
                        NOT NULL, Train_id int NOT NULL)"""
            self.kursor.execute(buyruq)

    def Inserting(self):
        self.kursor.execute(f"use {self.D_Name}")

        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("BKA 105", 200, 12, 
                            150000, '2024-02-02', "18:00", "Toshkent", "Jizzax")""")

        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("Afrosiyob", 200, 50, 
                            150000, '2024-02-02', "10:30", "Toshkent", "Jizzax")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("BKA 105", 200, 14, 
                            150000, '2024-02-02', "21:15", "Toshkent", "Jizzax")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("BKA 105", 200, 27, 
                            150000, '2024-01-25', "10:30", "Toshkent", "Xorazm")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("Afrosiyob", 200, 1, 
                            150000, '2024-01-25', "15:00", "Toshkent", "Xorazm")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("BKA 105", 200, 34, 
                            150000, '2024-01-31', "10:30", "Surxondaryo", "Samarqand")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("Afrosiyob", 200, 10, 
                            150000, '2024-01-30', "14:00", "Samarqand", "Navoiy")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("Afrosiyob", 200, 28, 
                            150000, '2024-02-18', "10:30", "Samarqand", "Navoiy")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("BKA 105", 200, 61, 
                            150000, '2024-02-16', "10:30", "Jizzax", "Xorazm")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("BKA 105", 200, 5, 
                            150000, '2024-02-16', "21:00", "Jizzax", "Xorazm")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("BKA 105", 200, 2, 
                            150000, '2024-02-16', "16:10", "Jizzax", "Xorazm")""")
        
        self.kursor.execute(f"""insert into {self.T2_name}(Name, Capacity, Free, Price, Sanasi, Vaqti, FromA, ToB) values("Afrosiyob", 200, 7, 
                            150000, '2024-02-16', "08:00", "Jizzax", "Xorazm")""")
        self.con.commit()
                            

# os.system("cls")
# db = Database("root", "root")