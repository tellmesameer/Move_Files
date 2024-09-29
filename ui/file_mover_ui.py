from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout, QScrollArea
)
import resources.resources_rc  # Import the compiled resources

class FileMoverUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Set the window icon using the resource path
        self.setWindowIcon(QIcon(':/icons/logo.png'))

        # Set window title and size
        self.setWindowTitle("File Mover (Sort Your Folders)")
        self.resize(800, 600)

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)  # No spacing between main layout widgets
        self.main_layout.setContentsMargins(5, 5, 5, 5)  # No margins around main layout
        self.setLayout(self.main_layout)

        # Instruction label with improved wording
        self.instruction_label = QLabel("Select a folder and choose the types of files to organize:")
        self.instruction_label.setStyleSheet("font-size: 16px;")
        self.main_layout.addWidget(self.instruction_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Scrollable area for buttons
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_area)

        # Container widget for buttons
        self.button_container = QWidget()
        self.scroll_area.setWidget(self.button_container)
        self.button_layout = QGridLayout()

        # Ensure the layout has no spacing or margins
        self.button_layout.setSpacing(0)  # No spacing between buttons
        self.button_layout.setContentsMargins(5, 5, 5, 5)  # Set margins to zero

        self.button_container.setLayout(self.button_layout)

        # Create and add buttons dynamically
        button_texts = [
            "Move Images", "Move Executables", "Move PDFs", "Move Excel Files",
            "Move Zip Files", "Move Text Files", "Move Python Files", "Move Word Documents"
        ]

        row = 0
        col = 0
        max_columns = 3  # Adjust this number based on your layout needs

        for text in button_texts:
            button = QPushButton(text)
            button.setFixedSize(220, 50)  # Set button size
            self.button_layout.addWidget(button, row, col)
            col += 1
            if col >= max_columns:
                col = 0
                row += 1

        # Optionally: Set row and column stretch to zero to prevent extra spacing
        for i in range(self.button_layout.rowCount()):
            self.button_layout.setRowStretch(i, 0)

        for j in range(self.button_layout.columnCount()):
            self.button_layout.setColumnStretch(j, 0)

        # Select folder button
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.setFixedSize(220, 50)
        self.select_folder_button.setIcon(QIcon(':/icons/folder_icon.png'))  # Resource path
        self.select_folder_button.setIconSize(QSize(24, 24))
        self.main_layout.addWidget(self.select_folder_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Status label
        self.status_label = QLabel()
        self.status_label.setObjectName("status_label")
        self.status_label.hide()
        self.main_layout.addWidget(self.status_label, alignment=Qt.AlignmentFlag.AlignCenter)
