from PyQt6.QtWidgets import QLabel, QTableWidget, QTableWidgetItem
from PyQt6 import QtCore

from calendar import monthcalendar
from datetime import date

class CalendarLogic:
    
    """ЛОГИКА СМЕНЫ МЕСЯЦА В КАЛЕНДАРЕ."""

    def __init__(self,
                 label_month: QLabel,
                 tableWidget_calendar:QTableWidget, 
                 label_calendar_day: QLabel = None,
                 label_calendar_month: QLabel = None,
                 label_calendar_year: QLabel = None):
        self.label_month = label_month # метка для отображения месяца
        self.tableWidget_calendar = tableWidget_calendar # таблица для отображения календаря
        self.label_calendar_day = label_calendar_day # метка для отображения дня
        self.label_calendar_month = label_calendar_month # метка для отображения месяца
        self.label_calendar_year = label_calendar_year # метка для отображения года
        
        self.today = date.today() # текущая дата
        self.year = self.today.year # текущий год
        
        self.months = [
            "Январь", "Февраль", "Март",
            "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь",
            "Октябрь", "Ноябрь", "Декабрь",
        ]

        self.current_month_index = self.today.month - 1 # текущий месяц (индекс от 0)
        self.set_date(self.current_month_index) # устанавливаем текст месяца

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

        self.label_calendar_day.setText(str(self.today.day)) # устанавливаем текст текущего дня
        self.label_calendar_month.setText(str(self.months[self.today.month - 1])) # устанавливаем текст текущего месяца

        self.label_month.setText(self.months[self.current_month_index]) # устанавливаем текст месяца (с возможностью смены)
        self.label_calendar_year.setText(str(self.year)) # устанавливаем текст года (с возможностью смены)
        
        self.show_days() # отображаем дни в календаре
        self.set_year(self.year) # устанавливаем год

    # функция для перехода к предыдущему месяцу
    def prev_month(self):
        """Переходим к предыдущему месяцу."""
        self.set_date(self.current_month_index - 1)

    # функция для перехода к следующему месяцу
    def next_month(self):
        """Переходим к следующему месяцу."""
        self.set_date(self.current_month_index + 1)
    
    # функция для отображения дней в календаре
    def show_days(self):
        month = self.current_month_index + 1 # номер месяца (+1 потому что нумерация месяцев начинается с 0, а в calendar начинается с 1)
        weeks = monthcalendar(self.year, month) # получаем список недель

        self.tableWidget_calendar.clear() # очищаем таблицу
        self.tableWidget_calendar.setRowCount(6) # устанавливаем количество строк
        self.tableWidget_calendar.setColumnCount(7) # устанавливаем количество столбцов

        self.tableWidget_calendar.setHorizontalHeaderLabels(["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]) # устанавливаем заголовки столбцов

        for row, week in enumerate(weeks):
            for col, day in enumerate(week):
                text = "" if day == 0 else str(day) # если день равен 0, то устанавливаем пустой текст
                item = QTableWidgetItem(text) # создаем элемент таблицы
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) # устанавливаем выравнивание текста по центру
                self.tableWidget_calendar.setItem(row, col, item) # устанавливаем элемент в таблицу

    # функция для установки текста года
    def set_year(self, year: int):
        self.year = year # устанавливаем год
        self.label_calendar_year.setText(str(year)) # устанавливаем текст года