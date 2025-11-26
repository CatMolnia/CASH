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
        "color: #2E2F33; "
        "background-color: #F1F2F3; "
        "border-radius: 6px; "
        "padding: 4px 10px; "
        "font-size: 10px;"
    )