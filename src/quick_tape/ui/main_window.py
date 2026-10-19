from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, \
    QStackedWidget, QFrame

from quick_tape.ui.pages.search_page import SearchPage
from quick_tape.ui.components.sidebar import Sidebar
from quick_tape.ui.pages import *
from quick_tape.ui.pages.settings_page import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_setup()
        self.init_sidebar()
        self.init_pages()
        self.init_layout()
        self.connect_signals()

    def ui_setup(self):
        self.setWindowTitle("quick-tape")
        self.resize(800, 600)

        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

    def init_pages(self):

        self.pages = QStackedWidget()
        self.search_page = SearchPage()
        self.settings_page = SettingsPage()
        self.pages.addWidget(self.search_page) #add search page
        self.pages.addWidget(self.settings_page)

    def init_layout(self):
        self.central_widget = QWidget()

        self.central_layout = QHBoxLayout()
        self.central_layout.addWidget(self.sidebar, 0)
        self.central_layout.addWidget(self.divider)
        self.central_layout.addWidget(self.pages, 1)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def init_sidebar(self):
        self.sidebar = Sidebar()
        self.divider = QFrame()

        self.divider.setFrameShape(QFrame.Shape.VLine)
        self.divider.setFrameShadow(QFrame.Shadow.Sunken)

    def connect_signals(self):
        # connect sidebar nav signals
        self.sidebar.nav_search.clicked.connect(self.open_search)
        self.sidebar.nav_prepare.clicked.connect(self.open_prepare)
        self.sidebar.nav_record.clicked.connect(self.open_record)
        self.sidebar.nav_library.clicked.connect(self.open_library)
        self.sidebar.nav_register.clicked.connect(self.open_register)
        self.sidebar.nav_jobs.clicked.connect(self.open_jobs)
        self.sidebar.nav_settings.clicked.connect(self.open_settings)


    def open_search(self):
        self.pages.setCurrentIndex(0)
        print("opening search")

    def open_prepare(self):
        self.pages.setCurrentIndex(6)
        print("opening prepare")

    def open_record(self):
        self.pages.setCurrentIndex(2)
        print("opening record")

    def open_library(self):
        self.pages.setCurrentIndex(3)
        print("opening library")

    def open_register(self):
        self.pages.setCurrentIndex(4)
        print("opening register")

    def open_jobs(self):
        self.pages.setCurrentIndex(5)
        print("opening jobs")

    def open_settings(self):
        self.pages.setCurrentIndex(1)
        print("opening settings")




