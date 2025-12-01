from PyQt6.QtWidgets import QWidget
from __config import AppWindowConfig, GeneralInformation

class StartWindow:
    def __init__(self, config: AppWindowConfig, general_information: GeneralInformation):
        self.config = config
        self.general_information = general_information

    def apply(self, widget: QWidget):
        # размер окна
        sizes = self.config.sizes
        size_key = self.config.default_size
        width, height = sizes.get(size_key, next(iter(sizes.values())))
        widget.resize(width, height)

        # general_information
        # ___label_title___
        widget.ui.label_title.setStyleSheet(self.general_information.label_title)
        widget.ui.label_calendar.setStyleSheet(self.general_information.label_calendar)
        widget.ui.label_work.setStyleSheet(self.general_information.label_work)
        widget.ui.label_weekend.setStyleSheet(self.general_information.label_weekend)