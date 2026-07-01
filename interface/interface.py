"""Interface generator for the interface"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap

FIGURE_MAPPING = {
    "figure1": "images/cats_1.png",
}


class MainWindow(QMainWindow):
    """Main window class for the application."""

    def __init__(self):
        super().__init__()

        self.unsetCursor()

        button = QPushButton("Te amo!")
        button.setFixedSize(200, 150)
        button.pressed.connect(self.close)

        figure_label = QLabel(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure1"])
        figure_label.setPixmap(pixmap)
        figure_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        figure_label.size().setHeight(400)

        content_layout = QVBoxLayout()
        content_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)
        content_layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignBottom)
        container = QWidget()
        container.setLayout(content_layout)
        self.setCentralWidget(container)
        self.show()


@Slot()
def say_hello():
    """Test function"""
    print("Button clicked, Hello!")


def main():
    """Main function to run the application."""
    app = QApplication([])

    window = MainWindow()
    window.resize(1200, 800)
    with open("interface/interface.css", "r", encoding="utf-8") as file:
        _style = file.read()
        app.setStyleSheet(_style)

    app.exec()


if __name__ == "__main__":
    main()
