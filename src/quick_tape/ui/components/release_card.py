from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
import deezer


class ReleaseCard(QFrame):
    def __init__(self, release):
        super().__init__()

        self.title = release.title
        self.artist = release.artist.name
        self.cover = release.cover_small
        self.num_tracks = release.nb_tracks
        self.tracklist = release.get_tracks()
        self.release_date = getattr(release, "release_date", None) or "Unknown"

        #print(self.title, self.artist, self.cover, self.tracklist, self.num_tracks)
        #print(self.release_date)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(12,12,12,12)
        main_layout.setSpacing(16)

        self.setObjectName("releaseCard")

        self.cover_image = QLabel()
        self.cover_image.setMinimumSize(140,140)
        self.cover_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover_image.setText("Loading artwork")

        self.cover_image.setObjectName("albumArt")

        main_layout.addWidget(self.cover_image)

        content_layout = QVBoxLayout()
        content_layout.setSpacing(6)

        self.title_label = QLabel(self.title)
        self.title_label.setObjectName("releaseTitle")
        self.title_label.setWordWrap(True)

        self.artist_label = QLabel(self.artist)
        self.artist_label.setObjectName("releaseArtist")
        self.artist_label.setWordWrap(True)

        #self.release_date_label = QLabel(self.release_date)
        #self.release_date_label.setObjectName("releaseDate")


        content_layout.addWidget(self.title_label)
        content_layout.addWidget(self.artist_label)


        content_layout.addStretch()

        main_layout.addLayout(content_layout)



