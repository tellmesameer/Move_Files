import os
import shutil
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QMessageBox

import ctypes
myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class ImageMover(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Mover")
        self.setWindowIcon(QtGui.QIcon('D:/Projects/Output/logo.png'))
        self.setGeometry(150, 150, 550, 250)
       
        # Set a custom style sheet to make the GUI more visually appealing
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F5F5;
            }
            QLabel {
                font-size: 14px;
                color: #333333;
            }
            QPushButton {
                font-size: 16px;
                color: #FFFFFF;
                background-color: #0077CC;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0066B3;
            }
            QPushButton:disabled {
                background-color: #999999;
            }
        """)
        
        # Create a label to display the status
        self.status_label = QLabel(self)
        self.status_label.setGeometry(55, 180, 460, 30)
        self.status_label.setText("Click the button to move Files from the downloads folder to a New Folder.")
        
        # Create a button to select the downloads directory
        self.select_folder_button = QPushButton("Select Downloads Folder", self)
        self.select_folder_button.setGeometry(160, 20, 220, 40)
        self.select_folder_button.clicked.connect(self.select_folder)
        
        # Create a button to move the images
        self.move_images_button = QPushButton("Move Images", self)
        self.move_images_button.setGeometry(285, 135, 220, 40)
        self.move_images_button.setEnabled(False)
        self.move_images_button.clicked.connect(self.move_images)
        

        # Create a button to move the EXE
        self.move_Exe_button = QPushButton("Move Exe Files", self)
        self.move_Exe_button.setGeometry(285, 80, 220, 40)
        self.move_Exe_button.setEnabled(False)
        self.move_Exe_button.clicked.connect(self.move_Exe)
               
        # Create a button to move the PDF
        self.move_PDF_button = QPushButton("Move PDF Files", self)
        self.move_PDF_button.setGeometry(35, 80, 220, 40)
        self.move_PDF_button.setEnabled(False)
        self.move_PDF_button.clicked.connect(self.move_PDF)
        
        # Create a button to move the Excel Files
        self.move_xls_button = QPushButton("Move Excel Files", self)
        self.move_xls_button.setGeometry(35, 135, 220, 40)
        self.move_xls_button.setEnabled(False)
        self.move_xls_button.clicked.connect(self.move_xls)

        
        # Store the selected directory path
        self.directory_path = ""
        
        # Store the status message
        self.status_message = ""

    def select_folder(self):
        # Open a file dialog to select the downloads directory
        self.directory_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        
        # Enable the move images button and change the color of the select folder button if a directory was selected
        if self.directory_path:
            self.move_Exe_button.setEnabled(True)
            self.move_images_button.setEnabled(True)
            self.move_PDF_button.setEnabled(True)
            self.move_xls_button.setEnabled(True)
            self.status_label.setText(f"Selected directory: {self.directory_path}")
            self.select_folder_button.setStyleSheet("background-color: #999999")
    
    def move_images(self):
        # Show a confirmation dialog before moving the images
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to move the images?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            # Check if the Images folder already exists in the selected directory
            if not os.path.exists(os.path.join(self.directory_path, "Images")):
                # If the folder doesn't exist, create it
                os.makedirs(os.path.join(self.directory_path, "Images"))
                self.status_message = "All Images Moved to Images folder"
            else:
                self.status_message = "Images folder already exists"
            
            # Define the source and destination directories
            source_dir = self.directory_path
            destination_dir = os.path.join(self.directory_path, "Images")
            
            # Get all the image files in the source directory
            image_files = [f for f in os.listdir(source_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            
            # Loop through each image file and move it to the destination directory
            for file_name in image_files:
                source_file_path = os.path.join(source_dir, file_name)
                destination_file_path = os.path.join(destination_dir, file_name)
                shutil.move(source_file_path, destination_file_path)
        
            self.status_label.setText(self.status_message)
            
    def move_Exe(self):
        # Show a confirmation dialog before moving the Exe
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to move the Exe?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            # Check if the Images folder already exists in the selected directory
            if not os.path.exists(os.path.join(self.directory_path, "Exe")):
                # If the folder doesn't exist, create it
                os.makedirs(os.path.join(self.directory_path, "Exe"))
                self.status_message = "Files Moved to Exe Folder."
            else:
                self.status_message = "Exe folder already exists."
            
            # Define the source and destination directories
            source_dir = self.directory_path
            destination_dir = os.path.join(self.directory_path, "Exe")
            
            # Get all the Exe files in the source directory
            Exe_files = [f for f in os.listdir(source_dir) if f.endswith(('.exe', '.msi'))]
            
            # Loop through each image file and move it to the destination directory
            for file_name in Exe_files:
                source_file_path = os.path.join(source_dir, file_name)
                destination_file_path = os.path.join(destination_dir, file_name)
                shutil.move(source_file_path, destination_file_path)
        
            self.status_label.setText(self.status_message)
     
    def move_PDF(self):
        # Show a confirmation dialog before moving the Exe
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to move the PDF?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            # Check if the Images folder already exists in the selected directory
            if not os.path.exists(os.path.join(self.directory_path, "PDF")):
                # If the folder doesn't exist, create it
                os.makedirs(os.path.join(self.directory_path, "PDF"))
                self.status_message = "Files Moved to PDF Folder."
            else:
                self.status_message = "Files Moved to PDF Folder."
            
            # Define the source and destination directories
            source_dir = self.directory_path
            destination_dir = os.path.join(self.directory_path, "PDF")
            
            # Get all the Exe files in the source directory
            PDF_files = [f for f in os.listdir(source_dir) if f.endswith(('.pdf'))]
            
            # Loop through each image file and move it to the destination directory
            for file_name in PDF_files:
                source_file_path = os.path.join(source_dir, file_name)
                destination_file_path = os.path.join(destination_dir, file_name)
                shutil.move(source_file_path, destination_file_path)
        
            self.status_label.setText(self.status_message)
            
    def move_xls(self):
        # Show a confirmation dialog before moving the Exe
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to move Excel Files?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            # Check if the Images folder already exists in the selected directory
            if not os.path.exists(os.path.join(self.directory_path, "Excel Files")):
                # If the folder doesn't exist, create it
                os.makedirs(os.path.join(self.directory_path, "Excel Files"))
                self.status_message = "Files Moved to Excel Files Folder."
            else:
                self.status_message = "Files Moved to Excel Files Folder."
            
            # Define the source and destination directories
            source_dir = self.directory_path
            destination_dir = os.path.join(self.directory_path, "Excel Files")
            
            # Get all the Exe files in the source directory
            PDF_files = [f for f in os.listdir(source_dir) if f.endswith(('.xlsx','.xls','.xlsm','.xlt','.csv' ))]
            
            # Loop through each image file and move it to the destination directory
            for file_name in PDF_files:
                source_file_path = os.path.join(source_dir, file_name)
                destination_file_path = os.path.join(destination_dir, file_name)
                shutil.move(source_file_path, destination_file_path)
        
            self.status_label.setText(self.status_message)


if __name__ == '__main__':
    app = QApplication([])
    window = ImageMover()
    window.show()
    app.exec_()