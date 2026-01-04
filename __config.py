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
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_work = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_weekend = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    # конфиг для lineEdit
    lineEdit_calendar = (
        "QLineEdit {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    lineEdit_work = (
        "QLineEdit {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    lineEdit_weekend = (
        "QLineEdit {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
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
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_day_avans = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
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
        "QLabel {"
        "color: #1F2937; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #D1D5DB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #F9FAFB"
        ");"

        "border: 1px solid #CBD5E1; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    # конфиг для label_day (label_day_1 - label_day_31)
    label_day = (
        "QLabel {"
        "color: #1F2937; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #D1D5DB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #F9FAFB"
        ");"

        "border: 1px solid #CBD5E1; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    # конфиг для lineEdit_day (lineEdit_day_1 - lineEdit_day_31)
    lineEdit_day = (
        "QLineEdit {"
        "color: #1F2937; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #D1D5DB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #F9FAFB"
        ");"

        "border: 1px solid #CBD5E1; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    # конфиг для label_day (label_day_1 - label_day_31)
    label_day_weekend_holiday = """
        QLabel {
            color: #7F1D1D;
            font-size: 12px;
            font-weight: 500;
            padding: 6px 8px;

            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #FCA5A5,
                stop:0.5 #FDE2E2,
                stop:1 #FEF2F2
            );

            border: 1px solid #585959;
            border-top-color: #9CA3AF;
            border-left-color: #9CA3AF;
            border-bottom-color: #E5E7EB;
            border-right-color: #E5E7EB;

            border-radius: 8px;
        }
    """

    # конфиг для label_day (label_day_1 - label_day_31)
    label_head_day_weekend_holiday = """
        QLabel {
            color: #7F1D1D;
            font-size: 12px;
            font-weight: 500;
            padding: 6px 8px;

            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #FCA5A5,
                stop:0.5 #FDE2E2,
                stop:1 #FEF2F2
            );

            border: 1px solid #585959;
            border-top-color: #9CA3AF;
            border-left-color: #9CA3AF;
            border-bottom-color: #E5E7EB;
            border-right-color: #E5E7EB;

            border-radius: 8px;
        }
    """

    # конфиг для lineEdit_day (lineEdit_day_1 - lineEdit_day_31)
    lineEdit_day_weekend_holiday = """
        QLineEdit {
            color: #7F1D1D;
            font-size: 12px;
            font-weight: 500;
            padding: 6px 8px;

            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #FCA5A5,
                stop:0.5 #FDE2E2,
                stop:1 #FEF2F2
            );

            border: 1px solid #585959;
            border-top-color: #9CA3AF;
            border-left-color: #9CA3AF;
            border-bottom-color: #E5E7EB;
            border-right-color: #E5E7EB;

            border-radius: 8px;
        }
    """


    #"color: #7F1D1D; "
        #"border: 1px solid #585959; "
        #"background-color: #FECACA; "

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
        "QLabel {"
        "color: #E5E7EB; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: #374151; "

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    tableWidget_zp = (
        "QTableWidget {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_all_zp = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_total_zp = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_all_zp_summ = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_total_zp_summ = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
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
        "QLabel {"
        "color: #E5E7EB; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: #374151; "

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    tableWidget_avans = (
        "QTableWidget {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_all_avans = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_total_avans = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_all_avans_summ = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
    )

    label_total_avans_summ = (
        "QLabel {"
        "color: #374151; "
        "font-size: 12px; "
        "font-weight: 500; "
        "padding: 6px 8px; "

        "background-color: qlineargradient("
        "x1:0, y1:0, x2:0, y2:1, "
        "stop:0 #E5E7EB, "
        "stop:0.5 #F3F4F6, "
        "stop:1 #FFFFFF"
        ");"

        "border: 1px solid #D1D5DB; "
        "border-top-color: #9CA3AF; "
        "border-left-color: #9CA3AF; "
        "border-radius: 8px; "
        "}"
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
            color: #374151;
            font-size: 16px;
            font-weight: 500;
            padding: 0px 20px;

            /* базовый утопленный вид */
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #E5E7EB,
                stop:0.5 #F3F4F6,
                stop:1 #FFFFFF
            );

            border: 1px solid #D1D5DB;
            border-top-color: #9CA3AF;
            border-left-color: #9CA3AF;
            border-bottom-color: #E5E7EB;
            border-right-color: #E5E7EB;

            border-radius: 8px;
        }

        /* hover — слегка "поднимается" */
        QPushButton:hover {
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #F3F4F6,
                stop:1 #FFFFFF
            );
        }

        /* pressed — реально утоплен */
        QPushButton:pressed {
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #D1D5DB,
                stop:1 #E5E7EB
            );

            border-top-color: #6B7280;
            border-left-color: #6B7280;
        }
    """

    pushButton_next = """
        QPushButton {
            color: #374151;
            font-size: 16px;
            font-weight: 500;
            padding: 0px 20px;

            /* базовый утопленный вид */
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #E5E7EB,
                stop:0.5 #F3F4F6,
                stop:1 #FFFFFF
            );

            border: 1px solid #D1D5DB;
            border-top-color: #9CA3AF;
            border-left-color: #9CA3AF;
            border-bottom-color: #E5E7EB;
            border-right-color: #E5E7EB;

            border-radius: 8px;
        }

        /* hover — слегка "поднимается" */
        QPushButton:hover {
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #F3F4F6,
                stop:1 #FFFFFF
            );
        }

        /* pressed — реально утоплен */
        QPushButton:pressed {
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #D1D5DB,
                stop:1 #E5E7EB
            );

            border-top-color: #6B7280;
            border-left-color: #6B7280;
        }
    """

    label_month = (
        "color: #4B5563; "
        "background-color: #FFFFFF; "
    )

    tableWidget_calendar = """
        QTableWidget {
            color: #374151;
            font-size: 12px;

            /* эффект вдавленности */
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #E5E7EB,
                stop:0.5 #F3F4F6,
                stop:1 #FFFFFF
            );

            border: 1px solid #D1D5DB;
            border-top-color: #9CA3AF;
            border-left-color: #9CA3AF;
            border-bottom-color: #E5E7EB;
            border-right-color: #E5E7EB;

            border-radius: 12px;
            gridline-color: transparent;
        }

        /* Ячейки */
        QTableWidget::item {
            background: transparent;
            padding: 4px 6px;
        }

        /* Заголовки столбцов */
        QHeaderView::section {
            color: #374151;
            background-color: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #E5E7EB,
                stop:1 #F3F4F6
            );
            font-weight: 600;
            font-size: 12px;
            border: none;
            padding: 4px 6px;
        }

        /* Верхние углы */
        QHeaderView::section:horizontal:first {
            border-top-left-radius: 12px;
        }

        QHeaderView::section:horizontal:last {
            border-top-right-radius: 12px;
        }
    """