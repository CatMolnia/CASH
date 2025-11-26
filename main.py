import sys

from PyQt6.QtWidgets import QApplication, QWidget

from cash import Ui_CASH
from __config import AppWindowConfig, GeneralInformation

class Cash(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CASH()
        self.ui.setupUi(self)

        self.config = AppWindowConfig() # config - конфигурация окна
        self.general_information = GeneralInformation() # general_information - конфигурация для general_information

        self.start_window = StartWindow(self.config, self.general_information) # StartWindow - класс для создания окна начала работы
        self.start_window.apply(self) # apply - метод для применения настроек к окну

class StartWindow:
    def __init__(self, config: AppWindowConfig, general_information: GeneralInformation):
        self.config = config
        self.general_information = general_information

    def apply(self, widget: QWidget):
        # размер окна
        sizes = self.config.sizes
        size_key = self.config.default_size
        width, height = sizes.get(size_key, next(iter(sizes.values())))
        widget.resize(width, height)

        # general_information
        widget.ui.label_title.setStyleSheet(self.general_information.label_title)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cash()
    window.show()
    sys.exit(app.exec())