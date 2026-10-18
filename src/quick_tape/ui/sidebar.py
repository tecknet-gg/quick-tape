from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.setMinimumWidth(180)

        buttons = []

        buttons.append(self.init_button(text="search"))
        buttons.append(self.init_button(text="prepare"))
        buttons.append(self.init_button(text="record"))
        buttons.append(self.init_button(text="library"))
        buttons.append(self.init_button(text="register"))
        buttons.append(self.init_button(text="jobs"))
        buttons.append(self.init_button(text="settings"))

        for button in buttons:
            self.layout.addWidget(button)

        self.layout.addStretch()

        self.setLayout(self.layout)

    def init_button(self, text:str, min_height:int=50, min_width:int=50):
        button = QPushButton(text)
        button.setMinimumHeight(min_height)
        button.setMinimumWidth(min_width)
        return button




