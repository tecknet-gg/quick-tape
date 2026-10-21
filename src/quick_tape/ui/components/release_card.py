from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QPushButton, QWidget, QSizePolicy
import requests

class ReleaseCard(QFrame):
    def __init__(self, release):
        super().__init__()


        self.release = release

        self.title = release.title
        self.artist = release.artist.name
        self.cover_url = release.cover_xl
        self.num_tracks = release.nb_tracks
        self.tracklist = None
        self.duration = release.duration
        self.release_date = str(getattr(release, "release_date", None) or "Unknown")

        if self.release_date != "Unknown" and self.release_date is not None:
            year, month, day = self.release_date.split("-")
            self.release_date = f"{day}/{month}/{year}"

        minutes = self.duration // 60
        seconds = self.duration % 60

        if minutes<10:
            minutes = f"0{minutes}"
        if seconds<10:
            seconds = f"0{seconds}"

        self.duration = f"{minutes}:{seconds}"


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


        self.track_list_widget.setMinimumWidth(0)
        self.track_list_widget.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Preferred,
        )


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

        if self.tracklist is None:
            self.tracklist = self.release.tracklist

        if self.track_list_layout.count() == 0:
            for i, track in enumerate(self.tracklist):
                track_layout = QHBoxLayout()

                track_layout.setContentsMargins(0, 0, 0, 0)
                track_layout.setSpacing(8)

                track_title = QLabel(track.title)
                track_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
                track_title.setWordWrap(True)
                track_title.setMinimumWidth(0)
                track_title.setSizePolicy(
                    QSizePolicy.Policy.Preferred,
                    QSizePolicy.Policy.Preferred
                )

                minutes = track.duration // 60
                seconds = track.duration % 60
                if minutes<10:
                    minutes = f"0{minutes}"
                if seconds<10:
                    seconds = f"0{seconds}"


                track_duration = QLabel(f"{minutes}:{seconds}")
                track_duration.setSizePolicy(
                    QSizePolicy.Policy.Fixed,
                    QSizePolicy.Policy.Fixed,
                )

                track_layout.addWidget(track_title, 1)
                track_layout.addWidget(track_duration)

                self.track_list_layout.addLayout(track_layout)

        self.track_list_widget.show()


    def download_release(self):
        pass




