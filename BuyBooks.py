from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mys
from os import *
from sys import *
from PyQt5.QtGui import QPixmap
from datetime import *

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
        self.D_Name = "OnlineBookSale"
        self.T1_name = "Users"
        self.T2_name = "Books"
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
        
        self.Bir_tomonlanga.clicked.connect(lambda: self.Bir_tomon_click())
        self.Borish_Qaytish.clicked.connect(lambda: self.Borish_Qaytish_click())

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
        Borish = self.Borish_sanasi.text()

        try:
            Borish = datetime.strptime(Borish, '%Y-%m-%d').date()
            if current_date <= Borish:
                self.Borish_sanasi_check.setStyleSheet("""color: transparent;""")
                lamp = True
            else:
                self.Borish_sanasi_check.setStyleSheet("""color: red;""")
                lamp = False
        except ValueError:
            self.Borish_sanasi_check.setStyleSheet("""color: red;""")
            lamp = False
        
        if self.IsBorib_Qaytish:
            Qaytish = self.Qaytish_sanasi.text()

            try:
                Qaytish = datetime.strptime(Qaytish, '%Y-%m-%d').date()
                if Borish <= Qaytish:
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



    def Bir_tomon_click(self):
        self.Qaytish_sanasi_check.setStyleSheet("""color: transparent;""")
        self.Borish_sanasi.setGeometry(912, 637, 550, 60)
        self.IsBorib_Qaytish = False
        
    def Borish_Qaytish_click(self):
        self.Qaytish_sanasi.setText("")
        self.Borish_sanasi.setGeometry(912, 637, 273, 60)
        self.IsBorib_Qaytish = True
        
    def Buttum_Buttons(self):
        self.wForButtumButton = QWidget()
        self.Layout_Buttons = QHBoxLayout(self.wForButtumButton)
        self.Layout_Buttons.setSpacing(100)

        self.Buyurtmalar_soni = QLabel("Buyurtmalar soni: 0")
        self.Buyurtmalar_soni.setAlignment(Qt.AlignCenter)
        self.Buyurtmalar_soni.setStyleSheet("""
                                                background-color: #D9D9D9;
                                                color: black;
                                                background-position: center;
                                                """)
        self.Buyurtmalar_soni.setFont(QFont("Calibri", 20, weight= 80))
        # self.Buyurtmalar_soni.setFixedSize()
        self.Layout_Buttons.addWidget(self.Buyurtmalar_soni)

        # Creating A button to order meals
        self.OrderButton = QPushButton("Buyurtma berish", clicked= self.order_click)
        self.OrderButton.setStyleSheet("""
                                        background-color: #D9D9D9;
                                        color: black;
                                        background-position: center;
                                        """)
        self.OrderButton.setFont(QFont("Calibri", 20, weight= 80))

        self.Layout_Buttons.addWidget(self.OrderButton)

        # Creating a label for showing the price of all the ordered meals
        self.SumLabel = QLabel("0 som")
        self.SumLabel.setAlignment(Qt.AlignCenter)
        self.SumLabel.setStyleSheet("""
                                    background-color: #D9D9D9;
                                    color: black;
                                    background-position: center;
                                    """)
        self.SumLabel.setFont(QFont("Montserrot", 15, weight=80))

        self.Layout_Buttons.addWidget(self.SumLabel)
        self.mainLayout.addWidget(self.wForButtumButton)

    def order_click(self):
        if len(self.Order_Book_ids) > 0:
            self.kursor.execute(f"use {self.D_Name}")
            self.id_list = ', '.join(map(str, self.Order_Book_ids))
            self.kursor.execute(f"SELECT * FROM {self.T2_name} WHERE id IN ({self.id_list})")

            ls = self.kursor.fetchall()

            msg = QMessageBox()
            msg.setFixedSize(500,400)
            msg.setWindowTitle("Order Book")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            msg.setText("Do you want to order?")

            info_book = list(map(lambda x: x[1], ls))
            info_book = "\n".join(info_book)
            msg.setInformativeText(info_book)

            msg.buttonClicked.connect(self.Write_orders_to_db)

            msg.exec_()

    def Write_orders_to_db(self, button):
        if button.text() == "&Yes":
            self.kursor.execute(f"use {self.D_Name}")
            for i in set(self.Order_Book_ids):
                B_id = i
                B_count = self.Order_Book_ids.count(i)
                self.kursor.execute(f"""insert into {self.T3_name}(User_id, Book_id, count) 
                                    values ({self.User_information[0]}, {B_id}, {B_count})""")
            self.con.commit()

            self.Buyurtmalar_soni.setText("Buyurtmalar soni: 0")
            self.SumLabel.setText("0 som")
            self.Order_Book_ids.clear()
            self.Clear_labels()

    def Clear_labels(self):
        for i in self.List_count:
            i.setText("0")

    def Show_Who_user(self):
        wid1 = QWidget()
        W1Lay = QHBoxLayout(wid1)

        self.Show_user = QLabel(f"{self.User_information[1]} {self.User_information[2]}")
        self.Show_user.setFont(QFont("Montserrat", 20))
        self.Show_user.setStyleSheet("""
                                     color: white
                                     """)
        self.Show_user.setFixedSize(1200, 100)
        W1Lay.addWidget(self.Show_user)

        self.OrdersB = QPushButton("Buyurtmalarim")
        self.OrdersB.setFixedSize(250, 50)
        self.OrdersB.setStyleSheet("""border: 2px solid black;
                                        color: black;
                                        background-color: #DADADA""")
        self.OrdersB.setFont(QFont("Montserrat", 15, weight=100))
        self.OrdersB.clicked.connect(lambda: self.All_Orders())
        W1Lay.addWidget(self.OrdersB)

        self.mainLayout.addWidget(wid1)

    def All_Orders(self):
        self.kursor.execute(f"use {self.D_Name}")
        self.kursor.execute(f"select Book_id from {self.T3_name} where User_id = '{self.User_information[0]}' ")
        lll = self.kursor.fetchall()
        ls = Myorders(lll, self.Db_Username, self.Db_Password)
        ls.exec_()
        
    def Show_Book_name_author_price(self):
        self.WforNameAuthorPrice = QWidget()
        self.WforNameAuthorPrice.setFixedSize(1400, 80)
        self.WforNameAuthorPrice.setStyleSheet("""
                                                background-color: #D9D9D9
                                                """)
        self.Book_name_label = QLabel("Kitob nomi", self.WforNameAuthorPrice)
        self.Book_name_label.setFont(QFont("Montserrat", 20, weight= 100))
        self.Book_name_label.setAlignment(Qt.AlignCenter)
        self.Book_name_label.setGeometry(0, 0, 400, 80)
        self.Book_name_label.setStyleSheet("border: 2px solid black;")

        self.Book_Author_label = QLabel("Kitob muallifi", self.WforNameAuthorPrice)
        self.Book_Author_label.setFont(QFont("Montserrat", 20, weight= 100))
        self.Book_Author_label.setAlignment(Qt.AlignCenter)
        self.Book_Author_label.setGeometry(400, 0, 400, 80)
        self.Book_Author_label.setStyleSheet("border: 2px solid black;")

        self.Book_Price_label = QLabel("Kitob narxi", self.WforNameAuthorPrice)
        self.Book_Price_label.setFont(QFont("Montserrat", 20, weight= 100))
        self.Book_Price_label.setAlignment(Qt.AlignCenter)
        self.Book_Price_label.setGeometry(800, 0, 350, 80)
        self.Book_Price_label.setStyleSheet("border: 2px solid black;")

        self.tem = QLabel("", self.WforNameAuthorPrice)
        self.tem.setFont(QFont("Montserrat", 20, weight= 100))
        self.tem.setAlignment(Qt.AlignCenter)
        self.tem.setGeometry(1150, 0, 250, 80)
        self.tem.setStyleSheet("border: 2px solid black;")

        self.mainLayout.addWidget(self.WforNameAuthorPrice)


