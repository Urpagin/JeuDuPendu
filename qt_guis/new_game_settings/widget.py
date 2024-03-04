from PySide6.QtWidgets import QApplication, QWidget
import json
from qt_guis.new_game_settings.ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect the exit button to the close function
        self.ui.pushButton.clicked.connect(self.close_window)

    def close_window(self):
        # This method closes the widget
        self.retrieve_values()
        self.close()

    def retrieve_values(self):
        # Retrieves value from UI
        player_name: str = self.ui.player_name_line_edit.text()  # .text() to get the text content
        difficulty_str: str = self.ui.difficulty_combo_box.currentText()  # .currentText() for the combo box selection
        language: str = self.ui.language_combo_box.currentText()  # .currentText() for the combo box selection

        if difficulty_str == 'Facile':
            difficulty = 0
        elif difficulty_str == 'Normal':
            difficulty = 1
        elif difficulty_str == 'Difficile':
            difficulty = 2
        elif difficulty_str == 'Infâme':
            difficulty = 3
        else:
            raise Exception('DIFFICULTY NOT FOUND!!!!!!!!!!!!')
            exit(-1)

        print(f'{difficulty_str=} & {difficulty=}')

        with open('info.json', 'w', encoding='utf-8') as f:
            vals = {
                'player_name': player_name,
                'difficulty': difficulty,
                'language': language
            }

            json.dump(vals, f)

        with open('language.txt', 'w', encoding='utf-8') as f:
            f.write(difficulty_str)

        with open('info.txt', 'w', encoding='utf-8') as f:
            f.write(player_name)

        return player_name, difficulty


def run_ui():
    # Check if a QApplication already exists; create it if not
    app = QApplication.instance()
    if not app:  # If no instance exists, create one
        app = QApplication([])

    widget = Widget()
    widget.show()
    app.exec()  # Run the Qt application

    # After the window is closed, the control returns here
    # You can retrieve values if needed before returning to Pygame

    # Now you can return to Pygame loop without exiting the application
    return


# Example usage from Pygame
if __name__ == "__main__":
    run_ui()
# Continue with your Pygame code here
