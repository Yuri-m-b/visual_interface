"""Interface generator for the interface"""

import sys
import random
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap

FIGURE_MAPPING = {
    "figure1": "images/cats_1.png",
    "figure2": "images/cats_2.png",
}


class FirstPage(QWidget):
    """The first romantic screen."""

    def __init__(self, stack_widget):
        """Initialize the first page and set up its UI."""
        super().__init__()
        self.stack = stack_widget  # Save reference to switch screens later
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the first page."""

        layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure1"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        text_label = QLabel("Para a mulher da minha vida!!", self)
        text_label.setObjectName("title")
        text_label.resize(500, 100)
        text_label.move(400, 50)

        button = QPushButton("Te amooooo!!", self)
        button.resize(300, 100)
        button.move(450, 250)
        button.clicked.connect(lambda: self.stack.setCurrentIndex(1))


class SecondPage(QWidget):
    """The second screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the second page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the second page."""
        layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure2"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        text_label = QLabel("Você concorda que eu te amo mais?", self)
        text_label.resize(500, 100)
        text_label.move(600, 200)

        sim_btn = QPushButton("Sim", self)
        sim_btn.resize(250, 50)
        sim_btn.move(500, 400)
        sim_btn.clicked.connect(QApplication.instance().quit)

        nao_btn = QPushButton("Não", self)
        nao_btn.resize(250, 50)
        nao_btn.move(800, 400)
        nao_btn.clicked.connect(lambda: self.move_button(nao_btn))

    def move_button(self, button):
        """Move the button to a random position within the window."""
        max_x = self.width() - button.width()
        max_y = self.height() - button.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        button.move(new_x, new_y)


class ThirdPage(QWidget):
    """The third screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the third page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the third page."""
        layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure2"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)


class MainWindow(QMainWindow):  # pylint: disable=too-few-public-methods
    """Main window class for the application."""

    def __init__(self):
        """Initialize the main window and set up the stacked widget."""
        super().__init__()
        self.unsetCursor()
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowTitle("Para a mulher mais linda desse mundo")

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.page1 = FirstPage(self.stacked_widget)
        self.page2 = SecondPage(self.stacked_widget)
        self.page3 = ThirdPage(self.stacked_widget)
        self.page4 = FourthPage(self.stacked_widget)
        self.page5 = FifthPage(self.stacked_widget)

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page4)
        self.stacked_widget.addWidget(self.page5)

        self.stacked_widget.setCurrentIndex(0)


@Slot()
def say_hello():
    """Test function"""
    print("Button clicked, Hello!")


def main():
    """Main function to run the application."""
    app = QApplication([])

    window = MainWindow()
    window.show()
    with open("interface/interface.css", "r", encoding="utf-8") as file:
        _style = file.read()
        app.setStyleSheet(_style)

    app.exec()


if __name__ == "__main__":
    main()
