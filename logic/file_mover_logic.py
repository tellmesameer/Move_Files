# logic/file_mover_logic.py
import os
import shutil
from PySide6.QtWidgets import QMessageBox, QFileDialog, QPushButton, QProgressDialog
from PySide6.QtCore import Qt
import logging

class FileMoverLogic:
    def __init__(self, ui, directory_path=""):
        self.ui = ui
        self.directory_path = directory_path
        self.buttons = {}
        self.setup_buttons()

    def setup_buttons(self):
        # Define button information with additional categories
        self.button_info = {
            "Move Images": {
                "extensions": ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
                "category": "Images"
            },
            "Move Executables": {
                "extensions": ['.exe', '.msi'],
                "category": "Executables"
            },
            "Move PDFs": {
                "extensions": ['.pdf'],
                "category": "PDFs"
            },
            "Move Excel Files": {
                "extensions": ['.xlsx', '.xls', '.xlsm', '.xlt', '.csv'],
                "category": "Excel Files"
            },
            "Move Zip Files": {
                "extensions": ['.zip'],
                "category": "Zip Files"
            },
            "Move Text Files": {
                "extensions": ['.txt', '.json'],
                "category": "Text Files"
            },
            "Move Python Files": {
                "extensions": ['.py', '.ipynb'],  # Fixed the typo here
                "category": "Python Files"
            },
            "Move Word Documents": {
                "extensions": ['.docx'],
                "category": "Word Documents"
            },
            # Add more categories here if needed
        }

        # Create buttons dynamically and add them to the grid layout
        row = 0
        col = 0
        max_columns = 3  # Adjust as needed
        for button_text, info in self.button_info.items():
            button = QPushButton(button_text)
            button.setFixedSize(220, 50)
            button.setEnabled(False)  # Initially disabled
            button.clicked.connect(
                lambda checked, b=info["category"], e=info["extensions"]: self.move_files(b, e)
            )
            self.buttons[button_text] = button
            self.ui.button_layout.addWidget(button, row, col)
            col += 1
            if col >= max_columns:
                col = 0
                row += 1

    def select_folder(self):
        # Open a file dialog to select the directory
        dialog = QFileDialog()
        self.directory_path = dialog.getExistingDirectory(self.ui, " Select Directory")

        if self.directory_path:
            # Enable all move buttons
            for button in self.buttons.values():
                button.setEnabled(True)
            self.ui.status_label.setText(f"Selected directory: {self.directory_path}")
            self.ui.status_label.setStyleSheet("font-size: 14px; color: #4CAF50;")  # Green color for success
            self.ui.status_label.show()
            self.ui.select_folder_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: #FFFFFF;
                    font-size: 16px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #43A047;
                }
            """)
            logging.info(f"Directory selected: {self.directory_path}")
        else:
            QMessageBox.warning(self.ui, "No Directory Selected", "Please select a directory to proceed.")
            logging.warning("No directory was selected.")

    def move_files(self, folder_name, extensions):
        if not self.directory_path:
            QMessageBox.warning(self.ui, "No Directory Selected", "Please select a directory first.")
            logging.warning("Attempted to move files without selecting a directory.")
            return

        # Confirmation dialog using StandardButton enumeration
        confirmation = QMessageBox.question(
            self.ui,
            "Confirmation",
            f"Are you sure you want to move the {folder_name}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No  # Set default button
        )
        if confirmation == QMessageBox.StandardButton.No:
            logging.info(f"User canceled moving {folder_name}.")
            return

        try:
            # Define the destination directory
            destination_dir = os.path.join(self.directory_path, folder_name)
            os.makedirs(destination_dir, exist_ok=True)

            # Get all the files with specified extensions in the source directory
            files = [
                f for f in os.listdir(self.directory_path)
                if os.path.isfile(os.path.join(self.directory_path, f)) and f.lower().endswith(tuple(extensions))
            ]

            if not files:
                self.ui.status_label.setText(f"No {folder_name} found to move.")
                self.ui.status_label.setStyleSheet("font-size: 14px; color: #F44336;")  # Red color for warnings
                self.ui.status_label.show()
                logging.info(f"No files found in category: {folder_name}")
                return

            # Initialize Progress Dialog
            progress_dialog = QProgressDialog(f"Moving {folder_name}...", "Cancel", 0, len(files), self.ui)
            progress_dialog.setWindowTitle("Moving Files")
            progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)  # Corrected attribute access
            progress_dialog.setMinimumDuration(0)
            progress_dialog.show()

            # Move each file to the destination directory
            moved_files_count = 0
            for i, file_name in enumerate(files, start=1):
                if progress_dialog.wasCanceled():
                    logging.info("File moving canceled by user.")
                    break

                source_file_path = os.path.join(self.directory_path, file_name)
                destination_file_path = os.path.join(destination_dir, file_name)

                # Handle potential naming conflicts
                if os.path.exists(destination_file_path):
                    base, extension = os.path.splitext(file_name)
                    counter = 1
                    new_file_name = f"{base}_{counter}{extension}"
                    destination_file_path = os.path.join(destination_dir, new_file_name)
                    while os.path.exists(destination_file_path):
                        counter += 1
                        new_file_name = f"{base}_{counter}{extension}"
                        destination_file_path = os.path.join(destination_dir, new_file_name)

                shutil.move(source_file_path, destination_file_path)
                moved_files_count += 1
                logging.info(f"Moved '{file_name}' to '{destination_dir}'")

                # Update progress
                progress_dialog.setValue(i)

            progress_dialog.close()

            # Update status label
            if moved_files_count > 0:
                self.ui.status_label.setText(f"Moved {moved_files_count} file(s) to '{folder_name}' folder.")
                self.ui.status_label.setStyleSheet("font-size: 14px; color: #4CAF50;")  # Green color for success
                self.ui.status_label.show()
                logging.info(f"Moved {moved_files_count} file(s) to '{folder_name}' folder.")
            else:
                self.ui.status_label.setText(f"No files were moved for '{folder_name}'.")
                self.ui.status_label.setStyleSheet("font-size: 14px; color: #FFA500;")  # Orange color for info
                self.ui.status_label.show()
                logging.info(f"No files were moved for category: {folder_name}")

        except PermissionError:
            QMessageBox.critical(self.ui, "Permission Denied", "You do not have the necessary permissions to move these files.")
            self.ui.status_label.setText("Permission denied during the file move operation.")
            self.ui.status_label.setStyleSheet("font-size: 14px; color: #F44336;")  # Red color for errors
            self.ui.status_label.show()
            logging.error("Permission denied during file move operation.")
        except FileNotFoundError:
            QMessageBox.critical(self.ui, "File Not Found", "One or more files were not found.")
            self.ui.status_label.setText("File not found during the move operation.")
            self.ui.status_label.setStyleSheet("font-size: 14px; color: #F44336;")  # Red color for errors
            self.ui.status_label.show()
            logging.error("File not found during move operation.")
        except Exception as e:
            QMessageBox.critical(self.ui, "Error", f"An unexpected error occurred: {str(e)}")
            self.ui.status_label.setText("An error occurred during the file move operation.")
            self.ui.status_label.setStyleSheet("font-size: 14px; color: #F44336;")  # Red color for errors
            self.ui.status_label.show()
            logging.error(f"Unexpected error during file move operation: {str(e)}")
