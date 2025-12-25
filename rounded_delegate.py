from PyQt6.QtWidgets import QStyledItemDelegate
from PyQt6.QtGui import QColor, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt


class RoundedItemDelegate(QStyledItemDelegate):
    """Делегат для отрисовки ячеек таблицы с закругленными углами."""
    
    def __init__(self, parent=None, radius=8):
        super().__init__(parent)
        self.radius = radius
    
    def paint(self, painter, option, index):
        """Отрисовывает ячейку с закругленными углами."""
        # Проверяем, есть ли в ячейке значение
        text = index.data(Qt.ItemDataRole.DisplayRole)
        
        # Если ячейка пустая, используем стандартную отрисовку
        if not text or str(text).strip() == "":
            super().paint(painter, option, index)
            return
        
        painter.save()
        
        # Получаем цвет фона из данных ячейки
        bg_brush = index.data(Qt.ItemDataRole.BackgroundRole)
        if bg_brush:
            if isinstance(bg_brush, QBrush):
                bg_color = bg_brush.color()
            elif isinstance(bg_brush, QColor):
                bg_color = bg_brush
            else:
                bg_color = QColor("#FFFFFF")
        else:
            bg_color = QColor("#FFFFFF")
        
        # Получаем цвет текста
        text_brush = index.data(Qt.ItemDataRole.ForegroundRole)
        if text_brush:
            if isinstance(text_brush, QBrush):
                text_color = text_brush.color()
            elif isinstance(text_brush, QColor):
                text_color = text_brush
            else:
                text_color = QColor("#000000")
        else:
            text_color = QColor("#000000")
        
        # Создаем прямоугольник с отступами для закругления
        rect = option.rect.adjusted(2, 2, -2, -2)
        
        # Рисуем закругленный прямоугольник с фоном
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(bg_color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(rect, self.radius, self.radius)
        
        # Рисуем текст
        painter.setPen(QPen(text_color))
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, str(text))
        
        painter.restore()

