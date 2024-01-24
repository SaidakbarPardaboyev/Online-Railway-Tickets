from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mys
from os import *
from sys import *
from PyQt5.QtGui import QPixmap
from datetime import *

class Available_trains(QDialog):
    def __init__(self, list_Available_trains, Db_Username, Db_Password, CurUser_id):
        super().__init__()
        self.CurUser_id = CurUser_id
        self.setMinimumSize(1800, 700)
        self.setMaximumSize(1800, 700)
        self.setStyleSheet("background-color: #D9D9D9")
        self.setWindowTitle("Order List")
        self.setWindowIcon(QIcon("bookstore.ico"))
        self.layout_Orders = QVBoxLayout(self)

        self.con = mys.connect(host='localhost', user=Db_Username, password=Db_Password)
        self.kursor = self.con.cursor()
        self.D_Name = "Online_Railway_Tickets"
        self.T2_name = "Trains"
        self.T3_name = "Orders"

        wForButtumButton = QWidget()
        wForButtumButton.setFixedSize(1800, 50)
        Layout_Buttons = QHBoxLayout(wForButtumButton)
        Layout_Buttons.setSpacing(0)

        Name_T = QLabel("Nomi")
        Name_T.setFixedSize(200, 50)
        Name_T.setAlignment(Qt.AlignCenter)
        Name_T.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Name_T.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Name_T)

        Free_seats = QLabel("Bosh o'rinlar soni")
        Free_seats.setFixedSize(250, 50)
        Free_seats.setAlignment(Qt.AlignCenter)
        Free_seats.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Free_seats.setFont(QFont("Calibri", 16, weight= 80))
        Layout_Buttons.addWidget(Free_seats)

        
        Price_t = QLabel("Narxi")
        Price_t.setFixedSize(200, 50)
        Price_t.setAlignment(Qt.AlignCenter)
        Price_t.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Price_t.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Price_t)

        Sana = QLabel("Sanasi")
        Sana.setFixedSize(200, 50)
        Sana.setAlignment(Qt.AlignCenter)
        Sana.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Sana.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Sana)

        Vaqti = QLabel("Vaqti")
        Vaqti.setFixedSize(200, 50)
        Vaqti.setAlignment(Qt.AlignCenter)
        Vaqti.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Vaqti.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Vaqti)

        From_P = QLabel("Qayerdan")
        From_P.setFixedSize(200, 50)
        From_P.setAlignment(Qt.AlignCenter)
        From_P.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        From_P.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(From_P)

        To_W = QLabel("Qayerga")
        To_W.setFixedSize(200, 50)
        To_W.setAlignment(Qt.AlignCenter)
        To_W.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        To_W.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(To_W)

        Just_space = QLabel("")
        Just_space.setFixedSize(200, 50)
        Just_space.setAlignment(Qt.AlignCenter)
        Just_space.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Just_space.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Just_space)

        self.layout_Orders.addWidget(wForButtumButton)


        OWid = QWidget()
        self.layout_Orders.addWidget(OWid)
        OWid.setFixedSize(1750, 650)
        OWid.setStyleSheet("""color: black;
                                background-color: #DADADA;""")
        OWid.setFont(QFont("Montserrat", 15, weight=100))
        OWLayout = QVBoxLayout(OWid)

        ScrollArea = QScrollArea()
        ScrollArea.setFixedSize(1750,650)
        container = QWidget()
        ScrollArea.setStyleSheet("background-color: #D9D9D9")
        Scroll_Layout = QVBoxLayout(container)

        self.ls = []  # Initialize self.ls
        for info in list_Available_trains:
            tem = self.Card(info)
            self.ls.append(tem)
            Scroll_Layout.addWidget(self.ls[-1])

        ScrollArea.setWidget(container)
        OWLayout.addWidget(ScrollArea)

    def Card(self, book_info):
        wind = QWidget()
        wind.setFixedSize(1750, 100)
        Llayout = QHBoxLayout()

        name = QLabel()
        name.setText(str(book_info[1]))
        name.setAlignment(Qt.AlignCenter)
        name.setFixedSize(200, 50)
        name.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        name.setFont(QFont("Montserrat", 12, weight=100))

        Avaiable_seat = QLabel()
        Avaiable_seat.setText(str(book_info[3]))
        Avaiable_seat.setAlignment(Qt.AlignCenter)
        Avaiable_seat.setFixedSize(200, 50)
        Avaiable_seat.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        Avaiable_seat.setFont(QFont("Montserrat", 12, weight=100))

        price = QLabel()
        price.setText(str(str(book_info[4])))
        price.setAlignment(Qt.AlignCenter)
        price.setFixedSize(200, 50)
        price.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        price.setFont(QFont("Montserrat", 12, weight=100))

        J_Sanasi = QLabel()
        J_Sanasi.setText(str(book_info[5]))
        J_Sanasi.setAlignment(Qt.AlignCenter)
        J_Sanasi.setFixedSize(200, 50)
        J_Sanasi.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        J_Sanasi.setFont(QFont("Montserrat", 12, weight=100))

        J_Vaqti = QLabel()
        J_Vaqti.setText(str(book_info[6]))
        J_Vaqti.setAlignment(Qt.AlignCenter)
        J_Vaqti.setFixedSize(200, 50)
        J_Vaqti.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        J_Vaqti.setFont(QFont("Montserrat", 12, weight=100))

        Jonash_joyi = QLabel()
        Jonash_joyi.setText(str(book_info[7]))
        Jonash_joyi.setAlignment(Qt.AlignCenter)
        Jonash_joyi.setFixedSize(200, 50)
        Jonash_joyi.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        Jonash_joyi.setFont(QFont("Montserrat", 12, weight=100))

        Qaytish_joyi = QLabel()
        Qaytish_joyi.setText(str(book_info[8]))
        Qaytish_joyi.setAlignment(Qt.AlignCenter)
        Qaytish_joyi.setFixedSize(200, 50)
        Qaytish_joyi.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        Qaytish_joyi.setFont(QFont("Montserrat", 12, weight=100))

        Buy_Ticket = QPushButton("Tanlash", self)
        Buy_Ticket.setFixedSize(140, 50)
        Buy_Ticket.setFont(QFont("Montserrat", 12, weight =100))
        Buy_Ticket.setStyleSheet("""color: white;
                                            background-color: #163E85;
                                            border-radius: 15px;""")
        Buy_Ticket.clicked.connect(lambda: self.Buy_Ticket_click(book_info, Avaiable_seat, Buy_Ticket))

        Llayout.addWidget(name)
        Llayout.addWidget(Avaiable_seat)
        Llayout.addWidget(price)
        Llayout.addWidget(J_Sanasi)
        Llayout.addWidget(J_Vaqti)
        Llayout.addWidget(Jonash_joyi)
        Llayout.addWidget(Qaytish_joyi)
        Llayout.addWidget(Buy_Ticket)

        wind.setLayout(Llayout) 
        return wind
    
    def Buy_Ticket_click(self, book_info, label, butt):
        try:
            self.kursor.execute(f"use {self.D_Name}")
            self.kursor.execute(f"""INSERT INTO {self.T3_name}(User_id, Train_id) VALUES
                                    ({self.CurUser_id},{book_info[0]})""")
            self.kursor.execute(f"""UPDATE {self.T2_name}
                                    SET Free = Free - 1
                                    WHERE id = {book_info[0]}""")
            
            # Commit changes after database operations
            self.con.commit()

            if int(label.text()) != 0:
                label.setText(str(int(label.text()) - 1))
                butt.setEnabled(False)

            # Open the Show_Ticket dialog
            tem = Show_Ticket()
            tem.exec_()

            # Enable the button after the dialog is closed
            if int(label.text()) != 0:
                butt.setEnabled(True)

        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            # Rollback changes if an error occurs
            self.con.rollback()


