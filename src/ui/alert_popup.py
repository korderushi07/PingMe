from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QApplication,
    QFrame,
)
from PySide6.QtCore import Qt, QTimer


class AlertPopup(QWidget):

    def __init__(self, alert_type, transcript):
        super().__init__()

        self.is_pinned = False

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.setFixedWidth(360)

        self.is_name_alert = alert_type == "Name Mentioned"

        self.setup_ui(alert_type, transcript)

        # Automatically close after 5 seconds
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.close)
        self.timer.start(5000)

    def setup_ui(self, alert_type, transcript):

        container = QFrame(self)
        container.setObjectName("container")

        container.setStyleSheet("""
            QFrame#container {
                background-color: #20232B;
                border: 1px solid #414653;
                border-radius: 14px;
            }

            QLabel {
                color: #FFFFFF;
                border: none;
            }

            QPushButton {
                background-color: #343945;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 6px 10px;
            }

            QPushButton:hover {
                background-color: #4A5060;
            }
        """)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(18, 16, 18, 16)
        layout.setSpacing(12)

        # Header
        header = QHBoxLayout()

        accent = "#4ADE80" if self.is_name_alert else "#60A5FA"

        title = QLabel(
            "YOU WERE MENTIONED!"
            if self.is_name_alert
            else "KEYWORD DETECTED"
        )

        title.setStyleSheet(
            f"font-size: 15px; font-weight: bold; color: {accent};"
        )

        header.addWidget(title)
        header.addStretch()

        self.pin_button = QPushButton("Pin")
        self.pin_button.clicked.connect(self.toggle_pin)

        close_button = QPushButton("✕")
        close_button.clicked.connect(self.close)

        header.addWidget(self.pin_button)
        header.addWidget(close_button)

        layout.addLayout(header)

        # Alert type
        type_label = QLabel(alert_type)
        type_label.setStyleSheet(
            "font-size: 12px; color: #AAB2C0;"
        )

        layout.addWidget(type_label)

        # Transcript
        transcript_label = QLabel(transcript)
        transcript_label.setWordWrap(True)
        transcript_label.setStyleSheet(
            "font-size: 14px; color: white;"
        )

        layout.addWidget(transcript_label)

        # Footer
        self.footer = QLabel("Auto-dismisses in 5 seconds")
        self.footer.setStyleSheet(
            "font-size: 11px; color: #929AAA;"
        )

        layout.addWidget(self.footer)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(container)

    def toggle_pin(self):

        self.is_pinned = not self.is_pinned

        if self.is_pinned:
            self.timer.stop()
            self.pin_button.setText("Unpin")
            self.footer.setText("Pinned · Waiting for dismissal")
        else:
            self.pin_button.setText("Pin")
            self.footer.setText("Auto-dismisses in 5 seconds")
            self.timer.start(5000)

    def show_popup(self):

        screen = QApplication.primaryScreen()

        if screen:
            available = screen.availableGeometry()

            x = available.right() - self.width() - 20
            y = available.top() + 20

            self.move(x, y)

        self.show()
        self.raise_()
