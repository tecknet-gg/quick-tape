from PySide6.QtCore import QObject
from PySide6.QtCore import Signal, Slot
from quick_tape.core.search import search


class SearchWorker(QObject):
    finished = Signal(list)
    error = Signal(str)

    def __init__(self, query: str):
        super().__init__()
        self.query = query

    @Slot()
    def run(self):
        try:
            results = search(self.query)
            self.finished.emit(results)
        except Exception as e:
            self.error.emit(str(e))