class Show_Ticket(QDialog):
    def __init__(self):
        super().__init__()
        label = QLabel(self)
        pixmap = QPixmap('Ticket.png')
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, pixmap.width(), pixmap.height())
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        self.setLayout(layout)

class Myorders(QDialog):
    def __init__(self, list_Available_trains):
        super().__init__()
        self.setMinimumSize(1800, 700)
        self.setMaximumSize(1800, 700)
        self.setStyleSheet("background-color: #D9D9D9")
        self.setWindowTitle("Order List")
        self.setWindowIcon(QIcon("bookstore.ico"))
        self.layout_Orders = QVBoxLayout(self)

        wForButtumButton = QWidget()
        wForButtumButton.setFixedSize(1800, 50)
        Layout_Buttons = QHBoxLayout(wForButtumButton)
        Layout_Buttons.setSpacing(0)

        Name_T = QLabel("Nomi")
        Name_T.setFixedSize(200, 50)
        Name_T.setAlignment(Qt.AlignCenter)
        Name_T.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Name_T.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Name_T)
        
        Price_t = QLabel("Narxi")
        Price_t.setFixedSize(200, 50)
        Price_t.setAlignment(Qt.AlignCenter)
        Price_t.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Price_t.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Price_t)

        Sana = QLabel("Sanasi")
        Sana.setFixedSize(200, 50)
        Sana.setAlignment(Qt.AlignCenter)
        Sana.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Sana.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Sana)

        Vaqti = QLabel("Vaqti")
        Vaqti.setFixedSize(200, 50)
        Vaqti.setAlignment(Qt.AlignCenter)
        Vaqti.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Vaqti.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Vaqti)

        From_P = QLabel("Qayerdan")
        From_P.setFixedSize(200, 50)
        From_P.setAlignment(Qt.AlignCenter)
        From_P.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        From_P.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(From_P)

        To_W = QLabel("Qayerga")
        To_W.setFixedSize(200, 50)
        To_W.setAlignment(Qt.AlignCenter)
        To_W.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        To_W.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(To_W)

        Just_space = QLabel("")
        Just_space.setFixedSize(200, 50)
        Just_space.setAlignment(Qt.AlignCenter)
        Just_space.setStyleSheet("""
                                background-color: #D9D9D9;
                                color: black;
                                background-position: center;
                                """)
        Just_space.setFont(QFont("Calibri", 20, weight= 80))
        Layout_Buttons.addWidget(Just_space)

        self.layout_Orders.addWidget(wForButtumButton)


        OWid = QWidget()
        self.layout_Orders.addWidget(OWid)
        OWid.setFixedSize(1750, 650)
        OWid.setStyleSheet("""color: black;
                                background-color: #DADADA;""")
        OWid.setFont(QFont("Montserrat", 15, weight=100))
        OWLayout = QVBoxLayout(OWid)

        ScrollArea = QScrollArea()
        ScrollArea.setFixedSize(1750,650)
        container = QWidget()
        ScrollArea.setStyleSheet("background-color: #D9D9D9")
        Scroll_Layout = QVBoxLayout(container)

        self.ls = []  # Initialize self.ls
        for info in list_Available_trains:
            tem = self.Card(info)
            self.ls.append(tem)
            Scroll_Layout.addWidget(self.ls[-1])

        ScrollArea.setWidget(container)
        OWLayout.addWidget(ScrollArea)

    def Card(self, book_info):
        wind = QWidget()
        wind.setFixedSize(1750, 100)
        Llayout = QHBoxLayout()

        name = QLabel()
        name.setText(str(book_info[0]))
        name.setAlignment(Qt.AlignCenter)
        name.setFixedSize(200, 50)
        name.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        name.setFont(QFont("Montserrat", 12, weight=100))

        price = QLabel()
        price.setText(str(str(book_info[1])))
        price.setAlignment(Qt.AlignCenter)
        price.setFixedSize(200, 50)
        price.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        price.setFont(QFont("Montserrat", 12, weight=100))

        J_Sanasi = QLabel()
        J_Sanasi.setText(str(book_info[2]))
        J_Sanasi.setAlignment(Qt.AlignCenter)
        J_Sanasi.setFixedSize(200, 50)
        J_Sanasi.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        J_Sanasi.setFont(QFont("Montserrat", 12, weight=100))

        J_Vaqti = QLabel()
        J_Vaqti.setText(str(book_info[3]))
        J_Vaqti.setAlignment(Qt.AlignCenter)
        J_Vaqti.setFixedSize(200, 50)
        J_Vaqti.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        J_Vaqti.setFont(QFont("Montserrat", 12, weight=100))

        Jonash_joyi = QLabel()
        Jonash_joyi.setText(str(book_info[4]))
        Jonash_joyi.setAlignment(Qt.AlignCenter)
        Jonash_joyi.setFixedSize(200, 50)
        Jonash_joyi.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        Jonash_joyi.setFont(QFont("Montserrat", 12, weight=100))

        Qaytish_joyi = QLabel()
        Qaytish_joyi.setText(str(book_info[5]))
        Qaytish_joyi.setAlignment(Qt.AlignCenter)
        Qaytish_joyi.setFixedSize(200, 50)
        Qaytish_joyi.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        Qaytish_joyi.setFont(QFont("Montserrat", 12, weight=100))

        Llayout.addWidget(name)
        Llayout.addWidget(price)
        Llayout.addWidget(J_Sanasi)
        Llayout.addWidget(J_Vaqti)
        Llayout.addWidget(Jonash_joyi)
        Llayout.addWidget(Qaytish_joyi)

        wind.setLayout(Llayout) 
        return wind

