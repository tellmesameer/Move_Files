import os
import sys
import shutil
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QMessageBox

class ImageMover(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("File Mover")
        self.setGeometry(150, 150, 550, 400)
        self.setWindowIcon(QtGui.QIcon('D:/Projects/Output/logo.png'))
        self.setStyleSheet(self.createStyleSheet())
        self.createWidgets()

    def createStyleSheet(self):
        return """
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #36C2FF, stop:1 #007BFF);
            }
            QLabel {
                font-size: 14px;
                color: #FFFFFF;
            }
            QPushButton {
                font-size: 16px;
                color: #FFFFFF;
                background-color: #007BFF;
                border: none;
                border-radius: 4px;
                padding: 10px 16px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:disabled {
                background-color: #999999;
            }
        """

    def createWidgets(self):
        # Group related buttons together
        self.select_folder_button = self.createButton(
        "Select Downloads Folder", (160, 20), True, self.select_folder
    )
        self.select_folder_button.clicked.connect(self.select_folder)
        self.status_label = QLabel("", self)
        self.status_label.setGeometry(35, 350, 500, 30)
        self.status_label.setStyleSheet("color: #FFFFFF;")

        button_info = {
            "Move Images": {
                "position": (285, 135),
                "enabled": False,
                "callback": lambda: self.move_files("Images", ['.jpg', '.jpeg', '.png', '.gif', '.svg'])
            },
            "Move Documents": {
                "position": (35, 245),
                "enabled": False,
                "callback": lambda: self.move_files("Documents", ['.doc', '.docx', '.txt', '.dot', '.docm'])
            },
            "Move Exe Files": {
                "position": (285, 80),
                "enabled": False,
                "callback": lambda: self.move_files("Exe", ['.exe', '.msi'])
            },
            "Move PDF Files": {
                "position": (35, 80),
                "enabled": False,
                "callback": lambda: self.move_files("PDF", ['.pdf'])
            },
            "Move Excel Files": {
                "position": (35, 135),
                "enabled": False,
                "callback": lambda: self.move_files("Excel Files", ['.xlsx', '.xls', '.xlsm', '.xlt', '.csv'])
            },
            "Move Zip Files": {
                "position": (35, 190),
                "enabled": False,
                "callback": lambda: self.move_files("Zip Files", ['.zip'])
            },
            "Move PPT Files": {
                "position": (285, 190),
                "enabled": False,
                "callback": lambda: self.move_files("PPT Files", ['.ppt', '.pptx', '.pptm'])
            },
            "Move Video Files": {
                "position": (35, 300),
                "enabled": False,
                "callback": lambda: self.move_files("Video Files", ['.avi', '.flv', '.mov', '.mp4', '.mpeg', '.mpg', '.swf', '.wmv', '.vob', '.mkv'])
            },
            "Move Web Files": {
                "position": (285, 300),
                "enabled": False,
                "callback": lambda: self.move_files("Web Files", ['.aspx', '.htm', '.html', '.css', '.js'])
            },
            "Move Programming Files": {
                "position": (285, 245),
                "enabled": False,
                "callback": lambda: self.move_files("Programming Files", ['.bat', '.dll', '.jar', '.py', '.sh'])
            },
        }

        for text, info in button_info.items():
            button = self.createButton(text, info["position"], info["enabled"], info["callback"])
            self.setButtonStyle(button, text)
            button.clicked.connect(info["callback"])

        self.statusBar().showMessage("Ready")

    def createButton(self, text, position, enabled, callback):
        button = QPushButton(text, self)
        button.setGeometry(position[0], position[1], 220, 40)
        button.setEnabled(enabled)
        return button

    def setButtonStyle(self, button, text):
        if text == "Select Downloads Folder":
            button.setStyleSheet("background-color: #0077CC")
            self.select_folder_button = button
        else:
            button.setStyleSheet("background-color: #999999")
    def select_folder(self):
        # If directory_path is not already defined, initialize it to an empty string
        if not hasattr(self, 'directory_path'):
            self.directory_path = ''

        # Use the static method getExistingDirectory from QFileDialog
        directory_path = QFileDialog.getExistingDirectory(self, "Select Directory")

        # Check if a directory was selected
        if directory_path:
            # Update the instance variable with the selected directory
            self.directory_path = directory_path

            # Enable other buttons and update their styles
            for button in self.findChildren(QPushButton):
                if button is not self.select_folder_button:
                    button.setStyleSheet("background-color: #0077CC")
                    button.setEnabled(True)

            # Update the status bar with the selected directory
            self.statusBar().showMessage(f"Selected directory: {self.directory_path}")

            # Disable the select_folder_button to avoid selecting another folder
            self.select_folder_button.setStyleSheet("background-color: #999999")
            self.select_folder_button.setEnabled(False)

def move_files(self, folder_name, extensions):
    # Show a confirmation dialog before moving the files
    confirmation = QMessageBox.question(self, "Confirmation", f"Are you sure you want to move the {folder_name}?",
                                        QMessageBox.Yes | QMessageBox.No)

    if confirmation == QMessageBox.Yes:
        # Check if the folder already exists in the selected directory
        destination_dir = os.path.join(self.directory_path, folder_name)
        if not os.path.exists(destination_dir):
            # If the folder doesn't exist, create it
            os.makedirs(destination_dir)
            self.status_message = f"Files moved to {folder_name} folder."
        else:
            self.status_message = f"{folder_name} folder already exists."

        # Define the source directory
        source_dir = self.directory_path

        # Get all the files with specified extensions in the source directory
        files = [f for f in os.listdir(source_dir) if f.endswith(tuple(extensions))]

        # Loop through each file and move it to the destination directory
        for file_name in files:
            source_file_path = os.path.join(source_dir, file_name)
            destination_file_path = os.path.join(destination_dir, file_name)
            shutil.move(source_file_path, destination_file_path)

    # Update the status label only if the user clicks "Yes" and confirmation is not None
    if confirmation == QMessageBox.Yes and confirmation is not None:
        self.status_label.setText(self.status_message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageMover()
    window.show()
    sys.exit(app.exec_())
