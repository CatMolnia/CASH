from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPixmap
from __config import AppWindowConfig, GeneralInformation
import resources_rc

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
        
        # добавляем иконки
        calendar_icon_path = ":/icons/icons/calendar.png"
        work_icon_path = ":/icons/icons/work.png"
        weekend_icon_path = ":/icons/icons/weekend.png"
        
        # добавляем иконки в QPixmap
        calendar_icon = QPixmap(calendar_icon_path)
        work_icon = QPixmap(work_icon_path)
        weekend_icon = QPixmap(weekend_icon_path)
        
        # если иконки не пустые, то добавляем их в label
        if not calendar_icon.isNull() and not work_icon.isNull() and not weekend_icon.isNull():
            # Сохраняем оригинальный текст
            original_text = widget.ui.label_calendar.text()
            original_work_text = widget.ui.label_work.text()
            original_weekend_text = widget.ui.label_weekend.text()
            
            # Создаем HTML с иконкой и текстом (иконка слева, текст по центру)
            icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{calendar_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_text}</td></tr></table>'
            work_icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{work_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_work_text}</td></tr></table>'
            weekend_icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{weekend_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_weekend_text}</td></tr></table>'
            
            # применяем HTML к label
            widget.ui.label_calendar.setText(icon_html)
            widget.ui.label_work.setText(work_icon_html)
            widget.ui.label_weekend.setText(weekend_icon_html)
        
        # выравниваем по левому краю
        widget.ui.label_calendar.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        widget.ui.label_work.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        widget.ui.label_weekend.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        
        # применяем стили к label
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