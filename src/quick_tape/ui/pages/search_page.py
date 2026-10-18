from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QScrollArea
from quick_tape.ui.components.release_card import ReleaseCard
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

        self.results_layout = QVBoxLayout()

        self.layout.addLayout(self.search_layout)


    def on_search(self):
        query = self.search_input.text()
        if not query:
            return


        results = search(query)

        while self.results_layout.count():
            item = self.results_layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()


        for result in results:
            card = ReleaseCard(result)
            self.results_layout.addWidget(card)

        self.results_layout.addStretch()
