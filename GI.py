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
        sizes = self.config.sizes
        size_key = self.config.default_size
        width, height = sizes.get(size_key, next(iter(sizes.values())))
        widget.resize(width, height)

        # _________________________________general_information_________________________________
        # виджет general_information - применяем стили и эффект тени
        gi_config = self.general_information.general_information
        widget.ui.general_information.setStyleSheet(gi_config["style"])
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = gi_config["shadow"]
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(shadow_params["blur_radius"])
        shadow.setXOffset(shadow_params["x_offset"])
        shadow.setYOffset(shadow_params["y_offset"])
        shadow.setColor(QColor(*shadow_params["color"]))
        widget.ui.general_information.setGraphicsEffect(shadow)
        
        # label
        widget.ui.label_title.setStyleSheet(self.general_information.label_title)
        widget.ui.label_calendar.setStyleSheet(self.general_information.label_calendar)
        widget.ui.label_work.setStyleSheet(self.general_information.label_work)
        widget.ui.label_weekend.setStyleSheet(self.general_information.label_weekend)
        
        # lineEdit
        widget.ui.lineEdit_calendar.setReadOnly(True) # отключаем редактирование на lineEdit_calendar
        widget.ui.lineEdit_calendar.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на lineEdit_calendar
        widget.ui.lineEdit_weekend.setReadOnly(True)
        widget.ui.lineEdit_weekend.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        widget.ui.lineEdit_work.setReadOnly(True)
        widget.ui.lineEdit_work.setFocusPolicy(Qt.FocusPolicy.NoFocus)