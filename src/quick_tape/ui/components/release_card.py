from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QPushButton
import requests




class ReleaseCard(QFrame):
    def __init__(self, release):
        super().__init__()

        self.title = release.title
        self.artist = release.artist.name
        self.cover_url = release.cover_xl
        self.num_tracks = release.nb_tracks
        self.tracklist = release.get_tracks()
        self.duration = f"{round(release.duration/60, 1)} minutes" # format duration better
        self.release_date = str(getattr(release, "release_date", None) or "Unknown")

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

        main_layout.addWidget(self.cover_image)
        self.content_info_main = QVBoxLayout()

        layer_1 = QHBoxLayout()
        title = QLabel(self.title)
        layer_1.addWidget(title)

        layer_2 = QHBoxLayout()
        artist = QLabel(self.artist)
        layer_2.addWidget(artist)

        layer_3 = QHBoxLayout()
        duration = QLabel(self.duration)
        track_count = QLabel(f"{self.num_tracks} tracks")

        layer_3.addWidget(duration)
        layer_3.addWidget(track_count)

        layer_4 = QHBoxLayout()
        release_date = QLabel(self.release_date)
        layer_4.addWidget(release_date)

        self.content_info_main.addLayout(layer_1)
        self.content_info_main.addLayout(layer_2)
        self.content_info_main.addLayout(layer_3)
        self.content_info_main.addLayout(layer_4)

        self.show_tracks_button = QPushButton("Show tracks")
        self.content_info_main.addWidget(self.show_tracks_button)
        #self.content_info_main.addStretch()

        self.download_release_button = QPushButton("Download release")
        self.content_info_main.addWidget(self.download_release_button)

        self.show_tracks_button.clicked.connect(self.show_tracks)

        main_layout.addLayout(self.content_info_main, 1)

    def show_tracks(self):
        print(self.tracklist)

    def download_release(self):
        pass




