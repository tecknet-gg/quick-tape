from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


class SearchPage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.search_layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search for a release...")

        self.search_button = QPushButton("Search")

        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_button)

        self.layout.addLayout(self.search_layout)
        self.layout.addStretch()

        self.setLayout(self.layout)
