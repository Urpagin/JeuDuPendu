from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# Create an instance of QApplication
app = QApplication([])

# Create an in stance of QWidget which will be the main window
window = QWidget()
window.setWindowTitle('Hello World App')  # Set the window title
window.setGeometry(100, 100, 280, 80)  # Set the window size and position

# Create a QLabel widget to display 'Hello World'
label = QLabel('Hello World', parent=window)
label.move(90, 20)  # Position the label inside the window

# Show the window
window.show()

# Execute the application's main loop
app.exec()
