from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from quick_tape.ui.components.release_scroll import ReleaseScroll
from quick_tape.core.search import search

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

        self.search_button.clicked.connect(self.on_search)

        self.release_list = ReleaseScroll()
        self.layout.addWidget(self.release_list, 1)

        self.layout.addStretch()
        self.setLayout(self.layout)


    def on_search(self):
        query = self.search_input.text().strip()
        if not query:
            return

        print(f"Searching for {query}")
        results = search(query)

        self.release_list.set_releases(results)

