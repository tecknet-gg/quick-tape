from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.setMinimumWidth(180)


        self.search_button = QPushButton("Search")
        self.search_button.setMinimumHeight(50)
        self.search_button.setMinimumWidth(50)
        self.layout.addWidget(self.search_button)

        self.record_button = QPushButton("Record")
        self.record_button.setMinimumHeight(50)
        self.record_button.setMinimumWidth(50)
        self.layout.addWidget(self.record_button)

        self.layout.addStretch()

        self.setLayout(self.layout)

