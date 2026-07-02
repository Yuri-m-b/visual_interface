"""Interface generator for the interface"""

import sys
import random
import time
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import QSize, QTimer, Slot, Qt
from PySide6.QtGui import QIcon, QPixmap

FIGURE_MAPPING = {
    "figure1": "images/cats_1.png",
    "figure2": "images/cats_2.png",
    "figure3": "images/i_love_you.png",
    "figure4": "images/cats_3.png",
    "figure5": "images/dis_for_you.png",
    "figure6": "images/cats_4.png",
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
        pixmap2 = QPixmap(FIGURE_MAPPING["figure3"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        figure_label2 = QLabel(self)
        figure_label2.setPixmap(pixmap2)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(figure_label2, alignment=Qt.AlignmentFlag.AlignRight)

        text_label = QLabel("Para a mulher da minha vida!!", self)
        text_label.setObjectName("title")
        text_label.resize(500, 100)
        text_label.move(400, 50)

        button = QPushButton("Te amooooo!!", self)
        button.resize(300, 100)
        button.move(450, 250)
        button.clicked.connect(lambda: self.stack.setCurrentIndex(4))


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
        sim_btn.clicked.connect(lambda: self.stack.setCurrentIndex(2))

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
        pixmap = QPixmap(FIGURE_MAPPING["figure4"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        text_label = QLabel("Qual imagem representa mais a gente?", self)
        text_label.resize(500, 100)
        text_label.move(600, 200)

        button_1 = QPushButton(self)
        button_1.resize(300, 300)
        button_1.setStyleSheet("""
            QPushButton {
                border-image: url("images/us_1.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_1.move(400, 300)
        button_1.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        button_2 = QPushButton(self)
        button_2.resize(300, 300)
        button_2.setStyleSheet("""
            QPushButton {
                border-image: url("images/us_2.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_2.move(800, 300)
        button_2.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        button_3 = QPushButton(self)
        button_3.resize(300, 300)
        button_3.setStyleSheet("""
            QPushButton {
                border-image: url("images/us_3.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_3.move(400, 600)
        button_3.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        button_4 = QPushButton(self)
        button_4.resize(300, 300)
        button_4.setStyleSheet("""
            QPushButton {
                border-image: url("images/us_4.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_4.move(800, 600)
        button_4.clicked.connect(lambda: self.stack.setCurrentIndex(3))


class FourthPage(QWidget):
    """The fourth screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the fourth page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the fourth page."""
        layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure5"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        text_label = QLabel("Qual 'Eu te Amo' é verdadeiro?", self)
        text_label.resize(500, 100)
        text_label.move(650, 150)

        button_1 = QPushButton(self)
        button_1.resize(300, 300)
        button_1.move(450, 300)
        button_1.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_1.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_1.clicked.connect(lambda: self.stack.setCurrentIndex(4))

        button_2 = QPushButton(self)
        button_2.resize(300, 300)
        button_2.move(800, 300)
        button_2.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_2.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_2.clicked.connect(lambda: self.stack.setCurrentIndex(4))

        button_3 = QPushButton(self)
        button_3.resize(300, 300)
        button_3.move(450, 600)
        button_3.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_3.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_3.clicked.connect(lambda: self.stack.setCurrentIndex(4))

        button_4 = QPushButton(self)
        button_4.resize(300, 300)
        button_4.move(800, 600)
        button_4.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_4.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_4.clicked.connect(lambda: self.stack.setCurrentIndex(4))

        button_5 = QPushButton(self)
        button_5.resize(100, 100)
        button_5.move(750, 50)
        button_5.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_5.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        button_5.clicked.connect(lambda: self.stack.setCurrentIndex(4))


class FifthPage(QWidget):
    """The fifth screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the fifth page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the fifth page."""

        self.layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure6"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        self.layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        self.text_label = QLabel("Quantas vezes falamos 'Eu te amo' no whats.", self)
        self.text_label.resize(500, 100)
        self.text_label.move(600, 200)

        self.opt_btn_1 = QPushButton("700", self)
        self.opt_btn_1.resize(250, 50)
        self.opt_btn_1.move(550, 400)
        self.opt_btn_1.clicked.connect(self.middle_page)

        self.opt_btn_2 = QPushButton("100", self)
        self.opt_btn_2.resize(250, 50)
        self.opt_btn_2.move(850, 400)
        self.opt_btn_2.clicked.connect(self.middle_page)

        self.opt_btn_3 = QPushButton("1000", self)
        self.opt_btn_3.resize(250, 50)
        self.opt_btn_3.move(550, 500)
        self.opt_btn_3.clicked.connect(self.middle_page)

        self.opt_btn_4 = QPushButton("360", self)
        self.opt_btn_4.resize(250, 50)
        self.opt_btn_4.move(850, 500)
        self.opt_btn_4.clicked.connect(self.middle_page)

    def middle_page(self):
        """Page that will show only a label before it continue to the sixth page."""

        self.opt_btn_1.deleteLater()
        self.opt_btn_2.deleteLater()
        self.opt_btn_3.deleteLater()
        self.opt_btn_4.deleteLater()
        self.text_label.setText("TODOS OS MEUS EU TE AMO SÃO VERDADEIROS!!")

        QTimer.singleShot(3000, lambda: self.stack.setCurrentIndex(2))


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
