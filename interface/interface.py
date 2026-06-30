"""Interface generator for the interface"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    """Class representing the main window of the application."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello, World!")

        button = QPushButton("Exit")
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()


def main():
    """Main function to run the application."""
    app = QApplication([])
    window = MainWindow()
    app.exec()


if __name__ == "__main__":
    main()
