import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выполнил Сысоев Илья Сергеевич")
        self.setGeometry(600, 300, 500, 500)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        self.label1 = QLabel("Группа: ИСиП 24-11", self)
        self.label2 = QLabel("Возраст: 18", self) 
        self.label3 = QLabel("Мое любимое животное это кот", self) 
        self.label4 = QLabel("1 победиль, 42 лузера. Я таких ем на завтрак", self)

        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter) 
        self.label3.setAlignment(Qt.AlignCenter) 
        self.label4.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label1) 
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)

        self.close_button = QPushButton("Пока", self)
        self.close_button.clicked.connect(self.close)

        layout.addWidget(self.close_button)
        layout.addWidget(self.label4) 
        
        layout.addStretch()
        self.central_widget.setLayout(layout)
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    mainWindow = MainWindow() 
    mainWindow.show()
    sys.exit(app.exec_()) 
