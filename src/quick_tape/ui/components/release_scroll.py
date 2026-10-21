from PySide6.QtWidgets import QFrame, QScrollArea, QVBoxLayout, QSizePolicy
from quick_tape.ui.components.release_card import ReleaseCard
from PySide6.QtCore import Qt


class ReleaseScroll(QScrollArea):
    def __init__(self, releases=None):
        super().__init__()



        self.setWidgetResizable(True)

        self.container = QFrame()
        self.results_layout = QVBoxLayout(self.container)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.container.setMinimumWidth(0)
        self.results_layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetNoConstraint)

        self.setWidget(self.container)
        releases = []
        self.set_releases(releases or [])

    def set_releases(self, releases=[]):
        while self.results_layout.count():
            item = self.results_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()


        for release in releases:
            card = ReleaseCard(release)
            card.setMinimumWidth(0)
            card.setSizePolicy(
                QSizePolicy.Policy.Ignored,
                QSizePolicy.Policy.Preferred,
            )
            self.results_layout.addWidget(card)

        self.results_layout.addStretch()