# from Create_database import Database
class BuyBooks(QWidget):
    def __init__(self, Db_Username, Db_Password, ls):
        super().__init__()
        self.User_information = ls
        self.ls = list()
        self.IsBorib_Qaytish = True
        self.List_count = list()
        self.Order_Book_ids = list()
        self.Db_Username = Db_Username
        self.Db_Password = Db_Password

        self.con = mys.connect(host='localhost', username=Db_Username, password=Db_Password)
        self.kursor = self.con.cursor()
        self.D_Name = "Online_Railway_Tickets"
        self.T1_name = "Users"
        self.T2_name = "Trains"
        self.T3_name = "Orders"

        label = QLabel(self)
        pixmap = QPixmap('Background.png')
        label.setPixmap(pixmap)
        self.move(0,0)
        self.setFixedSize(pixmap.width(), pixmap.height())

        self.Borish_Qaytish = QRadioButton(self)
        self.Borish_Qaytish.setGeometry(20, 630, 200, 30)
        self.Borish_Qaytish.setChecked(True)

        self.Bir_tomonlanga = QRadioButton(self)
        self.Bir_tomonlanga.setGeometry(20, 670, 200, 30)

        self.Viloyatlar = ["Toshkent", "Sirdaryo", "Jizzax", "Samarqand", "Qashqadaryo", "Surxondaryo", "Navoiy", "Xorazm",
                           "Qoraqalpoqiston", "Andijon", "Farg'ona"]

        self.combo_Qayerdan = QComboBox(self)
        self.combo_Qayerdan.addItem("Qayerdan") 
        self.combo_Qayerdan.addItems(self.Viloyatlar)
        self.combo_Qayerdan.setCurrentIndex(0)
        self.combo_Qayerdan.setGeometry(330, 637, 280, 60)
        self.combo_Qayerdan.setFont(QFont("Montserrat", 10, weight =100))
        self.combo_Qayerdan.setStyleSheet("""color: white;
                                            background-color: black;
                                            border: 2px solid #8B8C8D;
                                            border-radius: 10px;""")
        
        self.Qayerdan_check = QLabel("Invalid", self)
        self.Qayerdan_check.setGeometry(340, 610, 250, 20)
        self.Qayerdan_check.setStyleSheet("""color: transparent;""")
        self.Qayerdan_check.setFont(QFont("Montserrat", 9))
        
        self.combo_Qayerga = QComboBox(self)
        self.combo_Qayerga.addItem("Qayerga") 
        self.combo_Qayerga.addItems(self.Viloyatlar)
        self.combo_Qayerga.setCurrentIndex(0)
        self.combo_Qayerga.setGeometry(610, 637, 280, 60)
        self.combo_Qayerga.setFont(QFont("Montserrat", 10, weight =100))
        self.combo_Qayerga.setStyleSheet("""color: white;
                                            background-color: black;
                                            border: 2px solid #8B8C8D;
                                            border-radius: 10px;""")
        
        self.Qayerga_check = QLabel("Invalid", self)
        self.Qayerga_check.setGeometry(620, 610, 250, 20)
        self.Qayerga_check.setStyleSheet("""color: transparent;""")
        self.Qayerga_check.setFont(QFont("Montserrat", 9))
        
        self.Qaytish_sanasi = QLineEdit(self)
        self.Qaytish_sanasi.setPlaceholderText("YYYY-MM-DD") 
        self.Qaytish_sanasi.setGeometry(1188, 637, 275, 60)
        self.Qaytish_sanasi.setFont(QFont("Montserrat", 10, weight =100))
        self.Qaytish_sanasi.setStyleSheet("""color: white;
                                            background-color: black;
                                            border: 2px solid #8B8C8D;
                                            border-radius: 10px;""")
        
        self.Qaytish_sanasi_check = QLabel("Invalid", self)
        self.Qaytish_sanasi_check.setGeometry(1200, 610, 250, 20)
        self.Qaytish_sanasi_check.setStyleSheet("""color: transparent;""")
        self.Qaytish_sanasi_check.setFont(QFont("Montserrat", 9))
        
        self.Borish_sanasi = QLineEdit(self)
        self.Borish_sanasi.setPlaceholderText("YYYY-MM-DD") 
        self.Borish_sanasi.setGeometry(912, 637, 273, 60)
        self.Borish_sanasi.setFont(QFont("Montserrat", 10, weight =100))
        self.Borish_sanasi.setStyleSheet("""color: white;
                                            background-color: black;
                                            border: 2px solid #8B8C8D;
                                            border-radius: 10px;""")
        
        self.Borish_sanasi_check = QLabel("Invalid", self)
        self.Borish_sanasi_check.setGeometry(922, 610, 250, 20)
        self.Borish_sanasi_check.setStyleSheet("""color: transparent;""")
        self.Borish_sanasi_check.setFont(QFont("Montserrat", 9))

        
        self.sertch_ticketBtn = QPushButton("Bilet izlash", self)
        self.sertch_ticketBtn.setGeometry(1490, 637, 220, 55)
        self.sertch_ticketBtn.setFont(QFont("Montserrat", 12, weight =100))
        self.sertch_ticketBtn.setStyleSheet("""color: white;
                                            background-color: #163E85;
                                            border-radius: 15px;""")
        self.sertch_ticketBtn.clicked.connect(lambda: self.Search_Trains())

        self.BUyurtmalarim = QPushButton("Buyurtmalarim", self)
        self.BUyurtmalarim.setGeometry(1450, 500, 250, 55)
        self.BUyurtmalarim.setFont(QFont("Montserrat", 12, weight =100))
        self.BUyurtmalarim.setStyleSheet("""color: white;
                                            background-color: #163E85;
                                            border-radius: 15px;""")
        self.BUyurtmalarim.clicked.connect(lambda: self.Show_orders(self.User_information))
        
        self.Bir_tomonlanga.clicked.connect(lambda: self.Bir_tomon_click())
        self.Borish_Qaytish.clicked.connect(lambda: self.Borish_Qaytish_click())

    def Show_orders(self, User_information):
        self.con = mys.connect(host='localhost', username=self.Db_Username, password=self.Db_Password)
        self.kursor = self.con.cursor()
        self.D_Name = "Online_Railway_Tickets"
        self.T1_name = "Users"
        self.T2_name = "Trains"
        self.T3_name = "Orders"

        self.kursor.execute(f"use {self.D_Name}")
        buyruq = f"""select t.Name, t.Price, t.Sanasi, t.Vaqti, t.FromA, t.ToB
                    from Trains as t
                    left join Orders as o
                    on o.Train_id = t.id
                    where o.User_id = {User_information[0]};"""
        self.kursor.execute(buyruq)
        ls = self.kursor.fetchall()

        tem = Myorders(ls)
        tem.exec_()


    def Search_Trains(self):
        lamp = True
        if not self.combo_Qayerdan.currentText() != "Qayerdan":
            self.Qayerdan_check.setStyleSheet("""color: red;""")
            lamp = False
        else:
            self.Qayerdan_check.setStyleSheet("""color: transparent;""")
            lamp = True

        if not self.combo_Qayerga.currentText() != "Qayerga":
            self.Qayerga_check.setStyleSheet("""color: red;""")
            lamp = False
        else:
            if self.combo_Qayerdan.currentText() == self.combo_Qayerga.currentText():
                self.Qayerga_check.setStyleSheet("""color: red;""")
                lamp = False
            else:
                self.Qayerga_check.setStyleSheet("""color: transparent;""")
                lamp = True
        
        current_date = datetime.now().date()
        self.Borish = self.Borish_sanasi.text()

        try:
            self.Borish = datetime.strptime(self.Borish, '%Y-%m-%d').date()
            if current_date <= self.Borish:
                self.Borish_sanasi_check.setStyleSheet("""color: transparent;""")
                lamp = True
            else:
                self.Borish_sanasi_check.setStyleSheet("""color: red;""")
                lamp = False
        except ValueError:
            self.Borish_sanasi_check.setStyleSheet("""color: red;""")
            lamp = False
        
        if self.IsBorib_Qaytish:
            self.Qaytish = self.Qaytish_sanasi.text()

            try:
                self.Qaytish = datetime.strptime(self.Qaytish, '%Y-%m-%d').date()
                if self.Borish <= self.Qaytish:
                    self.Qaytish_sanasi_check.setStyleSheet("""color: transparent;""")
                    lamp = True
                else:
                    self.Qaytish_sanasi_check.setStyleSheet("""color: red;""")
                    lamp = False
            except ValueError:
                self.Qaytish_sanasi_check.setStyleSheet("""color: red;""")
                lamp = False
        else:
            self.Qaytish_sanasi_check.setStyleSheet("""color: transparent;""")

        if lamp:
            self.Search_Trains_from_DB()

    def Search_Trains_from_DB(self):
        list_Available_trains = None

        formatted_borish = self.Borish.strftime('%Y-%m-%d')

        self.con = mys.connect(host='localhost', username=self.Db_Username, password=self.Db_Password)
        self.kursor = self.con.cursor()
        self.D_Name = "Online_Railway_Tickets"
        self.T1_name = "Users"
        self.T2_name = "Trains"
        self.T3_name = "Orders"

        self.kursor.execute(f"use {self.D_Name}")

        if self.IsBorib_Qaytish:
            Qaytish = self.Qaytish.strftime('%Y-%m-%d')
            self.kursor.execute(f"""
                SELECT * FROM {self.T2_name}
                WHERE Free > 0 and FromA = '{self.combo_Qayerdan.currentText()}'
                AND ToB = '{self.combo_Qayerga.currentText()}'
                AND (Sanasi = '{formatted_borish}' OR Sanasi = '{Qaytish}')
                order by Sanasi
            """)
            # self.con.commit()
        else:
            self.kursor.execute(f"""
                SELECT * FROM {self.T2_name}
                WHERE Free > 0 and FromA = '{self.combo_Qayerdan.currentText()}'
                AND ToB = '{self.combo_Qayerga.currentText()}'
                AND Sanasi = '{formatted_borish}'
            """) 
            # self.con.commit()

        list_Available_trains = self.kursor.fetchall()

        Trainss = Available_trains(list_Available_trains, self.Db_Username, self.Db_Password, self.User_information[0])
        Trainss.exec_()

    def Bir_tomon_click(self):
        self.Qaytish_sanasi_check.setStyleSheet("""color: transparent;""")
        self.Borish_sanasi.setGeometry(912, 637, 550, 60)
        self.IsBorib_Qaytish = False
        
    def Borish_Qaytish_click(self):
        self.Qaytish_sanasi.setText("")
        self.Borish_sanasi.setGeometry(912, 637, 273, 60)
        self.IsBorib_Qaytish = True
        
    
if __name__ == "__main__":
    app = QApplication([])
    ilova = BuyBooks()
    ilova.show()
    app.exec_()