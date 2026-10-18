from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.setMinimumWidth(180)


        self.search_button = self.init_button(text="search")
        self.prepare_button = self.init_button(text="prepare")
        self.record_button = self.init_button(text="record")
        self.library_button = self.init_button(text="library")
        self.register_button = self.init_button(text="register")
        self.jobs_button = self.init_button(text="jobs")
        self.settings_button = self.init_button(text="settings")

        button = [
            self.search_button,
            self.prepare_button,
            self.record_button,
            self.library_button,
            self.register_button,
            self.jobs_button,
            self.settings_button
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




