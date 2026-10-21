from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QLabel
from quick_tape.core.config import save_config, load_config

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.window_layout = QVBoxLayout()
        self.setLayout(self.window_layout)

        self.config = load_config()

        self.download_directory()

        self.window_layout.addStretch()

    def download_directory(self):

        download_config = self.config.get("download", {})
        download_directory = download_config.get("path", "")


        directory_label = QLabel("Download Directory:")
        directory_layout = QHBoxLayout()
        directory_input = QLineEdit()
        directory_input.setText(download_directory)
        directory_select = QPushButton("Browse")

        directory_input.textChanged.connect(lambda: save_config({"download": {"path": directory_input.text()}}))

        directory_layout.addWidget(directory_label)
        directory_layout.addWidget(directory_input)
        directory_layout.addWidget(directory_select)


        self.window_layout.addLayout(directory_layout)

