from pydoc import text
from PyQt6.QtWidgets import QLabel, QTableWidget, QTableWidgetItem
from PyQt6 import QtCore

from calendar import month, monthcalendar, week

class CalendarLogic:
    
    """ЛОГИКА СМЕНЫ МЕСЯЦА В КАЛЕНДАРЕ."""

    def __init__(self, label_month: QLabel, tableWidget_calendar:QTableWidget):
        self.label_month = label_month # метка для отображения месяца
        self.tableWidget_calendar = tableWidget_calendar

        self.year = 2026
        
        self.months = [
            "Январь", "Февраль", "Март",
            "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь",
            "Октябрь", "Ноябрь", "Декабрь",
        ]
        self.current_month_index = 0 # текущий месяц
        self.set_month(self.current_month_index) # устанавливаем текст месяца

    # функция для установки текста месяца
    def set_month(self, index: int):
        """Устанавливаем текст месяца по индексу с циклическим переходом."""
        self.current_month_index = index % len(self.months) # устанавливаем текущий месяц с циклическим переходом
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