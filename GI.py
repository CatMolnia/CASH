from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QPixmap
from __config import AppWindowConfig, GeneralInformation, SecondaryInformation, WidgetDaysZp, WidgetDaysAvans
import resources_rc

class StartWindow:
    def __init__(self, 
                config: AppWindowConfig,
                general_information: GeneralInformation,
                secondary_information: SecondaryInformation,
                widget_days_zp: WidgetDaysZp,
                widget_days_avans: WidgetDaysAvans):
        
        self.config = config # конфиг из конфига
        self.general_information = general_information # конфиг из конфига
        self.secondary_information = secondary_information # конфиг из конфига
        self.widget_days_zp = widget_days_zp # конфиг из конфига
        self.widget_days_avans = widget_days_avans # конфиг из конфига

    # применяем стили к окну
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
        
        # применяем стили:
        # к label
        widget.ui.label_title.setStyleSheet(self.general_information.label_title) # применяем стиль к label_title
        widget.ui.label_calendar.setStyleSheet(self.general_information.label_calendar) # применяем стиль к label_calendar
        widget.ui.label_work.setStyleSheet(self.general_information.label_work) # применяем стиль к label_work
        widget.ui.label_weekend.setStyleSheet(self.general_information.label_weekend) # применяем стиль к label_weekend
        # к lineEdit
        widget.ui.lineEdit_calendar.setStyleSheet(self.general_information.lineEdit_calendar) # применяем стиль к lineEdit_calendar
        widget.ui.lineEdit_work.setStyleSheet(self.general_information.lineEdit_work) # применяем стиль к lineEdit_work
        widget.ui.lineEdit_weekend.setStyleSheet(self.general_information.lineEdit_weekend) # применяем стиль к lineEdit_weekend
        
        widget.ui.lineEdit_calendar.setReadOnly(True) # отключаем редактирование на lineEdit_calendar
        widget.ui.lineEdit_weekend.setReadOnly(True) # отключаем редактирование на lineEdit_weekend
        widget.ui.lineEdit_work.setReadOnly(True) # отключаем редактирование на lineEdit_work

        widget.ui.lineEdit_calendar.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на lineEdit_calendar
        widget.ui.lineEdit_weekend.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на lineEdit_weekend
        widget.ui.lineEdit_work.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на lineEdit_work

        widget.ui.lineEdit_calendar.setMaximumSize(QSize(40, 16777215)) # увеличиваем максимальный размер lineEdit_calendar
        widget.ui.lineEdit_weekend.setMaximumSize(QSize(40, 16777215)) # увеличиваем максимальный размер lineEdit_weekend
        widget.ui.lineEdit_work.setMaximumSize(QSize(40, 16777215)) # увеличиваем максимальный размер lineEdit_work

        # _________________________________secondary_information_________________________________
        
        # виджет secondary_information - применяем стили и эффект тени
        si_config = self.secondary_information.secondary_information # конфиг из конфига
        widget.ui.secondary_information.setStyleSheet(si_config["style"]) # применяем стиль к виджету secondary_information
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = si_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        widget.ui.secondary_information.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету secondary_information

        widget.ui.spinBox_zp.setReadOnly(False) # оставлем редактирование на spinBox_zp
        widget.ui.spinBox_zp.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на spinBox_zp
        widget.ui.spinBox_avans.setReadOnly(False) # оставлем редактирование на spinBox_avans
        widget.ui.spinBox_avans.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на spinBox_avans

        widget.ui.spinBox_zp.setMinimum(1) # устанавливаем минимальное значение 1
        widget.ui.spinBox_zp.setMaximum(31) # устанавливаем максимальное значение 31
        widget.ui.spinBox_avans.setMinimum(1) # устанавливаем минимальное значение 1
        widget.ui.spinBox_avans.setMaximum(31) # устанавливаем максимальное значение 31

        zp_icon_path = ":/icons/icons/zp.png"
        avans_icon_path = ":/icons/icons/avans.png"

        zp_icon = QPixmap(zp_icon_path)
        avans_icon = QPixmap(avans_icon_path)

        if not zp_icon.isNull() and not avans_icon.isNull():
            # Сохраняем оригинальный текст
            original_zp_text = widget.ui.label_day_zp.text()
            original_avans_text = widget.ui.label_day_avans.text()
            
            # Создаем HTML с иконкой и текстом (иконка слева, текст по центру)
            zp_icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{zp_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_zp_text}</td></tr></table>'
            avans_icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{avans_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_avans_text}</td></tr></table>'
            
            # применяем HTML к label
            widget.ui.label_day_zp.setText(zp_icon_html)
            widget.ui.label_day_avans.setText(avans_icon_html)

        # выравниваем по левому краю
        widget.ui.label_day_zp.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        widget.ui.label_day_avans.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        
        # применяем стили:
        # к label
        widget.ui.label_day_zp.setStyleSheet(self.secondary_information.label_day_zp) # применяем стиль к label_day_zp
        widget.ui.label_day_avans.setStyleSheet(self.secondary_information.label_day_avans) # применяем стиль к label_day_avans
        # к spinBox
        widget.ui.spinBox_zp.setStyleSheet(self.secondary_information.spinBox_zp) # применяем стиль к label_day_zp
        widget.ui.spinBox_avans.setStyleSheet(self.secondary_information.spinBox_avans) # применяем стиль к label_day_zp
        widget.ui.spinBox_zp.setMinimumSize(QSize(55, 16777215))
        widget.ui.spinBox_avans.setMinimumSize(QSize(55, 16777215))

        # _________________________________widget_days_zp_________________________________
        
        # виджет secondary_information - применяем стили и эффект тени
        dz_config = self.widget_days_zp.widget_days_zp # конфиг из конфига
        widget.ui.widget_days_zp.setStyleSheet(dz_config["style"]) # применяем стиль к виджету widget_days_zp
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = dz_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        widget.ui.widget_days_zp.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету widget_days_zp

        widget.ui.tableWidget_zp.setStyleSheet(self.widget_days_zp.tableWidget_zp) # применяем стиль к виджету widget_days_zp

        # _________________________________widget_days_avans_________________________________
        
        # виджет widget_days_avans - применяем стили и эффект тени
        da_config = self.widget_days_avans.widget_days_avans # конфиг из конфига
        widget.ui.widget_days_avans.setStyleSheet(da_config["style"]) # применяем стиль к виджету widget_days_avans
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = da_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        widget.ui.widget_days_avans.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету widget_days_avans

        widget.ui.tableWidget_avans.setStyleSheet(self.widget_days_avans.tableWidget_avans) # применяем стиль к виджету widget_days_