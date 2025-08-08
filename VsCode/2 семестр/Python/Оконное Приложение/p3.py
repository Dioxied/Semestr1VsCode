import sys  # Импортируем системный модуль для работы с аргументами командной строки
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit  # Импортируем QLineEdit для текстового поля
from PyQt5.QtGui import QFont  # Импортируем для работы с шрифтами
from PyQt5.QtGui import QPixmap  # Используется для работы с растровыми изображениями
from PyQt5.QtCore import Qt  # Импортируем Qt для использования перечислений
import os  # Позволяет выполнять различные операции, такие как создание, удаление, перемещение и изменение файлов и каталогов.

class MainWindow(QMainWindow):  # Создаем класс MainWindow, наследуемый от QMainWindow
    def __init__(self):
        super().__init__()  # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("Мое первое приложение на PyQt5")  # Устанавливаем заголовок окна
        self.setGeometry(100, 100, 700, 700)  # Задаем размеры окна (x, y, width(ширина), height(высота))

        self.central_widget = QWidget(self)  # Создаем центральный виджет и устанавливаем его
        self.setCentralWidget(self.central_widget)  # Устанавливаем наш виджет как центральный

        layout = QVBoxLayout()  # Создаем вертикальный компоновщик для размещения элементов

        # Создание нескольких меток с текстами
        self.label1 = QLabel("<b>Добро пожаловать в ваше приложение!</b>", self)  # жирный
        self.label2 = QLabel("<u>Это пример работы с PyQt5.</u>", self)  # подчёркнутый
        self.label3 = QLabel("<i>Нажмите кнопку ниже, чтобы закрыть приложение.</i>", self)  # курсив

        # Установка параметров шрифта (размера и стиля)
        font = QFont("Arial", 16)
        font1 = QFont("Arial", 22)
        self.label1.setFont(font)  # Применяем шрифт к метке
        self.label2.setFont(font1)  # Применяем шрифт к метке

        # Установка цвета шрифта
        self.label1.setStyleSheet("color: blue;")
        self.label2.setStyleSheet("color: rgb(255, 0, 0);")

        self.label1.setAlignment(Qt.AlignCenter)  # по центру
        self.label2.setAlignment(Qt.AlignLeft)  # слева
        self.label3.setAlignment(Qt.AlignRight)  # справа

        layout.addWidget(self.label1)  # Добавляем метки в компоновщик
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)

        # Добавление текстового поля для ввода текста
        self.input_text = QLineEdit(self)  # Создаем текстовое поле для ввода
        self.input_text.setPlaceholderText("Введите текст здесь...")  # Устанавливаем подсказку
        layout.addWidget(self.input_text)  # Добавляем текстовое поле в компоновщик

        # Кнопка для обновления текста метки
        self.update_button = QPushButton("Обновить текст приветствия", self)  # Создаем кнопку для обновления текста метки
        self.update_button.clicked.connect(self.update_text)  # Подключаем кнопку к методу update_text
        layout.addWidget(self.update_button)  # Добавляем кнопку в компоновщик
        
        # Добавление второго текстового поля для ввода
        self.second_input_text = QLineEdit(self)  # Создаем второе текстовое поле для ввода
        self.second_input_text.setPlaceholderText("Введите текст для новой метки...")  # Устанавливаем подсказку
        layout.addWidget(self.second_input_text)  # Добавляем второе текстовое поле в компоновщик
        
        # Кнопка для обновления текста новой метки
        self.create_label_button = QPushButton("Создать метку с текстом", self)  # Создаем кнопку для создания новой метки
        self.create_label_button.clicked.connect(self.create_new_label)  # Подключаем кнопку к методу create_new_label
        layout.addWidget(self.create_label_button)  # Добавляем кнопку в компоновщик

        # Создание метки для отображения нового текста
        self.new_label = QLabel("", self)  # Изначально пустая метка для новой строки текста
        layout.addWidget(self.new_label)  # Добавляем новую метку в компоновщик (после кнопки)

        # Кнопка для открытия конкретного изображения
        self.open_image_button = QPushButton("Открыть изображение 'cat'", self) 
        self.open_image_button.clicked.connect(self.open_image)  # Подключаем кнопку к методу open_image
        layout.addWidget(self.open_image_button)

        # Кнопка для закрытия изображения
        self.close_image_button = QPushButton("Закрыть изображение", self)
        self.close_image_button.clicked.connect(self.close_image)  # Подключаем кнопку к методу close_image
        layout.addWidget(self.close_image_button)

        # Создание кнопки для закрытия приложения
        self.close_button = QPushButton("Закрыть приложение", self)
        self.close_button.clicked.connect(self.close)  # Подключаем кнопку к методу close

        # Кнопка для открытия нового окна
        self.open_window_button = QPushButton("Открыть новое окно", self)
        self.open_window_button.clicked.connect(self.open_second_window)  # Подключаем кнопку к методу открытия окна

        hbox_layout = QHBoxLayout()  # Создаем горизонтальный компоновщик
        hbox_layout.addWidget(self.close_button)  # Добавляем кнопку в компоновщик
        hbox_layout.addWidget(self.open_window_button)  # Добавляем кнопку в компоновщик

        layout.addLayout(hbox_layout)  # Добавляем горизонтальный компоновщик в вертикальный
        layout.addStretch()  # Добавляет растяжимое пространство

        self.central_widget.setLayout(layout)  # Это позволяет кнопке находиться внизу

        # Метка для изображения (изначально скрыта)
        self.image_label = None

    def update_text(self):
        """Метод для обновления текста метки с приветствием."""
        new_text = self.input_text.text()  # Получаем текст из текстового поля (input_text - название которое мы задали выше)
        # Метод .text() возвращает строку, которая в данный момент введена в это текстовое поле.
        self.label1.setText(f"<b>{new_text}</b>")  # Обновляем метку с приветствием новым текстом

    def create_new_label(self):
        """Метод для создания новой метки с текстом из второго текстового поля."""
        new_label_text = self.second_input_text.text()  # Получаем текст из второго текстового поля
        if self.new_label is not None:
            self.new_label.setText(new_label_text)  # Обновляем текст новой метки
            # Если нужно, можно также установить какие-либо стили здесь
        # Если нужно скрыть пустую метку, например, при пустом вводе
        if new_label_text == "":
            self.new_label.setText("")  # Очищаем метку, если текст пустой

    def open_image(self):
        """Метод для открытия конкретного изображения."""
        image_path = os.path.join(os.path.dirname(__file__), "image.png")  # Замените на 'cat.jpg', если у вас файл с таким расширением
        pixmap1 = QPixmap(image_path)  # Загружаем изображение

        # Если метка изображения еще не создана, создаем её
        if self.image_label is None:
            self.image_label = QLabel(self)
            self.image_label.setPixmap(pixmap1.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.setAlignment(Qt.AlignCenter)
            self.central_widget.layout().insertWidget(2, self.image_label)  # Вставляем после label2
        else:
            # Если изображение уже открыто, обновляем его
            self.image_label.setPixmap(pixmap1.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def close_image(self):
        """Метод для закрытия изображения."""
        if self.image_label is not None:
            self.image_label.deleteLater()  # Удаляем метку
            self.image_label = None  # Сбрасываем ссылку на метку

    def open_second_window(self):
        self.second_window = SecondWindow()  # Создаем экземпляр второго окна
        self.second_window.show()  # Показываем второе окно

# Новый класс для второго окна
class SecondWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно")  # Устанавливаем заголовок окна
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()  # Создаем вертикальный компоновщик
        self.label = QLabel("<i>Это второе окно приложения!</i>", self)  # Пример курсивного текста во втором окне
        layout.addWidget(self.label)
        self.setLayout(layout)  # Устанавливаем созданный компоновщик как layout для текущего окна

# Основная часть запуска приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создаем экземпляр QApplication
    mainWindow = MainWindow()  # Создаем экземпляр нашего главного окна
    mainWindow.show()  # Отображаем главное окно
    sys.exit(app.exec_())  # Запускаем главный цикл приложения

