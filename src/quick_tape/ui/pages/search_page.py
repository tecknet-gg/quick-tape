from PySide6.QtCore import QThread
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

from quick_tape.core.search_worker import SearchWorker
from quick_tape.ui.components.release_scroll import ReleaseScroll

import time

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

        self.search_input.returnPressed.connect(self.on_search)
        #self.search_input.textChanged.connect(self.on_search)
        self.search_button.clicked.connect(self.on_search)

        self.release_list = ReleaseScroll()
        self.layout.addWidget(self.release_list, 1)

        self.layout.addStretch()
        self.setLayout(self.layout)

        self.worker = None
        self.worker_thread = None



    def on_search(self):
        query = self.search_input.text().strip()
        if not query:
            return

        if self.worker_thread and self.worker_thread.isRunning():
            return

        self.search_button.setDisabled(True)
        self.search_button.setText("Searching...")

        self.worker_thread = QThread(self)
        self.worker = SearchWorker(query)

        self.worker.moveToThread(self.worker_thread)

        self.worker_thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.on_results)
        self.worker.error.connect(self.on_error)

        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.error.connect(self.worker_thread.quit)

        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        self.worker_thread.finished.connect(self._on_thread_finished)



        self.worker_thread.start()

    def on_results(self, results):
        self.release_list.set_releases(results)
        self.reset_search()

    def reset_search(self):
        self.search_button.setDisabled(False)
        self.search_button.setText("Search")

    def on_error(self, error):
        print(error)
        self.reset_search()

    def _on_thread_finished(self):
        self.worker_thread = None
        self.worker = None