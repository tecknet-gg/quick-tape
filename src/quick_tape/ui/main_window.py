from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QStackedWidget, QFrame
from quick_tape.ui.sidebar import Sidebar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("quick-tape")
        self.resize(800, 600)

        self.setMinimumWidth(800)
        self.setMinimumHeight(600)


        self.sidebar = Sidebar()
        self.divider = QFrame()

        self.divider.setFrameShape(QFrame.Shape.VLine)
        self.divider.setFrameShadow(QFrame.Shadow.Sunken)

        self.pages = QStackedWidget()

        self.central_widget = QWidget()

        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.sidebar, 0)
        self.central_layout.addWidget(self.divider)
        self.central_layout.addWidget(self.pages, 1)

        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)



