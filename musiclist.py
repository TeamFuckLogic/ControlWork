from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QTextEdit, QLabel
from music import MUSIC_DB

class MusicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бот с музыкой")
        self.setGeometry(150, 150, 400, 500)

        # Влияние погоды на выбор (модификатор)
        self.weather_modifiers = {
            "солнечно": ["веселое", "энергичное"],
            "дождливо": ["грустное", "веселое"],
            "облачно": ["грустное", "энергичное"],
            "снежно": ["грустное", "веселое"],
            "любая": ["веселое", "грустное", "энергичное"]
        }

        # Центральный виджет и layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Выпадающий список для жанра
        layout.addWidget(QLabel("Выберите жанр:"))
        self.genre_combo = QComboBox()
        self.genre_combo.addItems(MUSIC_DB.keys())
        layout.addWidget(self.genre_combo)

        # Выпадающий список для настроения
        layout.addWidget(QLabel("Выберите настроение:"))
        self.mood_combo = QComboBox()
        self.mood_combo.addItems(["веселое", "грустное", "энергичное"])
        layout.addWidget(self.mood_combo)

        # Выпадающий список для погоды
        layout.addWidget(QLabel("Выберите погоду (не обязательно):"))
        self.weather_combo = QComboBox()
        self.weather_combo.addItems(["любая", "солнечно", "дождливо", "облачно", "снежно"])
        layout.addWidget(self.weather_combo)

        # Кнопка для рекомендации
        recommend_button = QPushButton("Получить рекомендацию")
        recommend_button.clicked.connect(self.recommend_music)
        layout.addWidget(recommend_button)

        # Поле для вывода результата
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.append("Выберите критерии и нажмите 'Получить рекомендацию'!")
        layout.addWidget(self.result_display)

    def recommend_music(self):
        genre = self.genre_combo.currentText()
        mood = self.mood_combo.currentText()
        weather = self.weather_combo.currentText()

        # Проверяем, подходит ли настроение под погоду
        if weather != "любая" and mood not in self.weather_modifiers[weather]:
            self.result_display.append(f"Настроение '{mood}' не очень подходит для погоды '{weather}'. Попробуйте другое настроение!")
            return

        # Получаем все подходящие треки
        try:
            tracks = MUSIC_DB[genre][mood]
            if not tracks:
                self.result_display.append("Ошибка: треков для этого сочетания нет в базе.")
                return

            # Формируем пронумерованный список
            self.result_display.append(f"\nПодходящие треки (жанр: {genre}, настроение: {mood}, погода: {weather}):")
            for i, track in enumerate(tracks, 1):
                self.result_display.append(f"{i}. {track}")
        except KeyError:
            self.result_display.append("Ошибка: такого сочетания нет в базе. Попробуйте другие критерии!")