class Myorders(QDialog):
    def __init__(self, ls, Db_Username, Db_Password):
        super().__init__()
        self.setMinimumSize(1350, 700)
        self.setMaximumSize(1350, 700)
        self.setStyleSheet("background-color: #EAFFFF")
        self.setWindowTitle("Order List")
        self.setWindowIcon(QIcon("bookstore.ico"))

        OWid = QWidget(self)
        OWid.setFixedSize(1350, 700)
        OWid.setStyleSheet("""color: black;
                                background-color: #DADADA;""")
        OWid.setFont(QFont("Montserrat", 15, weight=100))
        OWLayout = QVBoxLayout(OWid)

        ScrollArea = QScrollArea()
        ScrollArea.setFixedSize(1350,700)
        container = QWidget()
        ScrollArea.setStyleSheet("background-color: #D9D9D9")
        Scroll_Layout = QVBoxLayout(container)

        self.con = mys.connect(host='localhost', user=Db_Username, password=Db_Password)
        self.D_Name = "OnlineBookSale"
        self.T2_name = "Books"
        self.kursor = self.con.cursor()
        self.kursor.execute(f"use {self.D_Name}")
        placeholders = ', '.join(map(lambda x: str(x[0]), ls))
        self.kursor.execute(f"select * from {self.T2_name} where id in ({placeholders})")
        list_books = self.kursor.fetchall()

        self.ls = []  # Initialize self.ls
        for book_info in list_books:
            tem = self.BookCard(book_info)
            self.ls.append(tem)
            Scroll_Layout.addWidget(self.ls[-1])

        ScrollArea.setWidget(container)
        OWLayout.addWidget(ScrollArea)



    def BookCard(self, book_info):
        wind_book = QWidget()
        wind_book.setFixedSize(1350, 100)
        self.book_layout = QHBoxLayout()

        self.book_name = QTextEdit()
        self.book_name.setPlainText(book_info[1])
        self.book_name.setReadOnly(True)
        self.book_name.setAlignment(Qt.AlignCenter)
        self.book_name.setFixedSize(400, 80)
        self.book_name.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.book_name.setFont(QFont("Montserrat", 15, weight=100))

        self.book_author = QLabel()
        self.book_author.setText(book_info[4])
        self.book_author.setAlignment(Qt.AlignCenter)
        self.book_author.setFixedSize(400, 80)
        self.book_author.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.book_author.setFont(QFont("Montserrat", 15, weight=100))

        self.book_price = QLabel()
        self.book_price.setText(str(book_info[3]))
        self.book_price.setAlignment(Qt.AlignCenter)
        self.book_price.setFixedSize(350, 80)
        self.book_price.setStyleSheet("""border: 2px solid black;
                                        color: black;""")
        self.book_price.setFont(QFont("Montserrat", 15, weight=100))

        self.book_layout.addWidget(self.book_name)
        self.book_layout.addWidget(self.book_author)
        self.book_layout.addWidget(self.book_price)

        wind_book.setLayout(self.book_layout)

        return wind_book



