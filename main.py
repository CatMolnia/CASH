import sys

# импорт пакетов
from PyQt6.QtWidgets import QApplication, QWidget

# импорт UI
from cash import Ui_CASH

# импорт модулей
from GI import StartWindow
from __config import AppWindowConfig, GeneralInformation


class Cash(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CASH()
        self.ui.setupUi(self)

        self._init_components()

    def _init_components(self):
        config = AppWindowConfig()
        general_information = GeneralInformation()
        
        self.ui_manager = StartWindow(config, general_information)
        self.ui_manager.apply(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cash()
    window.show()
    sys.exit(app.exec())