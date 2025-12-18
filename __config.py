from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass(frozen=True)
class AppWindowConfig:
    sizes: Dict[str, Tuple[int, int]] = field(
        default_factory=lambda: {
            "default": (1500, 680)
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