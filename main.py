import sys

# импорт пакетов
from PyQt6.QtWidgets import QApplication, QWidget

# импорт UI
from cash import Ui_CASH

# импорт модулей
from GI import StartWindow
from __config import (AppWindowConfig, GeneralInformation, SecondaryInformation,
                      WidgetDaysZp, WidgetDaysAvans, WidgetDaysZpAvans, 
                      WidgetTableZP, WidgetTableAvans, WidgetCalendar)

class Cash(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_CASH() # подгружаем UI
        self.ui.setupUi(self) # применяем UI к окну

        self._init_components() # инициализируем компоненты

    # подгружаем конфиги
    def _init_components(self):
        config = AppWindowConfig()
        general_information = GeneralInformation()
        secondary_information = SecondaryInformation()
        widget_days_zp = WidgetDaysZp()
        widget_days_avans = WidgetDaysAvans()
        widget_days_zp_avans = WidgetDaysZpAvans()
        widget_table_zp = WidgetTableZP()
        widget_table_avans = WidgetTableAvans()
        widget_calendar = WidgetCalendar()
        
        # применяем стили к окну
        self.ui_manager = StartWindow(config, general_information, secondary_information,
                                      widget_days_zp, widget_days_avans, widget_days_zp_avans,
                                      widget_table_zp, widget_table_avans, widget_calendar) # применяем стили к окну
        
        self.ui_manager.apply(self) # применяем стили к окну

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    window = Cash()
    window.show()
    sys.exit(app.exec())