if __name__ == "__main__":
    app = QApplication([])
    ilova = BuyBooks()
    ilova.show()
    app.exec_()

        # def MinusOrder(self, book_info, label):
    #     if book_info[0] in self.Order_Book_ids:
    #         if int(label.text().strip()) != 0:
    #             label.setText(str(int(label.text().strip()) - 1))
    #         self.Order_Book_ids.remove(book_info[0])
    #         self.MinusCount()
    #         self.MinusSumma(book_info[3])

    # def MinusSumma(self, Price):
    #     tem = str(int(self.SumLabel.text()[:-4].strip()) - int(Price))
    #     self.SumLabel.setText(tem + " som")

    # def MinusCount(self):
    #     tem = int(self.Buyurtmalar_soni.text()[18:].strip()) - 1
    #     self.Buyurtmalar_soni.setText("Buyurtmalar soni: " + str(tem))

    # def PilusOrder(self, book_info, label):
    #     label.setText(str(int(label.text().strip()) + 1))
    #     self.List_count.append(label)
    #     self.PilusCount()
    #     self.PilusSumma(book_info[3])
    #     self.Order_Book_ids.append(book_info[0])

    # def PilusSumma(self, Price):
    #     tem = str(int(self.SumLabel.text()[:-4].strip()) + int(Price))
    #     self.SumLabel.setText(tem + " som")

    # def PilusCount(self):
    #     tem = int(self.Buyurtmalar_soni.text()[18:].strip()) + 1
    #     self.Buyurtmalar_soni.setText("Buyurtmalar soni: " + str(tem))


    # def Show_Book_info(self):
    #     self.ScrollArea = QScrollArea()
    #     self.container = QWidget()
    #     self.ScrollArea.setStyleSheet("background-color: #D9D9D9")
    #     self.Scroll_Layout = QVBoxLayout(self.container)

    #     self.kursor.execute(f"use {self.D_Name}")
    #     self.kursor.execute(f"select * from {self.T2_name}")  # Corrected table name
    #     self.list_books = self.kursor.fetchall()

    #     for book_info in self.list_books:
    #         tem = self.BookCard(book_info)
    #         self.ls.append(tem)
    #         self.Scroll_Layout.addWidget(self.ls[-1])

    #     self.ScrollArea.setWidget(self.container)
    #     self.mainLayout.addWidget(self.ScrollArea)




    # def BookCard(self, book_info):
    #     wind_book = QWidget()
    #     wind_book.setFixedSize(1350, 100)
    #     self.book_layout = QHBoxLayout()

    #     self.book_name = QTextEdit()
    #     self.book_name.setPlainText(book_info[1])
    #     self.book_name.setReadOnly(True)
    #     self.book_name.setAlignment(Qt.AlignCenter)
    #     self.book_name.setFixedSize(400, 80)
    #     self.book_name.setStyleSheet("""border: 2px solid black;
    #                                     color: black;""")
    #     self.book_name.setFont(QFont("Montserrat", 15, weight=100))

    #     self.book_author = QLabel()
    #     self.book_author.setText(book_info[4])
    #     self.book_author.setAlignment(Qt.AlignCenter)
    #     self.book_author.setFixedSize(400, 80)
    #     self.book_author.setStyleSheet("""border: 2px solid black;
    #                                     color: black;""")
    #     self.book_author.setFont(QFont("Montserrat", 15, weight=100))

    #     self.book_price = QLabel()
    #     self.book_price.setText(str(book_info[3]))
    #     self.book_price.setAlignment(Qt.AlignCenter)
    #     self.book_price.setFixedSize(350, 80)
    #     self.book_price.setStyleSheet("""border: 2px solid black;
    #                                     color: black;""")
    #     self.book_price.setFont(QFont("Montserrat", 15, weight=100))

    #     Count = QLabel("0")
    #     Count.setAlignment(Qt.AlignCenter)
    #     Count.setFixedSize(50, 80)
    #     Count.setStyleSheet("""border: 2px solid black;
    #                                     color: black;""")
    #     Count.setFont(QFont("Montserrat", 15, weight=100))

    #     self.Pilus = QPushButton("+")
    #     self.Pilus.setFixedSize(70, 80)
    #     self.Pilus.setStyleSheet("""border: 2px solid black;
    #                                     color: black;""")
    #     self.Pilus.setFont(QFont("Montserrat", 15, weight=100))
    #     self.Pilus.clicked.connect(lambda: self.PilusOrder(book_info, Count))


    #     self.Minus = QPushButton("-")
    #     self.Minus.setFixedSize(70, 80)
    #     self.Minus.setStyleSheet("""border: 2px solid black;
    #                                     color: black;""")
    #     self.Minus.setFont(QFont("Montserrat", 15, weight=100))
    #     self.Minus.clicked.connect(lambda: self.MinusOrder(book_info, Count))

    #     self.book_layout.addWidget(self.book_name)
    #     self.book_layout.addWidget(self.book_author)
    #     self.book_layout.addWidget(self.book_price)
    #     self.book_layout.addWidget(self.Pilus)
    #     self.book_layout.addWidget(Count)
    #     self.book_layout.addWidget(self.Minus)

    #     wind_book.setLayout(self.book_layout)

    #     return wind_book