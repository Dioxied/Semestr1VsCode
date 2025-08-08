import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
from PyQt5.QtGui import QFont 
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import Qt 
import os  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Самсонов Александр Максимович: Вот что я люблю")
        self.setGeometry(250, 300, 700, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.label1 = QLabel("<u><b>Я очень люблю животных, а особенно котов</b></u>", self)
        self.label2 = QLabel("<u><i>Смотри какие они:</i></u>", self)

        fontlabel12 = QFont("Arial", 15)
        fontlabel34 = QFont("Calibri", 20)
        font2 = QFont("Arial", 10)

        self.label1.setFont(fontlabel12)
        self.label2.setFont(fontlabel12)

        self.label1.setStyleSheet("color: red")
        self.label2.setStyleSheet("color: red")

        self.label1.setAlignment(Qt.AlignLeft)
        self.label2.setAlignment(Qt.AlignRight)

        layout.addWidget(self.label1)
        layout.addWidget(self.label2)

        box = QHBoxLayout()
        self.lay1 = QVBoxLayout()
        self.lay2 = QVBoxLayout()
        box.addLayout(self.lay1)
        box.addLayout(self.lay2)

        layout.addLayout(box)

        self.button1 = QPushButton("Нажми, чтобы посмотреть", self)
        self.button1.clicked.connect(self.button1action)
        self.button2 = QPushButton("А вот еще фото", self)
        self.button2.clicked.connect(self.button2action)

        oneHBox_layout = QHBoxLayout()
        oneHBox_layout.addWidget(self.button1)
        oneHBox_layout.addWidget(self.button2)

        layout.addLayout(oneHBox_layout)

        self.button3 = QPushButton("Очистить фото", self)
        self.button3.clicked.connect(self.button3action)

        layout.addWidget(self.button3)

        self.label3 = QLabel("<b><i>А кто нарвится тебе?</i></b>", self)
        self.label3.setFont(fontlabel34)
        self.label3.setStyleSheet("color: blue")
        self.label3.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label3)

        twoHBox = QHBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Введите название любимого животного")
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.returnPressed.connect(self.create_text_metka_1)
        twoHBox.addWidget(self.line_edit)

        self.button4 = QPushButton("Очистить поле")
        self.button4.clicked.connect(self.button4action)
        twoHBox.addWidget(self.button4)

        layout.addLayout(twoHBox)

        self.label4 = QLabel("", self)
        self.label4.setFont(font2)
        self.label4.setStyleSheet("color: green")
        self.label4.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label4)

        self.label5 = QLabel("<b><i>Опиши какие они.</i></b>", self)
        self.label5.setFont(fontlabel34)
        self.label5.setStyleSheet("color: blue")
        self.label5.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label5)

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setPlaceholderText("Введите описание любимого животного")
        self.line_edit2.returnPressed.connect(self.create_text_metka_2)
        self.line_edit2.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.line_edit2)

        self.label6 = QLabel("", self)
        self.label6.setFont(font2)
        self.label6.setStyleSheet("color: green")
        self.label6.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label6)

        ThreeHBox = QHBoxLayout()

        self.button5 = QPushButton("Закрыть приложеине", self)
        self.button5.clicked.connect(self.close)
        ThreeHBox.addWidget(self.button5)

        self.button6 = QPushButton("Открыть новое окно", self)
        self.button6.clicked.connect(self.button6action)
        ThreeHBox.addWidget(self.button6)

        layout.addLayout(ThreeHBox)

        layout.addStretch()
        self.central_widget.setLayout(layout)

        self.image_label = None
        self.image_label2 = None
    def button1action(self):
        image_cat1 = os.path.join(os.path.dirname(__file__), "cat1.png")
        pixmap1 = QPixmap(image_cat1)

        if self.image_label is None:
            self.image_label = QLabel(self)
            self.image_label.setPixmap(pixmap1.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.setAlignment(Qt.AlignCenter)
            self.lay1.insertWidget(2, self.image_label)
        else:
            self.image_label.setPixmap(pixmap1.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
    def button2action(self):
        image_cat2 = os.path.join(os.path.dirname(__file__), "cat2.png")
        pixmap2 = QPixmap(image_cat2)

        if self.image_label2 is None:
            self.image_label2 = QLabel(self)
            self.image_label2.setPixmap(pixmap2.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label2.setAlignment(Qt.AlignCenter)
            self.lay2.insertWidget(2, self.image_label2)
        else:
            self.image_label2.setPixmap(pixmap2.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
    def button3action(self):
        if self.image_label is not None:
            self.image_label.deleteLater()
            self.image_label = None
            
        if self.image_label2 is not None:
            self.image_label2.deleteLater()
            self.image_label2 = None
        
    def create_text_metka_1(self):
        new_text = self.line_edit.text()
        self.line_edit.clear()
        self.label4.setText(f"<u>{new_text}</u>")

    def button4action(self):
        self.label4.setText("")

    def create_text_metka_2(self):
        new_text2 = self.line_edit2.text()
        self.line_edit2.clear()
        self.label6.setText(f"<u>{new_text2}</u>")
    
    def button6action(self):
        self.second_window = SecondWindows()
        self.second_window.show()

class SecondWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Это я придумал сам")
        self.setGeometry(650, 300, 700, 200)

        layout = QVBoxLayout()

        font = QFont("Arial", 22)
        font2 = QFont("Calibri", 17)
        font3 = QFont("Times", 23)
        font4 = QFont("Sans", 19)

        self.label1 = QLabel("<b>А еще я люблю: Собак, Хомяков, и Манки</b>")
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: rgb(128, 0, 128)")
        self.label1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label1)
        HBoxLayout = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        self.label11 = QLabel("")
        self.label11.setFont(font2)
        self.label11.setStyleSheet("color: blue")
        self.label11.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.label11)

        image_path1 = os.path.join(os.path.dirname(__file__), "dogsecondwindows.png") 
        pixmap11 = QPixmap(image_path1)
        self.image_label1 = QLabel(self)
        self.image_label1.setPixmap(pixmap11.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label1.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.image_label1)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Введите имя")
        self.line_edit.setStyleSheet("background-color: red; color: white")
        self.line_edit.setFont(font2)
        self.line_edit.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.line_edit)



        self.label12 = QLabel("")
        self.label12.setFont(font3)
        self.label12.setStyleSheet("color: orange")
        self.label12.setAlignment(Qt.AlignCenter)
        layout2.addWidget(self.label12)

        image_path2 = os.path.join(os.path.dirname(__file__), "humstersecondwindows.png") 
        pixmap12 = QPixmap(image_path2)
        self.image_label2 = QLabel(self)
        self.image_label2.setPixmap(pixmap12.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label2.setAlignment(Qt.AlignCenter)
        layout2.addWidget(self.image_label2)

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setPlaceholderText("Введите имя")
        self.line_edit1.setStyleSheet("background-color: green; color: black")
        self.line_edit1.setFont(font2)
        self.line_edit1.setAlignment(Qt.AlignCenter)
        layout2.addWidget(self.line_edit1)



        self.label13 = QLabel("")
        self.label13.setFont(font4)
        self.label13.setStyleSheet("color: pink")
        self.label13.setAlignment(Qt.AlignCenter)
        layout3.addWidget(self.label13)

        image_path3 = os.path.join(os.path.dirname(__file__), "monkeysecondwindows.png") 
        pixmap13 = QPixmap(image_path3)
        self.image_label3 = QLabel(self)
        self.image_label3.setPixmap(pixmap13.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label3.setAlignment(Qt.AlignCenter)
        layout3.addWidget(self.image_label3)

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setPlaceholderText("Введите имя")
        self.line_edit2.setStyleSheet("background-color: black; color: white")
        self.line_edit2.setFont(font2)
        self.line_edit2.setAlignment(Qt.AlignCenter)
        layout3.addWidget(self.line_edit2)


        HBoxLayout.addLayout(layout1)
        HBoxLayout.addLayout(layout2)
        HBoxLayout.addLayout(layout3)
        layout.addLayout(HBoxLayout)

        self.button1 = QPushButton("Назвать питомцев", self)
        self.button1.setStyleSheet("""
                                   background-color: yellow; 
                                   color: black; border-radius: 15px; 
                                   padding-top: 15px; 
                                   padding-bottom: 15px; 
                                   font-size: 200%; 
                                   margin-left: 130px; 
                                   margin-right: 130px
                                   """)
        self.button1.clicked.connect(self.button1action)
        self.button1.setFont(QFont("Arial", 20))
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Закрыть приложение", self) 
        self.button2.setStyleSheet("""
                                   background-color: red; 
                                   color: white; border-radius: 15px; 
                                   padding-top: 15px; 
                                   padding-bottom: 15px; 
                                   font-size: 200%; 
                                   margin-left: 180px; 
                                   margin-right: 180px;
                                   
                                   """)
        self.button2.clicked.connect(self.close)
        self.button2.setFont(QFont("Arial", 20))
        layout.addWidget(self.button2)

        self.setLayout(layout)
    def button1action(self):
        new_name1 = self.line_edit.text()
        new_name2 = self.line_edit1.text()
        new_name3 = self.line_edit2.text()

        self.label11.setText(f"<b>{new_name1}</b>")
        self.label12.setText(f"<i>{new_name2}</i>")
        self.label13.setText(f"<u>{new_name3}</u>")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создаем экземпляр QApplication
    mainWindow = MainWindow()  # Создаем экземпляр нашего главного окна
    mainWindow.show()  # Отображаем главное окно
    sys.exit(app.exec_())  # Запускаем главный цикл приложения