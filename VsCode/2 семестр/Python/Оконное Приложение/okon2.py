import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Самсонов Александр Максимович 04.09.2006")

        self.setGeometry(100, 200, 900, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        hbox_layout1 = QHBoxLayout()
        hbox_layout2 = QHBoxLayout()

        self.label1 = QLabel("Бердюжье нече такой", self)
        self.label2 = QLabel("Лето", self)
        self.label3 = QLabel("Смотри что я умею Никита", self)
        
        font = QFont("Arial", 16, QFont.Bold)
        self.label1.setFont(font)
        self.label2.setFont(font)
        self.label3.setFont(font)



        self.open_new_button = QPushButton("Открытие нового окна", self)
        self.open_new_button.clicked.connect(self.open_second_window)
        self.close_button = QPushButton("Закрыть приложение", self)
        self.close_button.clicked.connect(self.close)
        

        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3.setAlignment(Qt.AlignCenter)
        
        hbox_layout1.addWidget(self.label1)
        hbox_layout1.addWidget(self.label2)

        layout.addLayout(hbox_layout1)
   
        hbox_layout2.addWidget(self.close_button)
        hbox_layout2.addWidget(self.open_new_button)
        layout.addLayout(hbox_layout2)
        layout.addWidget(self.label3)


        layout.addStretch()
        self.central_widget.setLayout(layout)
        


    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Книга братан")
        self.setGeometry(900, 200, 400, 300)
        
        layout = QVBoxLayout()
        self.label = QLabel("Смотри что я могу", self)
        font = QFont("Arial", 16, QFont.Bold)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.close_button = QPushButton("Закрыть приложение", self)
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.label)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
