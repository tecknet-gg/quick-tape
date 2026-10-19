from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout
import requests




class ReleaseCard(QFrame):
    def __init__(self, release):
        super().__init__()

        self.title = release.title
        self.artist = release.artist.name
        self.cover_url = release.cover_xl
        self.num_tracks = release.nb_tracks
        self.tracklist = release.get_tracks()
        self.release_date = getattr(release, "release_date", None) or "Unknown"

        #print(self.title, self.artist, self.cover, self.tracklist, self.num_tracks)
        #print(self.release_date)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(16)

        self.cover_image = QLabel("Loading cover image")
        self.cover_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover_image.setFixedSize(140, 140) # let it scale later


        response = requests.get(self.cover_url)
        response.raise_for_status()

        pixmap = QPixmap()
        pixmap.loadFromData(response.content)

        self.cover_image.setPixmap(
            pixmap.scaled(
                self.cover_image.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )


        self.cover_image.setFixedSize(140, 140)
        main_layout.addWidget(self.cover_image)

        self.content_info = QVBoxLayout()
        main_layout.addLayout(self.content_info, 1)

        self.title_label = QLabel(self.title)
        self.title_label.setWordWrap(True)
        self.content_info.addWidget(self.title_label)

        self.artist_label = QLabel(self.artist)
        self.artist_label.setWordWrap(True)
        self.content_info.addWidget(self.artist_label)




