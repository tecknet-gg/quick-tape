from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QPushButton, QWidget
import requests

class ReleaseCard(QFrame):
    def __init__(self, release):
        super().__init__()

        self.title = release.title
        self.artist = release.artist.name
        self.cover_url = release.cover_xl
        self.num_tracks = release.nb_tracks
        self.tracklist = release.get_tracks()
        self.duration = f"{round(release.duration / 60, 1)} minutes"
        self.release_date = str(getattr(release, "release_date", None) or "Unknown")

        self.tracks_shown = False

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(12, 12, 12, 12)
        self.main_layout.setSpacing(10)


        self.top_layout = QHBoxLayout()
        self.top_layout.setSpacing(16)

        self.cover_image = QLabel("Loading cover image")
        self.cover_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover_image.setFixedSize(140, 140)

        self.top_layout.addWidget(self.cover_image)

        self.content_info_main = QVBoxLayout()

        self.content_info_main.addWidget(QLabel(self.title))
        self.content_info_main.addWidget(QLabel(self.artist))

        metadata_layout = QHBoxLayout()
        metadata_layout.addWidget(QLabel(self.duration))
        metadata_layout.addWidget(QLabel(f"{self.num_tracks} tracks"))

        self.content_info_main.addLayout(metadata_layout)
        self.content_info_main.addWidget(QLabel(self.release_date))

        self.top_layout.addLayout(self.content_info_main, 1)
        self.main_layout.addLayout(self.top_layout)


        self.track_list_widget = QWidget()
        self.track_list_layout = QVBoxLayout(self.track_list_widget)
        self.track_list_layout.setContentsMargins(0, 0, 0, 0)
        self.track_list_widget.hide()


        self.show_tracks_button = QPushButton("Show tracks")
        self.download_release_button = QPushButton("Download release")

        self.main_layout.addWidget(self.show_tracks_button)
        self.main_layout.addWidget(self.track_list_widget)
        self.main_layout.addWidget(self.download_release_button)

        self.show_tracks_button.clicked.connect(self.show_tracks)
        self.download_release_button.clicked.connect(self.download_release)


        response = requests.get(self.cover_url)
        response.raise_for_status()

        pixmap = QPixmap()
        if pixmap.loadFromData(response.content):
            self.cover_image.setPixmap(
                pixmap.scaled(
                    self.cover_image.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        else:
            self.cover_image.setText("Artwork unavailable")


    def show_tracks(self):
        if self.tracks_shown:
            self.show_tracks_button.setText("Show tracks")
            self.track_list_widget.hide()
            self.tracks_shown = False
            return

        self.show_tracks_button.setText("Hide tracks")
        self.tracks_shown = True

        if self.track_list_layout.count() == 0:
            for i, track in enumerate(self.tracklist):
                track_layout = QHBoxLayout()

                track_title = QLabel(track.title)
                track_duration = QLabel(f"{round(track.duration/60, 1)} minutes")

                track_layout.addWidget(track_title)
                track_layout.addWidget(track_duration)

                self.track_list_layout.addLayout(track_layout)

        self.track_list_widget.show()


    def download_release(self):
        pass




