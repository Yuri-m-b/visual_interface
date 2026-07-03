"""Interface generator for the interface"""

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
from PySide6.QtCore import QTimer, Slot, Qt
from PySide6.QtGui import QPixmap

FIGURE_MAPPING = {
    "figure1": "images/cats_1.png",
    "figure2": "images/cats_2.png",
    "figure3": "images/i_love_you.png",
    "figure4": "images/cats_3.png",
    "figure5": "images/dis_for_you.png",
    "figure6": "images/cats_4.png",
    "figure7": "images/cats_5.png",
    "figure8": "images/cats_6.png",
    "figure9": "images/teamo_1.png",
    "figure10": "images/ss_1.png",
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

        self.text_label = QLabel("Qual 'Eu te Amo' é verdadeiro?", self)
        self.text_label.resize(500, 100)
        self.text_label.move(650, 150)

        self.button_1 = QPushButton(self)
        self.button_1.resize(300, 300)
        self.button_1.move(450, 300)
        self.button_1.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_1.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_1.clicked.connect(self.middle_page)

        self.button_2 = QPushButton(self)
        self.button_2.resize(300, 300)
        self.button_2.move(800, 300)
        self.button_2.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_2.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_2.clicked.connect(self.middle_page)

        self.button_3 = QPushButton(self)
        self.button_3.resize(300, 300)
        self.button_3.move(450, 600)
        self.button_3.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_3.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_3.clicked.connect(self.middle_page)

        self.button_4 = QPushButton(self)
        self.button_4.resize(300, 300)
        self.button_4.move(800, 600)
        self.button_4.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_4.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_4.clicked.connect(self.middle_page)

        self.button_5 = QPushButton(self)
        self.button_5.resize(100, 100)
        self.button_5.move(750, 50)
        self.button_5.setStyleSheet("""
            QPushButton {
                border-image: url("images/amo_5.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_5.clicked.connect(self.middle_page)

    def middle_page(self):
        """Page that will show only a label before it continue to the sixth page."""

        self.button_1.deleteLater()
        self.button_2.deleteLater()
        self.button_3.deleteLater()
        self.button_4.deleteLater()
        self.button_5.deleteLater()
        self.text_label.setText("TODOS OS MEUS EU TE AMO SÃO VERDADEIROS!!")

        QTimer.singleShot(3000, lambda: self.stack.setCurrentIndex(4))


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

        opt_btn_1 = QPushButton("100", self)
        opt_btn_1.resize(250, 50)
        opt_btn_1.move(550, 400)
        opt_btn_1.clicked.connect(
            lambda checked=False, btn=opt_btn_1: self.fail_attempt(btn)
        )

        opt_btn_2 = QPushButton("700", self)
        opt_btn_2.resize(250, 50)
        opt_btn_2.move(850, 400)
        opt_btn_2.clicked.connect(lambda: self.stack.setCurrentIndex(5))

        opt_btn_3 = QPushButton("1000", self)
        opt_btn_3.resize(250, 50)
        opt_btn_3.move(550, 500)
        opt_btn_3.clicked.connect(
            lambda checked=False, btn=opt_btn_3: self.fail_attempt(btn)
        )

        opt_btn_4 = QPushButton("360", self)
        opt_btn_4.resize(250, 50)
        opt_btn_4.move(850, 500)
        opt_btn_4.clicked.connect(
            lambda checked=False, btn=opt_btn_4: self.fail_attempt(btn)
        )

    def fail_attempt(self, button_clicked):
        """Handle the case when the user fails to select an image."""
        button_clicked.deleteLater()


class SixthPage(QWidget):
    """The sixth screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the sixth page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the sixth page."""
        layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure7"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        text_label = QLabel(
            "Todos os meus momentos com vocês são os mais belos que já tive!", self
        )
        text_label.resize(1000, 100)
        text_label.move(450, 200)

        self.button_1 = QPushButton(self)
        self.button_1.resize(300, 300)
        self.button_1.move(450, 300)
        self.button_1.setStyleSheet("""
            QPushButton {
                border-image: url("images/nos_1.jpeg") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_1.clicked.connect(lambda: self.stack.setCurrentIndex(6))

        self.button_2 = QPushButton(self)
        self.button_2.resize(300, 300)
        self.button_2.move(800, 300)
        self.button_2.setStyleSheet("""
            QPushButton {
                border-image: url("images/nos_2.jpeg") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_2.clicked.connect(lambda: self.stack.setCurrentIndex(6))

        self.button_3 = QPushButton(self)
        self.button_3.resize(300, 300)
        self.button_3.move(450, 600)
        self.button_3.setStyleSheet("""
            QPushButton {
                border-image: url("images/nos_3.jpeg") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_3.clicked.connect(lambda: self.stack.setCurrentIndex(6))

        self.button_4 = QPushButton(self)
        self.button_4.resize(300, 300)
        self.button_4.move(800, 600)
        self.button_4.setStyleSheet("""
            QPushButton {
                border-image: url("images/nos_4.jpeg") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_4.clicked.connect(lambda: self.stack.setCurrentIndex(6))


class SeventhPage(QWidget):
    """The seventh screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the seventh page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the seventh page."""
        layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure8"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        text_label = QLabel("Te AMO em TODOS os momentos", self)
        text_label.resize(1000, 100)
        text_label.move(450, 200)

        self.button_1 = QPushButton(self)
        self.button_1.resize(300, 300)
        self.button_1.move(450, 300)
        self.button_1.setStyleSheet("""
            QPushButton {
                border-image: url("images/vc_1.jpeg") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_1.clicked.connect(lambda: self.stack.setCurrentIndex(7))

        self.button_2 = QPushButton(self)
        self.button_2.resize(300, 300)
        self.button_2.move(800, 300)
        self.button_2.setStyleSheet("""
            QPushButton {
                border-image: url("images/vc_2.jpeg") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_2.clicked.connect(lambda: self.stack.setCurrentIndex(7))

        self.button_3 = QPushButton(self)
        self.button_3.resize(300, 300)
        self.button_3.move(450, 600)
        self.button_3.setStyleSheet("""
            QPushButton {
                border-image: url("images/vc_3.jpeg") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_3.clicked.connect(lambda: self.stack.setCurrentIndex(7))

        self.button_4 = QPushButton(self)
        self.button_4.resize(300, 300)
        self.button_4.move(800, 600)
        self.button_4.setStyleSheet("""
            QPushButton {
                border-image: url("images/vc_4.jpeg") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_4.clicked.connect(lambda: self.stack.setCurrentIndex(7))


class EighthPage(QWidget):
    """The eighth screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the eighth page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the eighth page."""
        layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure9"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        text_label = QLabel("TE AMO TE AMO TE AMO TE AMO TE AMO TE AMO TE AMO", self)
        text_label.resize(1000, 100)
        text_label.move(600, 100)

        self.button_1 = QPushButton(self)
        self.button_1.resize(400, 600)
        self.button_1.move(650, 200)
        self.button_1.setStyleSheet("""
            QPushButton {
                border-image: url("images/ss_1.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)
        self.button_1.clicked.connect(lambda: self.stack.setCurrentIndex(8))


class NingthyPage(QWidget):
    """The ninth screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the ninth page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the ninth page."""
        layout = QVBoxLayout(self)
        pixmap = QPixmap(FIGURE_MAPPING["figure10"])
        figure_label = QLabel(self)
        figure_label.setPixmap(pixmap)
        layout.addWidget(figure_label, alignment=Qt.AlignmentFlag.AlignLeft)

        text_label = QLabel("TE AMO TE AMO TE AMO TE AMO TE AMO TE AMO TE AMO", self)
        text_label.resize(1000, 100)
        text_label.move(500, 200)

        text_label = QLabel("Qual adjetivo você gosta mais?", self)
        text_label.resize(1000, 100)
        text_label.move(630, 300)

        opt_btn_1 = QPushButton("Amor", self)
        opt_btn_1.resize(250, 50)
        opt_btn_1.move(550, 400)
        opt_btn_1.clicked.connect(lambda: self.stack.setCurrentIndex(9))

        opt_btn_2 = QPushButton("Vida", self)
        opt_btn_2.resize(250, 50)
        opt_btn_2.move(850, 400)
        opt_btn_2.clicked.connect(lambda: self.stack.setCurrentIndex(9))

        opt_btn_3 = QPushButton("Bida", self)
        opt_btn_3.resize(250, 50)
        opt_btn_3.move(550, 500)
        opt_btn_3.clicked.connect(lambda: self.stack.setCurrentIndex(9))

        opt_btn_4 = QPushButton("Biluga", self)
        opt_btn_4.resize(250, 50)
        opt_btn_4.move(850, 500)
        opt_btn_4.clicked.connect(lambda: self.stack.setCurrentIndex(9))

        opt_btn_5 = QPushButton("Princesa", self)
        opt_btn_5.resize(250, 50)
        opt_btn_5.move(550, 600)
        opt_btn_5.clicked.connect(lambda: self.stack.setCurrentIndex(9))

        opt_btn_6 = QPushButton("Gata", self)
        opt_btn_6.resize(250, 50)
        opt_btn_6.move(850, 600)
        opt_btn_6.clicked.connect(lambda: self.stack.setCurrentIndex(9))


class TenthPage(QWidget):
    """The tenth screen that loads next."""

    def __init__(self, stack_widget):
        """Initialize the tenth page and set up its UI."""
        super().__init__()
        self.stack = stack_widget
        self.init_ui()

    def init_ui(self):
        """Set up the UI for the tenth page."""

        self.button_1 = QPushButton(self)
        self.button_1.resize(600, 600)
        self.button_1.move(330, 200)
        self.button_1.setStyleSheet("""
            QPushButton {
                border-image: url("images/fim.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)

        self.button_2 = QPushButton(self)
        self.button_2.resize(300, 300)
        self.button_2.move(0, 0)
        self.button_2.setStyleSheet("""
            QPushButton {
                border-image: url("images/cats_7.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)

        self.button_3 = QPushButton(self)
        self.button_3.resize(300, 300)
        self.button_3.move(0, 650)
        self.button_3.setStyleSheet("""
            QPushButton {
                border-image: url("images/cats_8.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)

        self.button_4 = QPushButton(self)
        self.button_4.resize(300, 300)
        self.button_4.move(900, 0)
        self.button_4.setStyleSheet("""
            QPushButton {
                border-image: url("images/cats_9.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)

        self.button_5 = QPushButton(self)
        self.button_5.resize(300, 300)
        self.button_5.move(900, 650)
        self.button_5.setStyleSheet("""
            QPushButton {
                border-image: url("images/cats_10.png") 0 0 0 0 stretch stretch;
                border: none;
            }
        """)

        QTimer.singleShot(20000, lambda: self.stack.setCurrentIndex(0))


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
        self.page6 = SixthPage(self.stacked_widget)
        self.page7 = SeventhPage(self.stacked_widget)
        self.page8 = EighthPage(self.stacked_widget)
        self.page9 = NingthyPage(self.stacked_widget)
        self.page10 = TenthPage(self.stacked_widget)

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page4)
        self.stacked_widget.addWidget(self.page5)
        self.stacked_widget.addWidget(self.page6)
        self.stacked_widget.addWidget(self.page7)
        self.stacked_widget.addWidget(self.page8)
        self.stacked_widget.addWidget(self.page9)
        self.stacked_widget.addWidget(self.page10)

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
