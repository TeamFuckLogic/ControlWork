import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from funnyjoke import JokeWindow
from musiclist import MusicWindow

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Чат-бот")
        self.setGeometry(100, 100, 300, 200)

        # Центральный виджет и layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Кнопка для анекдотов
        joke_button = QPushButton("Анекдоты")
        joke_button.clicked.connect(self.open_joke_window)
        layout.addWidget(joke_button)

        # Кнопка для музыки
        music_button = QPushButton("Рекомендации музыки")
        music_button.clicked.connect(self.open_music_window)
        layout.addWidget(music_button)

        self.joke_window = None
        self.music_window = None

    def open_joke_window(self):
        if self.joke_window is None:
            self.joke_window = JokeWindow()
        self.joke_window.show()

    def open_music_window(self):
        if self.music_window is None:
            self.music_window = MusicWindow()
        self.music_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = MainMenu()
    menu.show()
    sys.exit(app.exec_())