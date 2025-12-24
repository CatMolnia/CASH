from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass(frozen=True)
class AppWindowConfig:
    sizes: Dict[str, Tuple[int, int]] = field(
        default_factory=lambda: {
            "default": (1500, 660)
        }
    )
    
    default_size: str = "default"

class GeneralInformation:
    
    # конфиг для general_information
    general_information = {
        "style": (
            "QWidget#general_information { "
            "background-color: #FFFFFF; "
            "border: none; "
            "border-radius: 12px; "
            "margin: 0px 2px 6px 2px; "
            "}"
        ),
        "shadow": {
            "blur_radius": 15,
            "x_offset": 6,
            "y_offset": 6,
            "color": (0, 0, 0, 80)  # RGBA: черный с прозрачностью 80/255
        }
    }
    
    label_title = (
        "color: #4B5563; "
        "background-color: #FFFFFF; "
        "border: none; "
        "font-size: 32px; "
        "font-weight: 800;"
    )

    label_calendar = (
        "color: #4B5563; "
        "background-color: #F4F4F4; "
        "border-top: 2px solid #94A3B8; "
        "border-left: 2px solid #94A3B8; "
        "border-bottom: 2px solid #E2E8F0; "
        "border-right: 2px solid #E2E8F0; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 12px; "
        "font-weight: 500;"
    )

    label_work = (
        "color: #4B5563; "
        "background-color: #F4F4F4; " #CBD5E1
        "border-top: 2px solid #94A3B8; "
        "border-left: 2px solid #94A3B8; "
        "border-bottom: 2px solid #E2E8F0; "
        "border-right: 2px solid #E2E8F0; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 12px; "
        "font-weight: 500;"
    )

    label_weekend = (
        "color: #4B5563; "
        "background-color: #F4F4F4; "
        "border-top: 2px solid #94A3B8; "
        "border-left: 2px solid #94A3B8; "
        "border-bottom: 2px solid #E2E8F0; "
        "border-right: 2px solid #E2E8F0; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 12px; "
        "font-weight: 500;"
    )

    # конфиг для lineEdit
    lineEdit_calendar = (
        "color: #4B5563; "
        "background-color: #F4F4F4; "
        "border-top: 2px solid #94A3B8; "
        "border-left: 2px solid #94A3B8; "
        "border-bottom: 2px solid #E2E8F0; "
        "border-right: 2px solid #E2E8F0; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 16px; "
        "font-weight: 500;"
    )

    lineEdit_work = (
        "color: #4B5563; "
        "background-color: #F4F4F4; "
        "border-top: 2px solid #94A3B8; "
        "border-left: 2px solid #94A3B8; "
        "border-bottom: 2px solid #E2E8F0; "
        "border-right: 2px solid #E2E8F0; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 16px; "
        "font-weight: 500;"
    )

    lineEdit_weekend = (
        "color: #4B5563; "
        "background-color: #F4F4F4; "
        "border-top: 2px solid #94A3B8; "
        "border-left: 2px solid #94A3B8; "
        "border-bottom: 2px solid #E2E8F0; "
        "border-right: 2px solid #E2E8F0; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 16px; "
        "font-weight: 500;"
    )

