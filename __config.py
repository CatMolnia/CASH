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
    label_title = (
        "color: black; "
        "background-color: #F1F2F3; "
        "border-radius: 6px; "
        "padding: 4px 10px; "
        "font-size: 12px; "
        "font-weight: 800;"
    )

    label_calendar = (
        "color: white; "
        "background-color: #805A3B; "
        "border-radius: 6px; "
        "padding: 4px 10px; "
        "font-size: 10px; "
        "font-weight: 500;"
    )

    label_work = (
        "color: white; "
        "background-color: #805A3B; "
        "border-radius: 6px; "
        "padding: 4px 10px; "
        "font-size: 10px; "
        "font-weight: 500;"
    )

    label_weekend = (
        "color: white; "
        "background-color: #805A3B; "
        "border-radius: 6px; "
        "padding: 4px 10px; "
        "font-size: 10px; "
        "font-weight: 500;"
    )

    general_information = {
        "style": (
            "QWidget#general_information { "
            "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
            "stop:0 #F8EDE0, stop:1 #E6D6C8); "
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