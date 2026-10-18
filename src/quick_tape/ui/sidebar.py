from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.setMinimumWidth(180)


        self.nav_search = self.init_button(text="search")
        self.nav_prepare = self.init_button(text="prepare")
        self.nav_record = self.init_button(text="record")
        self.nav_library = self.init_button(text="library")
        self.nav_register = self.init_button(text="register")
        self.nav_jobs = self.init_button(text="jobs")
        self.nav_settings = self.init_button(text="settings")

        button = [
            self.nav_search,
            self.nav_prepare,
            self.nav_record,
            self.nav_library,
            self.nav_register,
            self.nav_jobs,
            self.nav_settings
        ]

        for button in button:
            self.layout.addWidget(button)

        self.layout.addStretch()

        self.setLayout(self.layout)

    def init_button(self, text:str, min_height:int=50, min_width:int=50):
        button = QPushButton(text)
        button.setMinimumHeight(min_height)
        button.setMinimumWidth(min_width)
        return button




