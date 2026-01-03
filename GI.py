from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QHeaderView, QAbstractItemView, QLineEdit, QStackedLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QPixmap, QIcon, QIntValidator
from MainLogic import CalendarLogic
from __config import (AppWindowConfig, GeneralInformation, SecondaryInformation,
                      WidgetDaysZp, WidgetDaysAvans, WidgetDaysZpAvans,
                      WidgetTableZP, WidgetTableAvans, WidgetCalendar)

import sys
import calendar
import resources_rc

class StartWindow:
    def __init__(self, 
                config: AppWindowConfig,
                general_information: GeneralInformation,
                secondary_information: SecondaryInformation,
                widget_days_zp: WidgetDaysZp,
                widget_days_avans: WidgetDaysAvans,
                widget_days_zp_avans: WidgetDaysZpAvans,
                widget_table_zp: WidgetTableZP,
                widget_table_avans: WidgetTableAvans,
                widget_calendar: WidgetCalendar):
        
        self.calendar = calendar
        
        # присваиваем конфиги
        self.config = config
        self.general_information = general_information
        self.secondary_information = secondary_information
        self.widget_days_zp = widget_days_zp
        self.widget_days_avans = widget_days_avans
        self.widget_days_zp_avans = widget_days_zp_avans
        self.widget_table_zp = widget_table_zp
        self.widget_table_avans = widget_table_avans
        self.widget_calendar = widget_calendar

    # применяем стили к окну
    def apply(self, window: QWidget):

        self.window = window # присваиваем окно
        self.ui = window.ui # присваиваем UI

        # _________________________________CASH_________________________________
        
        sizes = self.config.sizes # размеры из конфига
        size_key = self.config.default_size # ключ из конфига
        width, height = sizes.get(size_key, next(iter(sizes.values()))) # размеры из конфига
        self.window.resize(width, height) # изменяем размер окна

        # _________________________________general_information_________________________________
        
        gi_config = self.general_information.general_information # конфиг из конфига
        self.ui.general_information.setStyleSheet(gi_config["style"]) # применяем стиль к виджету general_information
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = gi_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        self.ui.general_information.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету general_information
        
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
            original_text = self.ui.label_calendar.text()
            original_work_text = self.ui.label_work.text()
            original_weekend_text = self.ui.label_weekend.text()
            
            # Создаем HTML с иконкой и текстом (иконка слева, текст по центру)
            icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{calendar_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_text}</td></tr></table>'
            work_icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{work_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_work_text}</td></tr></table>'
            weekend_icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{weekend_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_weekend_text}</td></tr></table>'
            
            # применяем HTML к label
            self.ui.label_calendar.setText(icon_html)
            self.ui.label_work.setText(work_icon_html)
            self.ui.label_weekend.setText(weekend_icon_html)

        # выравниваем по левому краю
        self.ui.label_calendar.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        self.ui.label_work.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        self.ui.label_weekend.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        
        # применяем стили:
       
        # к label
        self.ui.label_title.setStyleSheet(self.general_information.label_title) # применяем стиль к label_title
        self.ui.label_calendar.setStyleSheet(self.general_information.label_calendar) # применяем стиль к label_calendar
        self.ui.label_work.setStyleSheet(self.general_information.label_work) # применяем стиль к label_work
        self.ui.label_weekend.setStyleSheet(self.general_information.label_weekend) # применяем стиль к label_weekend
       
        # к lineEdit
        self.ui.lineEdit_calendar.setStyleSheet(self.general_information.lineEdit_calendar) # применяем стиль к lineEdit_calendar
        self.ui.lineEdit_work.setStyleSheet(self.general_information.lineEdit_work) # применяем стиль к lineEdit_work
        self.ui.lineEdit_weekend.setStyleSheet(self.general_information.lineEdit_weekend) # применяем стиль к lineEdit_weekend
        
        self.ui.lineEdit_calendar.setReadOnly(True) # отключаем редактирование на lineEdit_calendar
        self.ui.lineEdit_weekend.setReadOnly(True) # отключаем редактирование на lineEdit_weekend
        self.ui.lineEdit_work.setReadOnly(True) # отключаем редактирование на lineEdit_work

        self.ui.lineEdit_calendar.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на lineEdit_calendar
        self.ui.lineEdit_weekend.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на lineEdit_weekend
        self.ui.lineEdit_work.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на lineEdit_work

        self.ui.lineEdit_calendar.setMaximumSize(QSize(40, 16777215)) # увеличиваем максимальный размер lineEdit_calendar
        self.ui.lineEdit_weekend.setMaximumSize(QSize(40, 16777215)) # увеличиваем максимальный размер lineEdit_weekend
        self.ui.lineEdit_work.setMaximumSize(QSize(40, 16777215)) # увеличиваем максимальный размер lineEdit_work

        self.ui.lineEdit_calendar.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter) # выравниваем текст по центру
        self.ui.lineEdit_weekend.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter) # выравниваем текст по центру
        self.ui.lineEdit_work.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter) # выравниваем текст по центру

        # _________________________________secondary_information_________________________________
        
        si_config = self.secondary_information.secondary_information # конфиг из конфига
        self.ui.secondary_information.setStyleSheet(si_config["style"]) # применяем стиль к виджету secondary_information
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = si_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        self.ui.secondary_information.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету secondary_information

        self.ui.spinBox_zp.setReadOnly(False) # оставлем редактирование на spinBox_zp
        self.ui.spinBox_zp.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на spinBox_zp
        self.ui.spinBox_avans.setReadOnly(False) # оставлем редактирование на spinBox_avans
        self.ui.spinBox_avans.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на spinBox_avans

        self.ui.spinBox_zp.setMinimum(1) # устанавливаем минимальное значение 1
        self.ui.spinBox_zp.setMaximum(31) # устанавливаем максимальное значение 31
        self.ui.spinBox_avans.setMinimum(1) # устанавливаем минимальное значение 1
        self.ui.spinBox_avans.setMaximum(31) # устанавливаем максимальное значение 31

        # добавляем иконки
        zp_icon_path = ":/icons/icons/zp.png"
        avans_icon_path = ":/icons/icons/avans.png"

        # добавляем иконки в QPixmap
        zp_icon = QPixmap(zp_icon_path)
        avans_icon = QPixmap(avans_icon_path)

        # если иконки не пустые, то добавляем их в label
        if not zp_icon.isNull() and not avans_icon.isNull():
            # Сохраняем оригинальный текст
            original_zp_text = self.ui.label_day_zp.text()
            original_avans_text = self.ui.label_day_avans.text()
            
            # Создаем HTML с иконкой и текстом (иконка слева, текст по центру)
            zp_icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{zp_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_zp_text}</td></tr></table>'
            avans_icon_html = f'<table style="width: 100%; height: 100%;"><tr><td style="vertical-align: middle; width: 28px; padding-right: 4px;"><img src="{avans_icon_path}" width="24" height="24" style="vertical-align: middle;"></td><td style="vertical-align: middle; text-align: center;">{original_avans_text}</td></tr></table>'
            
            # применяем HTML к label
            self.ui.label_day_zp.setText(zp_icon_html)
            self.ui.label_day_avans.setText(avans_icon_html)

        # выравниваем по левому краю
        self.ui.label_day_zp.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        self.ui.label_day_avans.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        
        # применяем стили:
        # к label
        self.ui.label_day_zp.setStyleSheet(self.secondary_information.label_day_zp) # применяем стиль к label_day_zp
        self.ui.label_day_avans.setStyleSheet(self.secondary_information.label_day_avans) # применяем стиль к label_day_avans
        # к spinBox
        self.ui.spinBox_zp.setStyleSheet(self.secondary_information.spinBox_zp) # применяем стиль к label_day_zp
        self.ui.spinBox_avans.setStyleSheet(self.secondary_information.spinBox_avans) # применяем стиль к label_day_zp
        self.ui.spinBox_zp.setMinimumSize(QSize(40, 16777215))
        self.ui.spinBox_avans.setMinimumSize(QSize(40, 16777215))

        # _________________________________widget_days_zp_________________________________
        
        #dz_config = self.widget_days_zp.widget_days_zp # конфиг из конфига
        #self.ui.widget_days_zp.setStyleSheet(dz_config["style"]) # применяем стиль к виджету widget_days_zp
        
        # добавляем эффект размытой тени (параметры из конфига)
        #shadow_params = dz_config["shadow"] # параметры из конфига
        #shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        #shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        #shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        #shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        #shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        #self.ui.widget_days_zp.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету widget_days_zp

        # _________________________________widget_days_avans_________________________________
        
        #da_config = self.widget_days_avans.widget_days_avans # конфиг из конфига
        #self.ui.widget_days_avans.setStyleSheet(da_config["style"]) # применяем стиль к виджету widget_days_avans
        
        # добавляем эффект размытой тени (параметры из конфига)
        #shadow_params = da_config["shadow"] # параметры из конфига
        #shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        #shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        #shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        #shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        #shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        #self.ui.widget_days_avans.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету widget_days_avans
        
        # общая логика для widget_days_zp и widget_days_avans
        
        # применяем стили к label_head_day и label_day (от 1 до 31)
        # и настраиваем логику переключения между QLabel и QLineEdit
        self.label_edits = {}  # словарь для хранения соответствия label -> lineEdit
        self.current_editing_label = None  # текущий редактируемый label
        
        for i in range(1, 32):
            label_head = getattr(self.ui, f"label_head_day_{i}", None) # получаем соответствующий label_head_day_i
            label_day = getattr(self.ui, f"label_day_{i}", None) # получаем соответствующий label_day_i
            if label_head:
                label_head.setStyleSheet(self.widget_days_zp_avans.label_head_day) # применяем стиль к label_head_day
            if label_day:
                label_day.setStyleSheet(self.widget_days_zp_avans.label_day) # применяем стиль к label_day
                label_day.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                # создаем QLineEdit для этого label_day
                line_edit = QLineEdit()
                line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
                line_edit.setStyleSheet(self.widget_days_zp_avans.lineEdit_day)
                # устанавливаем валидатор только для целых чисел (0-999999)
                validator = QIntValidator(0, 999999)
                line_edit.setValidator(validator)
                
                # получаем родительский layout (day_i)
                day_layout = getattr(self.ui, f"day_{i}", None)
                if day_layout:
                    # находим позицию label_day в layout
                    label_index = day_layout.indexOf(label_day)
                    if label_index >= 0:
                        # создаем QStackedLayout для переключения между label и lineEdit
                        stacked_layout = QStackedLayout()
                        stacked_layout.addWidget(label_day)  # индекс 0 - label
                        stacked_layout.addWidget(line_edit)  # индекс 1 - lineEdit
                        stacked_layout.setCurrentIndex(0)  # показываем label
                        
                        # заменяем label_day на stacked_layout в day_layout
                        day_layout.removeWidget(label_day)
                        day_layout.insertLayout(label_index, stacked_layout)
                        
                        # сохраняем связь между label, lineEdit и stacked_layout
                        self.label_edits[label_day] = {
                            'line_edit': line_edit,
                            'stacked_layout': stacked_layout
                        }
                        
                        setattr(self.ui, f"lineEdit_day_{i}", line_edit) # сохраняем lineEdit как атрибут UI для доступа из MainLogic
                        
                        # подключаем обработчики событий
                        label_day.mousePressEvent = lambda event, lbl=label_day: self.start_edit(lbl, event) # подключаем обработчик событий для label_day
                        line_edit.editingFinished.connect(lambda le=line_edit, lbl=label_day: self.finish_edit(lbl, le)) # подключаем обработчик событий для line_edit
                        line_edit.returnPressed.connect(lambda le=line_edit, lbl=label_day: self.finish_edit(lbl, le)) # подключаем обработчик событий для line_edit


        # _________________________________widget_table_zp_________________________________

        tdz_config = self.widget_table_zp.widget_table_zp # конфиг из конфига
        self.ui.widget_table_zp.setStyleSheet(tdz_config["style"]) # применяем стиль к виджету widget_table_zp
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = tdz_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        self.ui.widget_table_zp.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету general_information

        self.ui.label_zp.setStyleSheet(self.widget_table_zp.label_zp) # применяем стиль к label_zp
        self.ui.tableWidget_zp.setStyleSheet(self.widget_table_zp.tableWidget_zp) # применяем стиль к tableWidget_zp

        # _________________________________widget_table_avans__________________________________

        tda_config = self.widget_table_avans.widget_table_avans # конфиг из конфига
        self.ui.widget_table_avans.setStyleSheet(tda_config["style"]) # применяем стиль к виджету widget_table_avans
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = tda_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        self.ui.widget_table_avans.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету widget_table_avans

        self.ui.label_avans.setStyleSheet(self.widget_table_avans.label_avans) # применяем стиль к label_avans
        self.ui.tableWidget_avans.setStyleSheet(self.widget_table_avans.tableWidget_avans) # применяем стиль к tableWidget_avans

        # _________________________________calendar___________________________________

        wc_config = self.widget_calendar.widget_calendar # конфиг из конфига
        self.ui.widget_calendar.setStyleSheet(wc_config["style"]) # применяем стиль к виджету widget_calendar
        
        # добавляем эффект размытой тени (параметры из конфига)
        shadow_params = wc_config["shadow"] # параметры из конфига
        shadow = QGraphicsDropShadowEffect() # эффект размытой тени
        shadow.setBlurRadius(shadow_params["blur_radius"]) # радиус размытия
        shadow.setXOffset(shadow_params["x_offset"]) # смещение по X
        shadow.setYOffset(shadow_params["y_offset"]) # смещение по Y
        shadow.setColor(QColor(*shadow_params["color"])) # цвет тени
        self.ui.widget_calendar.setGraphicsEffect(shadow) # добавляем эффект размытой тени к виджету widget_calendar

        # настройка иконки календаря
        calendar_int_icon_path = ":/icons/icons/calendar_int.png"
        calendar_int_icon = QPixmap(calendar_int_icon_path)

        if not calendar_int_icon.isNull():
            self.ui.label_calendar_icon.setPixmap(calendar_int_icon) # устанавливаем иконку
            self.ui.label_calendar_icon.setFixedSize(70, 70) # устанавливаем размер иконки
            self.ui.label_calendar_icon.setScaledContents(True) # масштабируем иконку

        self.ui.label_calendar_icon.setStyleSheet(self.widget_calendar.label_calendar_icon) # применяем стиль к label_calendar_icon
        
        # настройка label_calendar_day
        self.ui.label_calendar_day.setStyleSheet(self.widget_calendar.label_calendar_day) # применяем стиль к label_calendar_day
        self.ui.label_calendar_day.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        self.ui.label_calendar_day.setContentsMargins(0, 0, 0, 0) # убираем внутренние отступы
        self.ui.label_calendar_day.setIndent(0) # убираем отступ текста
        
        # настройка label_calendar_month
        self.ui.label_calendar_month.setStyleSheet(self.widget_calendar.label_calendar_month) # применяем стиль к label_calendar_month
        self.ui.label_calendar_month.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        self.ui.label_calendar_month.setContentsMargins(0, 0, 0, 0) # убираем внутренние отступы
        self.ui.label_calendar_month.setIndent(0) # убираем отступ текста

        # настройка label_calendar_year
        self.ui.label_calendar_year.setStyleSheet(self.widget_calendar.label_calendar_year) # применяем стиль к label_calendar_year
        self.ui.label_calendar_year.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter) # выравниваем по левому краю
        self.ui.label_calendar_year.setContentsMargins(0, 0, 0, 0) # убираем внутренние отступы
        self.ui.label_calendar_year.setIndent(0) # убираем отступ текста
        
        # настройка progressBar_calendar
        self.ui.progressBar_calendar.setStyleSheet(self.widget_calendar.progressBar_calendar) # применяем стиль к progressBar_calendar

        # настройка клавиш "вперед", "назад"
        # добавляем иконки
        last_path = ":/icons/icons/last.png"
        next_path = ":/icons/icons/next.png"
        
        # добавляем иконки в QPixmap
        last_icon = QPixmap(last_path)
        next_icon = QPixmap(next_path)
        
        # если иконки не пустые, добавляем их на кнопки
        if not last_icon.isNull() and not next_icon.isNull():
            self.ui.pushButton_last.setIcon(QIcon(last_icon)) # устанавливаем иконку на кнопку last
            self.ui.pushButton_next.setIcon(QIcon(next_icon)) # устанавливаем иконку на кнопку next
            self.ui.pushButton_last.setIconSize(QSize(18, 18)) # устанавливаем размер иконки
            self.ui.pushButton_next.setIconSize(QSize(18, 18)) # устанавливаем размер иконки

        self.ui.pushButton_last.setStyleSheet(self.widget_calendar.pushButton_last) # применяем стиль к pushButton_last
        self.ui.pushButton_next.setStyleSheet(self.widget_calendar.pushButton_next) # применяем стиль к pushButton_next

        # логика смены данных календаря
        self.calendar_logic = CalendarLogic(
            self.ui.label_month, # инициализируем метку месяца
            self.ui.tableWidget_calendar, # инициализируем таблицу календаря
            self.ui.label_calendar_day, # инициализируем метку дня
            self.ui.label_calendar_month, # инициализируем метку месяца
            self.ui.label_calendar_year, # инициализируем метку года
            self.ui.progressBar_calendar, # инициализируем progressBar
            self.ui.lineEdit_calendar, # инициализируем lineEdit_calendar
            self.ui.lineEdit_work, # инициализируем lineEdit_work
            self.ui.lineEdit_weekend, # инициализируем lineEdit_weekend
            self.ui, # передаем UI для доступа к label_day_i
            self.widget_days_zp_avans # передаем конфигурацию для стилей
            )
        
        self.ui.pushButton_last.clicked.connect(self.calendar_logic.prev_month) # переход к предыдущему месяцу
        self.ui.pushButton_next.clicked.connect(self.calendar_logic.next_month) # переход к следующему месяцу

        # настройка label_month
        self.ui.label_month.setStyleSheet(self.widget_calendar.label_month) # применяем стиль к label_month

        # настройка tableWidget_calendar
        table = self.ui.tableWidget_calendar # присваиваем tableWidget_calendar к table

        table.setRowCount(6) # устанавливаем количество строк
        table.setColumnCount(7) # устанавливаем количество столбцов

        table.setHorizontalHeaderLabels(
            ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        )

        # параметры tableWidget_calendar
        table.verticalHeader().setVisible(False) # устанавливаем видимость вертикальных заголовков
        table.setShowGrid(False) # устанавливаем видимость сетки
        table.setFrameShape(table.Shape.NoFrame) # устанавливаем форму фрейма
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # подгоняем размеры столбцов
        table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # подгоняем размеры строк
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) # устанавливаем политику прокрутки горизонтальной полосы
        table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) # устанавливаем политику прокрутки вертикальной полосы
        table.setEditTriggers(self.ui.tableWidget_calendar.EditTrigger.NoEditTriggers) # устанавливаем режим редактирования (отключаем)
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection) # отключаем выделение ячеек в tableWidget_calendar
        table.setFocusPolicy(Qt.FocusPolicy.NoFocus) # отключаем фокус на tableWidget_calendar

        self.ui.tableWidget_calendar.setStyleSheet(self.widget_calendar.tableWidget_calendar) # применяем стиль к tableWidget_calendar

    # функция для начала редактирования label_day
    def start_edit(self, label_day, event):
        """Начинаем редактирование label_day - переключаемся на QLineEdit"""
        
        edit_data = self.label_edits[label_day] # получаем данные из словаря label_edits
        line_edit = edit_data['line_edit'] # получаем line_edit из данных
        stacked_layout = edit_data['stacked_layout'] # получаем stacked_layout из данных
        
        self.current_editing_label = label_day # сохраняем текущий редактируемый label
        
        line_edit.setText(label_day.text()) # устанавливаем текст из label в lineEdit
        line_edit.selectAll() # выделяем весь текст в lineEdit
        
        stacked_layout.setCurrentIndex(1) # переключаемся на lineEdit (1 потому что индекс 0 - label, а индекс 1 - lineEdit)
        line_edit.setFocus() # устанавливаем фокус на lineEdit

    # функция для завершения редактирования label_day
    def finish_edit(self, label_day, line_edit):
        """Завершаем редактирование - сохраняем текст и переключаемся обратно на QLabel"""
        
        edit_data = self.label_edits[label_day] # получаем данные из словаря label_edits
        stacked_layout = edit_data['stacked_layout'] # получаем stacked_layout из данных
        
        # сохраняем текст из lineEdit в label
        text = line_edit.text() # получаем текст из lineEdit
        if not text: # если текст пустой
            stacked_layout.setCurrentIndex(0) # переключаемся обратно на label (0 потому что индекс 0 - label, а индекс 1 - lineEdit)
            if self.current_editing_label == label_day: # если текущий редактируемый label равен label_day
                self.current_editing_label = None # сбрасываем текущий редактируемый label
            return
        
        # валидатор гарантирует, что текст является числом, но для надежности используем try-except
        try: # в случае ошибки оставляем старое значение (не должно происходить благодаря валидатору)
            value = int(text) # преобразуем текст в число
            formatted_text = f"{value:,}".replace(",", " ") # заменяем запятые на пробелы
            label_day.setText(formatted_text) # устанавливаем текст в label
        except (ValueError, TypeError): # в случае ошибки оставляем старое значение (не должно происходить благодаря валидатору)
            pass # оставляем старое значение (не должно происходить благодаря валидатору)
        
        stacked_layout.setCurrentIndex(0) # переключаемся обратно на label
        
        if self.current_editing_label == label_day: # если текущий редактируемый label равен label_day
            self.current_editing_label = None # сбрасываем текущий редактируемый label