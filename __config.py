from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass(frozen=True)
class AppWindowConfig:
    sizes: Dict[str, Tuple[int, int]] = field(
        default_factory=lambda: {
            "default": (1024, 768)
        }
    )
    
    default_size: str = "default"

class GeneralInformation:
    general_information = {
        "style": (
            "QWidget#general_information { "
            "background-color: white; "
            "border: none; "
            "border-radius: 12px; "
            "margin: 0px 2px 6px 2px; "
            "}"
        ),
        "shadow": {
            "blur_radius": 15,
            "x_offset": 4,
            "y_offset": 4,
            "color": (0, 0, 0, 80)  # RGBA: черный с прозрачностью 80/255
        }
    }
    
    label_title = (
        "color: #4B5563; "
        "background-color: white; "
        "border: none; "
        "font-size: 16px; "
        "font-weight: 800;"
    )

    label_calendar = (
        "color: #4B5563; "
        "border: none; "
        "background-color: #CBD5E1; "
        "border-radius: 8px; "
        "padding: 6px 12px; "
        "font-size: 11px; "
        "font-weight: 500;"
    )

    label_work = (
        "color: #4B5563; "
        "border: none; "
        "background-color: #CBD5E1; "
        "border-radius: 8px; "
        "padding: 6px 12px; "
        "font-size: 11px; "
        "font-weight: 500;"
    )

    label_weekend = (
        "color: #4B5563; "
        "border: none; "
        "background-color: #CBD5E1; "
        "border-radius: 8px; "
        "padding: 6px 12px; "
        "font-size: 11px; "
        "font-weight: 500;"
    )

    