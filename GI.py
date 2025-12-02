from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from __config import AppWindowConfig, GeneralInformation

class StartWindow:
    def __init__(self, config: AppWindowConfig, general_information: GeneralInformation):
        self.config = config
        self.general_information = general_information

    def apply(self, widget: QWidget):
        # _________________________________CASH_________________________________
        sizes = self.config.sizes # размеры из конфига
        size_key = self.config.default_size # ключ из конфига
        width, height = sizes.get(size_key, next(iter(sizes.values()))) # размеры из конфига
        widget.resize(width, height) # изменяем размер окна

        # _________________________________general_information_________________________________
        # виджет general_information - применяем стили и эффект тени
        gi_config = self.general_information.general_information # конфиг из конфига
        widget.ui.general_information.setStyleSheet(gi_config["style"]) # применяем стиль к виджету general_information
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = gi_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        widget.ui.general_information.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету general_information
        
        # label
        widget.ui.label_title.setStyleSheet(self.general_information.label_title) # применяем стиль к label_title
        widget.ui.label_calendar.setStyleSheet(self.general_information.label_calendar) # применяем стиль к label_calendar
        widget.ui.label_work.setStyleSheet(self.general_information.label_work) # применяем стиль к label_work
        widget.ui.label_weekend.setStyleSheet(self.general_information.label_weekend) # применяем стиль к label_weekend
        
        # lineEdit
        widget.ui.lineEdit_calendar.setReadOnly(True) # отключаем редактирование на lineEdit_calendar
        widget.ui.lineEdit_calendar.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на lineEdit_calendar
        widget.ui.lineEdit_weekend.setReadOnly(True)
        widget.ui.lineEdit_weekend.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        widget.ui.lineEdit_work.setReadOnly(True)
        widget.ui.lineEdit_work.setFocusPolicy(Qt.FocusPolicy.NoFocus)