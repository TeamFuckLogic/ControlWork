from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
from jokes import JOKES
import random

class JokeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бот с анекдотами")
        self.setGeometry(150, 150, 400, 500)

        # Центральный виджет и layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Поле для отображения чата
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.append("<b>Бот:</b> Расскажи, хочешь анекдот?")
        layout.addWidget(self.chat_display)

        # Поле ввода и кнопка
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        input_layout.addWidget(self.input_field)

        send_button = QPushButton("Отправить")
        send_button.clicked.connect(self.handle_message)
        input_layout.addWidget(send_button)

        layout.addLayout(input_layout)

    def handle_message(self):
        user_text = self.input_field.text().strip().lower()
        if user_text:
            self.chat_display.append(f"<b>Ты:</b> {user_text}")
            if any(word in user_text for word in ["анекдот", "шутка", "расскажи", "смешно"]):
                joke = random.choice(JOKES)
                self.chat_display.append(f"<b>Бот:</b> {joke}")
            else:
                self.chat_display.append(f"<b>Бот:</b> Скажи что-то вроде 'расскажи анекдот'!")
            self.input_field.clear()