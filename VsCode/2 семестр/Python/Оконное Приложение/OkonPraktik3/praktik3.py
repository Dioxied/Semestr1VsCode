import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QCheckBox, QSpinBox, QVBoxLayout)
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QFileDialog

from PyQt5.QtGui import QFont 
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import Qt 
import os 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Анкета питомца")
        self.setGeometry(200, 80, 600, 800)

        font = QFont("Arial", 12)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.horbox1 = QHBoxLayout()

        image_cat = os.path.join(os.path.dirname(__file__), "cat2.png")
        pixmap1 = QPixmap(image_cat)
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap1.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image_label.setAlignment(Qt.AlignLeft)
        self.image_label.setStyleSheet("margin: 15px; border: 3px solid yellow; border-radius: 10px")
        self.horbox1.addWidget(self.image_label)

        self.lay1 = QVBoxLayout()
        self.label1 = QLabel("Кличка вашего питомца")
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignCenter)
        self.lay1.addWidget(self.label1)

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setPlaceholderText("Здеся")
        self.line_edit1.setFont(font)
        self.line_edit1.setAlignment(Qt.AlignCenter)
        self.lay1.addWidget(self.line_edit1)

        self.label2 = QLabel("Сколько лет вашему питомцу")
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)
        self.lay1.addWidget(self.label2)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 100)
        self.spin_box.setAlignment(Qt.AlignCenter)
        self.lay1.addWidget(self.spin_box)
        

        self.label3 = QLabel("Какой у вас домашний питомец")
        self.label3.setFont(font)
        self.label3.setAlignment(Qt.AlignCenter)
        self.lay1.addWidget(self.label3)

        self.combo_box = QComboBox()
        self.combo_box.addItem("Сабака")
        self.combo_box.addItem("Кит маму мав")
        self.combo_box.addItem("Манки")
        self.combo_box.addItem("Крокодил")
        self.lay1.addWidget(self.combo_box)

        self.button2 = QPushButton("Загрузить фото")
        self.button2.clicked.connect(self.load_file)

        self.lay1.addWidget(self.button2)

        self.horbox1.addLayout(self.lay1)
        layout.addLayout(self.horbox1)

        self.horbox2 = QHBoxLayout()
        self.label4 = QLabel("Виберите, какие обследования хотите провести:")
        self.label4.setFont(font)
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setStyleSheet("margin-top: 40px")
        layout.addWidget(self.label4)

        self.check_box1 = QCheckBox("Осмотр")
        self.check_box1.setFont(font)
        self.check_box2 = QCheckBox("Массаж")
        self.check_box2.setFont(font)
        self.check_box3 = QCheckBox("Прививка")
        self.check_box3.setFont(font)
        self.check_box4 = QCheckBox("Кострация")
        self.check_box4.setFont(font)
        self.horbox2.addWidget(self.check_box1)
        self.horbox2.addWidget(self.check_box2)
        self.horbox2.addWidget(self.check_box3)
        self.horbox2.addWidget(self.check_box4)
        layout.addLayout(self.horbox2)

        self.label5 = QLabel("Расскажите немножко о своем питомце:")
        self.label5.setFont(font)
        self.label5.setAlignment(Qt.AlignCenter)
        self.label5.setStyleSheet("margin-top: 40px")
        layout.addWidget(self.label5)

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setPlaceholderText("Тут пиши жи ес")
        self.line_edit1.setStyleSheet("height: 200px; margin-left: 10px; margin-right: 10px; padding: 10px")
        layout.addWidget(self.line_edit1)

        self.button = QPushButton("Сохранить анкету")
        self.button.setStyleSheet("""
                                  width: 300px; 
                                  height: 100px; 
                                  font-size: 50px; 
                                  border: 4px solid green; 
                                  margin-top: 40px;
                                  """)
        self.button.clicked.connect(self.close)
        layout.addWidget(self.button)

        layout.addStretch()
        self.central_widget.setLayout(layout)
    

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Выберите файл',
            '', 
            'Все файлы (*);;Текстовые файлы (*.txt);;Изображения (*.png *.jpg)'
        )
        try:
            self.horbox1.removeWidget(self.image_label)
            image_cat = os.path.join(os.path.dirname(__file__), file_path)
            pixmap1 = QPixmap(image_cat)
            self.image_label = QLabel(self)
            self.image_label.setPixmap(pixmap1.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.setAlignment(Qt.AlignLeft)
            self.image_label.setStyleSheet("margin: 15px; border: 3px solid yellow; border-radius: 10px")
            self.horbox1.insertWidget(0, self.image_label)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow() 
    mainWindow.show()  
    sys.exit(app.exec_()) 