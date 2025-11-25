import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt

from cash import Ui_CASH
from __config import AppWindowConfig, get_window_config

class Cash(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CASH()
        self.ui.setupUi(self)

        self.config = get_window_config() # get_window_config - функция для получения конфигурации
        self.start_window = StartWindow(self.config) # StartWindow - класс для создания окна начала работы
        self.start_window.apply(self) # apply - метод для применения настроек к текущему окну

class StartWindow:
    def __init__(self, config: AppWindowConfig):
        self.config = config

    def apply(self, widget: QWidget):
        width, height = self.config.MAIN_WINDOW_SIZE
        widget.resize(width, height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cash()
    window.show()
    sys.exit(app.exec())