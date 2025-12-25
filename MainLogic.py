from PyQt6.QtWidgets import QLabel, QTableWidget, QTableWidgetItem, QProgressBar, QLineEdit
from PyQt6.QtGui import QColor
from PyQt6 import QtCore

from calendar import monthcalendar, calendar, monthrange
from datetime import date, datetime

import json

from rounded_delegate import RoundedItemDelegate

class CalendarLogic:
    
    """ЛОГИКА СМЕНЫ МЕСЯЦА В КАЛЕНДАРЕ."""

    def __init__(self,
                 label_month: QLabel,
                 tableWidget_calendar:QTableWidget, 
                 label_calendar_day: QLabel = None,
                 label_calendar_month: QLabel = None,
                 label_calendar_year: QLabel = None,
                 progressBar: QProgressBar = None,
                 lineEdit_calendar: QLineEdit = None,
                 lineEdit_work: QLineEdit = None,
                 lineEdit_weekend: QLineEdit = None):

        self.label_month = label_month # метка для отображения месяца
        self.tableWidget_calendar = tableWidget_calendar # таблица для отображения календаря
        self.label_calendar_day = label_calendar_day # метка для отображения дня
        self.label_calendar_month = label_calendar_month # метка для отображения месяца
        self.label_calendar_year = label_calendar_year # метка для отображения года
        self.progressBar = progressBar # progressBar для отображения прогресса
        self.lineEdit_calendar = lineEdit_calendar # lineEdit для отображения кол-ва дней в месяце
        self.lineEdit_work = lineEdit_work # lineEdit для отображения кол-ва рабочих дней
        self.lineEdit_weekend = lineEdit_weekend # lineEdit для отображения кол-ва выходных дней
        
        self.today = date.today() # текущая дата
        self.year = self.today.year # текущий год
        self.month = self.today.month # текущий месяц
        self.day = self.today.day # текущий день
        
        self.months = [
            "Январь", "Февраль", "Март",
            "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь",
            "Октябрь", "Ноябрь", "Декабрь",
        ]

        self.current_month_index = self.month - 1 # текущий месяц (индекс от 0)
        
        # Устанавливаем делегат для закругленных углов ячеек
        delegate = RoundedItemDelegate(self.tableWidget_calendar, radius=8)
        self.tableWidget_calendar.setItemDelegate(delegate)
        
        self.set_date(self.current_month_index) # устанавливаем текст месяца

    """ЛОГИКА ОПРЕДЕЛЕНИЯ КОЛИЧЕСТВА ДНЕЙ В МЕСЯЦЕ, НЕРАБОЧИХ ДНЕЙ И РАБОЧИХ ДНЕЙ"""

    def calendar_work_weekend(self, day: int = None, month: int = None, year: int = None):

        """ Определяем количество дней в месяце """

        calendar_month = self.current_month_index + 1 # Определяем выбранный месяц календаря (индекс + 1)
        calendar_year = self.year # Определяем выбранный год календаря
        calendar_days = monthrange(calendar_year, calendar_month)[1] # Определяем количество дней в выбранном месяце

        if self.lineEdit_calendar is not None:
            self.lineEdit_calendar.setText(str(calendar_days)) # Устанавливаем количество дней в выбранном месяце

        """ Определякм количество нерабочих дней в месяце """
        
        with open("holidays.json", "r", encoding="utf-8") as f:
            holidays_data = json.load(f) # загружаем данные из файла
            holidays_list = holidays_data.get("holidays", []) # получаем список праздников
            not_weekend_list = holidays_data.get("not_weekend", []) # получаем список рабочих выходных дней
            
            # преобразуем списки дат в множества для быстрого поиска
            self.non_working_days = {
                datetime.strptime(d, "%d.%m.%Y").date() # преобразуем строку в дату
                for d in holidays_list # проходим по списку праздников
            }
            self.working_weekends = {
                datetime.strptime(d, "%d.%m.%Y").date() # преобразуем строку в дату
                for d in not_weekend_list # проходим по списку рабочих выходных дней
            }
        
        non_working_days = [] # список нерабочих дней
        for day in range(1, calendar_days + 1): # проходим по дням месяца (+ 1 потому что нумерация дней начинается с 1, а в range начинается с 0)
            current_date = date(calendar_year, calendar_month, day) # создаем дату
            
            # день считается нерабочим, если:
            # 1. он в списке праздников, ИЛИ
            # 2. это выходной (weekday >= 5) И он НЕ в списке рабочих выходных
            is_holiday = current_date in self.non_working_days
            is_weekend = current_date.weekday() >= 5
            is_working_weekend = current_date in self.working_weekends
            
            if is_holiday or (is_weekend and not is_working_weekend):
                non_working_days.append(current_date) # добавляем день в список нерабочих дней

        if self.lineEdit_weekend is not None: # если lineEdit_weekend не None
            self.lineEdit_weekend.setText(str(len(non_working_days))) # Устанавливаем количество выходных дней
        
        """Определяем количество рабочих дней в месяце """
        
        working_days = calendar_days - len(non_working_days) # определяем количество рабочих дней
        if self.lineEdit_work is not None: # если lineEdit_work не None
            self.lineEdit_work.setText(str(working_days)) # Устанавливаем количество рабочих дней

    # функция для установки текста месяца и года
    def set_date(self, index: int):
        """Устанавливаем текст месяца по индексу с циклическим переходом."""
        # Обрабатываем переходы между годами
        if index < 0:
            # Переход к предыдущему году
            self.year -= 1
            index = len(self.months) - 1
        elif index >= len(self.months):
            # Переход к следующему году
            self.year += 1
            index = 0
        
        self.current_month_index = index # устанавливаем текущий месяц

        self.label_calendar_day.setText(str(self.day)) # устанавливаем текст текущего дня
        self.label_calendar_month.setText(str(self.months[self.month - 1])) # устанавливаем текст текущего месяца

        self.label_month.setText(self.months[self.current_month_index]) # устанавливаем текст месяца (с возможностью смены)
        self.label_calendar_year.setText(str(self.year)) # устанавливаем текст года (с возможностью смены)
        
        self.show_days() # отображаем дни в календаре
        self.show_year() # устанавливаем год
        
        # обновляем прогрессбар при смене месяца
        if self.progressBar is not None:
            self.show_progress()
        
        # обновляем количество дней в месяце
        self.calendar_work_weekend()

    # функция для перехода к предыдущему месяцу
    def prev_month(self):
        """Переходим к предыдущему месяцу."""
        self.set_date(self.current_month_index - 1)

    # функция для перехода к следующему месяцу
    def next_month(self):
        """Переходим к следующему месяцу."""
        self.set_date(self.current_month_index + 1)
    
    """ЛОГИКА ОТОБРАЖЕНИЯ ДНЕЙ В КАЛЕНДАРЕ"""

    # функция для отображения дней в календаре
    def show_days(self):
        month = self.current_month_index + 1 # номер месяца (+1 потому что нумерация месяцев начинается с 0, а в calendar начинается с 1)
        weeks = monthcalendar(self.year, month) # получаем список недель

        self.tableWidget_calendar.clear() # очищаем таблицу
        self.tableWidget_calendar.setRowCount(6) # устанавливаем количество строк
        self.tableWidget_calendar.setColumnCount(7) # устанавливаем количество столбцов

        self.tableWidget_calendar.setHorizontalHeaderLabels(["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]) # устанавливаем заголовки столбцов

        # загружаем данные о праздниках и рабочих выходных для подсветки
        with open("holidays.json", "r", encoding="utf-8") as f:
            holidays_data = json.load(f) # загружаем данные из файла
            holidays_list = holidays_data.get("holidays", []) # получаем список праздников
            not_weekend_list = holidays_data.get("not_weekend", []) # получаем список рабочих выходных дней
            
            # преобразуем списки дат в множества для быстрого поиска
            non_working_days_set = {
                datetime.strptime(d, "%d.%m.%Y").date() # преобразуем строку в дату
                for d in holidays_list # проходим по списку праздников
            }
            working_weekends_set = {
                datetime.strptime(d, "%d.%m.%Y").date() # преобразуем строку в дату
                for d in not_weekend_list # проходим по списку рабочих выходных дней
            }

        for row, week in enumerate(weeks):
            for col, day in enumerate(week):
                text = "" if day == 0 else str(day) # если день равен 0, то устанавливаем пустой текст
                item = QTableWidgetItem(text) # создаем элемент таблицы
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) # устанавливаем выравнивание текста по центру
                
                # подсветка дней
                if day != 0: # если день валидный (не пустой)
                    current_date = date(self.year, month, day) # создаем дату текущего дня
                    
                    # проверяем, является ли день праздником
                    is_holiday = current_date in non_working_days_set
                    
                    # проверяем, является ли день выходным (суббота=5, воскресенье=6)
                    is_weekend = (col == 5 or col == 6) # col 5 = суббота, col 6 = воскресенье
                    is_working_weekend = current_date in working_weekends_set
                    
                    # подсветка праздников (красный фон)
                    if is_holiday:
                        item.setBackground(QColor("#FECACA")) # светло-красный фон
                        item.setForeground(QColor("#7F1D1D"))
                    # подсветка выходных дней, но только если это не рабочий выходной
                    elif is_weekend and not is_working_weekend:
                        item.setBackground(QColor("#FECACA")) # светло-красный фон
                        item.setForeground(QColor("#7F1D1D"))
                
                self.tableWidget_calendar.setItem(row, col, item) # устанавливаем элемент в таблицу

                

    # функция для установки текста года
    def show_year(self, year: int = None):
        if year is None:
            year = self.year # используем текущий год, если не передан аргумент
        else:
            self.year = year # устанавливаем год, если передан аргумент
        self.label_calendar_year.setText(str(year)) # устанавливаем текст года

    """ЛОГИКА РАБОТЫ PROGRESS BARа"""

    def show_progress(self):
        
        display_month = self.current_month_index + 1 # Определяем отображаемый месяц (current_month_index + 1, т.к. индексы с 0, а месяцы с 1)
        first_day = 1 # Первый день месяца всегда 1
        last_day = monthrange(self.year, display_month)[1] # Последний день месяца через monthrange(год, месяц)[1]
        
        # Определяем значение дня для отображения
        # Если смотрим текущий месяц и год - показываем текущий день
        # Иначе показываем 1 (начало месяца)
        if (self.year == self.today.year and 
            display_month == self.month):
            value = self.day  # текущий день в текущем месяце
        else:
            value = 1  # для прошлых/будущих месяцев показываем начало

        # устанавливаем диапазон и значение в progressBar
        self.progressBar.setMinimum(first_day)
        self.progressBar.setMaximum(last_day)
        self.progressBar.setValue(value)