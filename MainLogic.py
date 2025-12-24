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
        self.tableWidget_calendar = tableWidget_calendar
        self.label_calendar_day = label_calendar_day # метка для отображения дня
        self.label_calendar_month = label_calendar_month # метка для отображения месяца
        self.label_calendar_year = label_calendar_year # метка для отображения года
        
        today = date.today() # текущая дата
        self.year = today.year # текущий год
        
        self.months = [
            "Январь", "Февраль", "Март",
            "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь",
            "Октябрь", "Ноябрь", "Декабрь",
        ]

        self.current_month_index = today.month - 1 # текущий месяц (индекс от 0)
        self.set_month(self.current_month_index) # устанавливаем текст месяца
        
        # устанавливаем текущий день и месяц в label_calendar_day и label_calendar_month
        if self.label_calendar_day and self.label_calendar_month and self.label_calendar_year:
            self.show_day_and_month(today.day, today.month, today.year)

    # функция для установки текста месяца
    def set_month(self, index: int):
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
        self.label_month.setText(self.months[self.current_month_index]) # устанавливаем текст месяца
        self.show_days() # отображаем дни в календаре

    # функция для перехода к предыдущему месяцу
    def prev_month(self):
        """Переходим к предыдущему месяцу."""
        self.set_month(self.current_month_index - 1)

    # функция для перехода к следующему месяцу
    def next_month(self):
        """Переходим к следующему месяцу."""
        self.set_month(self.current_month_index + 1)
    
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
    
    # функция для отображения дня, месяца и года в label_calendar_day и label_calendar_month, label_calendar_year
    def show_day_and_month(self, day: int, month: int, year: int):
        self.label_calendar_day.setText(str(day)) # устанавливаем текст дня
        self.label_calendar_month.setText(self.months[month - 1]) # устанавливаем текст месяца
        self.label_calendar_year.setText(str(year)) # устанавливаем текст года