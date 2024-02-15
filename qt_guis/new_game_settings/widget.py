# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from qt_guis.new_game_settings.ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.difficulty_combo_box
        self.ui.


def retrieve_values(self):
    # Retrieves value form Qpy
    player_name: str = self.ui.player_name_line_edit
    difficulty: str = self.ui.difficulty_combo_box



def run_ui() -> None:
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