class SecondaryInformation:
    # конфиг для secondary_information
    secondary_information = {
        "style": (
            "QWidget#secondary_information { "
            "background-color: #FFFFFF; "
            "border: none; "
            "border-radius: 12px; "
            "margin: 0px 2px 6px 2px; "
            "}"
        ),
        "shadow": {
            "blur_radius": 15,
            "x_offset": 6,
            "y_offset": 6,
            "color": (0, 0, 0, 80)  # RGBA: черный с прозрачностью 80/255
        }
    }

    label_day_zp = (
        "color: #4B5563; "
        "background-color: #F4F4F4; "
        "border-top: 2px solid #94A3B8; "
        "border-left: 2px solid #94A3B8; "
        "border-bottom: 2px solid #E2E8F0; "
        "border-right: 2px solid #E2E8F0; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 12px; "
        "font-weight: 500;"
    )

    label_day_avans = (
        "color: #4B5563; "
        "background-color: #F4F4F4; "
        "border-top: 2px solid #94A3B8; "
        "border-left: 2px solid #94A3B8; "
        "border-bottom: 2px solid #E2E8F0; "
        "border-right: 2px solid #E2E8F0; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 12px; "
        "font-weight: 500;"
    )

    spinBox_zp = (
        "QSpinBox {"
        "   color: #E5E7EB;"
        "   background-color: #374151;"
        "   border: 1px solid #4B5563;"
        "   border-radius: 6px;"
        "   padding: 4px 6px;"
        "   font-size: 16px;"
        "   selection-color: #E5E7EB;"
        "   selection-background-color: transparent;"
        "}"

        "QSpinBox::up-button, QSpinBox::down-button {"
        "   width: 20px;"
        "   background: #4B5563;"
        "   border: none;"
        "}"

        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {"
        "   background: #6B7280;"
        "}"

        "QSpinBox::up-button {"
        "   border-top-right-radius: 6px;"
        "}"

        "QSpinBox::down-button {"
        "   border-bottom-right-radius: 6px;"
        "}"
    )

    spinBox_avans = (
        "QSpinBox {"
        "   color: #E5E7EB;"
        "   background-color: #374151;"
        "   border: 1px solid #4B5563;"
        "   border-radius: 6px;"
        "   padding: 4px 6px;"
        "   font-size: 16px;"
        "   selection-color: #E5E7EB;"
        "   selection-background-color: transparent;"
        "}"

        "QSpinBox::up-button, QSpinBox::down-button {"
        "   width: 20px;"
        "   background: #4B5563;"
        "   border: none;"
        "}"

        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {"
        "   background: #6B7280;"
        "}"

        "QSpinBox::up-button {"
        "   border-top-right-radius: 6px;"
        "}"

        "QSpinBox::down-button {"
        "   border-bottom-right-radius: 6px;"
        "}"
    )

class WidgetDaysZp:
    # конфиг для widget_days_zp
    widget_days_zp = {
        "style": (
            "QWidget#widget_days_zp { "
            "background-color: #B8BFBC; "
            "border: black; "
            "border-radius: 12px; "
            "margin: 0px 2px 6px 2px; "
            "}"
        ),
        "shadow": {
            "blur_radius": 15,
            "x_offset": 6,
            "y_offset": 6,
            "color": (0, 0, 0, 80)  # RGBA: черный с прозрачностью 80/255
        }
    }    

class WidgetDaysAvans:
    # конфиг для widget_days_avans
    widget_days_avans = {
        "style": (
            "QWidget#widget_days_avans { "
            "background-color: #B8BFBC; "
            "border: none; "
            "border-radius: 12px; "
            "margin: 0px 2px 6px 2px; "
            "}"
        ),
        "shadow": {
            "blur_radius": 15, 
            "x_offset": 6,
            "y_offset": 6,
            "color": (0, 0, 0, 80)  # RGBA: черный с прозрачностью 80/255
        }
    }

class WidgetDaysZpAvans:
    # конфиг для label_head_day
    label_head_day = (
        "color: #4B5563; "
        "border: 1px solid #585959; "
        "background-color: #F4F4F4; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 16px; "
        "font-weight: 500;"
    )

    # конфиг для label_day (label_day_1 - label_day_31)
    label_day = (
        "color: #4B5563; "
        "border: 1px solid #585959; "
        "background-color: #F4F4F4; "
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 16px; "
        "font-weight: 500;"
    )

class WidgetTableZP:
    widget_table_zp = {
        "style": (
            "QWidget#widget_table_zp { "
            "background-color: #FFFFFF; "
            "border: none; "
            "border-radius: 12px; "
            "margin: 0px 2px 6px 2px; "
            "}"
        ),
        "shadow": {
            "blur_radius": 15,
            "x_offset": 6,
            "y_offset": 6,
            "color": (0, 0, 0, 80)  # RGBA: черный с прозрачностью 80/255
        }
    }

    label_zp = (
        "color:  #F4F4F4; "
        "background-color: #50526A; "
        "border-top: 2px solid #8B9491;"
        "border-left: 2px solid #8B9491;"
        "border-bottom: 2px solid #E6EBE9;"
        "border-right: 2px solid #E6EBE9;"
        "border-radius: 8px;"
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 14px; "
        "font-weight: 800;"
    )

    tableWidget_zp = (
        "color: #1F2933;"
        "background-color: #D9D6DF;"
        "border-top: 2px solid #8B9491;"
        "border-left: 2px solid #8B9491;"
        "border-bottom: 2px solid #E6EBE9;"
        "border-right: 2px solid #E6EBE9;"
        "border-radius: 8px;"
        "padding: 4px;"
        "font-size: 12px;"
        "font-weight: 500;"
    )

class WidgetTableAvans:
    widget_table_avans = {
        "style": (
            "QWidget#widget_table_avans { "
            "background-color: #FFFFFF; "
            "border: none; "
            "border-radius: 12px; "
            "margin: 0px 2px 6px 2px; "
            "}"
        ),
        "shadow": {
            "blur_radius": 15,
            "x_offset": 6,
            "y_offset": 6,
            "color": (0, 0, 0, 80)  # RGBA: черный с прозрачностью 80/255
        }
    }

    label_avans = (
        "color:  #F4F4F4; "
        "background-color: #50526A; "
        "border-top: 2px solid #8B9491;"
        "border-left: 2px solid #8B9491;"
        "border-bottom: 2px solid #E6EBE9;"
        "border-right: 2px solid #E6EBE9;"
        "border-radius: 8px;"
        "border-radius: 8px; "
        "padding: 4px 4px; "
        "font-size: 14px; "
        "font-weight: 800;"
    )

    tableWidget_avans = (
        "color: #1F2933;"
        "background-color: #D9D6DF;"
        "border-top: 2px solid #8B9491;"
        "border-left: 2px solid #8B9491;"
        "border-bottom: 2px solid #E6EBE9;"
        "border-right: 2px solid #E6EBE9;"
        "border-radius: 8px;"
        "padding: 4px;"
        "font-size: 12px;"
        "font-weight: 500;"
    )

class WidgetCalendar:
    widget_calendar = {
        "style": (
            "QWidget#widget_calendar { "
            "background-color: #FFFFFF; "
            "border: none; "
            "border-radius: 12px; "
            "margin: 0px 2px 6px 2px; "
            "}"
        ),
        "shadow": {
            "blur_radius": 15,
            "x_offset": 6,
            "y_offset": 6,
            "color": (0, 0, 0, 80)  # RGBA: черный с прозрачностью 80/255
        }
    }

    label_calendar_icon = (
        "background-color: #FFFFFF; "
    )

    label_calendar_day = (
        "color: #4B5563; "
        "background-color: #FFFFFF; "
        "border-radius: 8px; "
        "padding-left: 0px; "
        "padding-right: 0px; "
        "padding-top: 0px; "
        "padding-bottom: 0px; "
        "margin-left: 0px; "
        "font-size: 32px; "
        "font-weight: 800; "
        "text-align: left;"
    )

    label_calendar_month = (
        "color: #4B5563; "
        "background-color: #FFFFFF; "
        "border-radius: 8px; "
        "padding-left: 0px; "
        "padding-right: 0px; "
        "padding-top: 0px; "
        "padding-bottom: 0px; "
        "margin-left: 0px; "
        "font-size: 16px; "
        "font-weight: 500; "
        "text-align: left;"
    )

    label_calendar_year = (
        "color: #4B5563; "
        "background-color: #FFFFFF; "
        "border-radius: 6px; "
        "padding-left: 0px; "
        "padding-right: 0px; "
        "padding-top: 0px; "
        "padding-bottom: 0px; "
        "margin-left: 0px; "
        "font-size: 12px; " 
        "font-weight: 300; "
    )

    progressBar_calendar = (
        "QProgressBar {"
        "  background-color: rgba(0, 0, 0, 0.07);"
        "  border: none;"
        "  border-radius: 2px;"
        "  min-height: 4px;"
        "  max-height: 4px;"
        "}"
        "QProgressBar::chunk {"
        "  background-color: qlineargradient("
        "    x1:0, y1:0, x2:0, y2:1, "
        "    stop:0 #FF8A8A, stop:1 #FF3B30"
        "  );"
        "  border-radius: 2px;"
        "}"
    )

    pushButton_last = """
        QPushButton {
            background-color: #FFFFFF;
            border-top: 2px solid #94A3B8;
            border-left: 2px solid #94A3B8;
            border-bottom: 2px solid #E2E8F0;
            border-right: 2px solid #E2E8F0;
            border-radius: 8px;
            padding: 0px 20px;
            font-size: 16px;
            font-weight: 500;
        }
        QPushButton:hover {
            background-color: #F0F0F0;
        }
        QPushButton:pressed {
            background-color: #D9D9D9;
        }
        """

    pushButton_next = """
        QPushButton {
            background-color: #FFFFFF;
            border-top: 2px solid #94A3B8;
            border-left: 2px solid #94A3B8;
            border-bottom: 2px solid #E2E8F0;
            border-right: 2px solid #E2E8F0;
            border-radius: 8px; 
            padding: 0px 20px;  /* отступы внутри кнопки */
            font-size: 16px;  /* размер текста */
            font-weight: 500;  /* вес текста */
        }
        QPushButton:hover {
            background-color: #F0F0F0;
        }
        QPushButton:pressed {
            background-color: #D9D9D9;
        }
        """

    label_month = (
        "color: #4B5563; "
        "background-color: #FFFFFF; "
    )

    tableWidget_calendar = """
        QTableWidget {
            background-color: #F4F4F4;
            border-top: 2px solid #94A3B8;
            border-left: 2px solid #94A3B8;
            border-bottom: 2px solid #E2E8F0;
            border-right: 2px solid #E2E8F0;
            gridline-color: transparent;
        }

        /* Заголовки столбцов */
        QHeaderView {
            background: transparent;
        }

        /* Заголовки столбцов */
        QHeaderView::section {
            color: #374151;
            background-color: #FFFFFF;
            font-weight: 500;
            font-size: 12px;
            border: none;
            padding: 3px 6px;
        }

        /* Верхний левый угол */
        QHeaderView::section:horizontal:first {
            border-top-left-radius: 10px;
        }

        /* Верхний правый угол */
        QHeaderView::section:horizontal:last {
            border-top-right-radius: 10px;
        }

        /* Ячейки таблицы */
        QTableWidget::item {
            padding: 5px;
            color: black;
        }

        /* Выделение ячеек */
        QTableWidget::item:selected {
            background: none;
            color: black;
        }
    """