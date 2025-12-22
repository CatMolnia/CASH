import sys

# импорт пакетов
from PyQt6.QtWidgets import QApplication, QWidget

# импорт UI
from cash import Ui_CASH

# импорт модулей
from GI import StartWindow
from __config import AppWindowConfig, GeneralInformation, SecondaryInformation, WidgetDaysZp, WidgetDaysAvans, WidgetDaysZpAvans, WidgetTableZP, WidgetTableAvans, WidgetCalendar

class Cash(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CASH()
        self.ui.setupUi(self)

        self._init_components()

    def _init_components(self):
        config = AppWindowConfig() # конфиг из конфига
        general_information = GeneralInformation() # конфиг из конфига
        secondary_information = SecondaryInformation() # конфиг из конфига
        widget_days_zp = WidgetDaysZp() # конфиг из конфига
        widget_days_avans = WidgetDaysAvans() # конфиг из конфига
        widget_days_zp_avans = WidgetDaysZpAvans() # конфиг из конфига
        widget_table_zp = WidgetTableZP() # конфиг из конфига
        widget_table_avans = WidgetTableAvans() # конфиг из конфига
        widget_calendar = WidgetCalendar() # конфиг из конфига
        
        self.ui_manager = StartWindow(config, general_information, secondary_information, widget_days_zp, widget_days_avans, widget_days_zp_avans, widget_table_zp, widget_table_avans, widget_calendar) # применяем стили к окну
        self.ui_manager.apply(self) # применяем стили к окну

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cash()
    window.show()
    sys.exit(app.exec())