# main.py
import sys
import os
import ctypes
import logging
from PySide6.QtWidgets import QApplication
from ui.file_mover_ui import FileMoverUI
from logic.file_mover_logic import FileMoverLogic

def main():
    # Configure logging
    logging.basicConfig(
        filename='file_mover.log',
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )

    # Create the application instance
    app = QApplication(sys.argv)

    # Set application ID for Windows (optional, works only on Windows)
    if sys.platform.startswith('win'):
        myappid = 'com.mycompany.filemoverapp'  # Arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # Initialize UI
    ui = FileMoverUI()

    # Initialize Logic
    logic = FileMoverLogic(ui)

    # Connect signals to logic
    ui.select_folder_button.clicked.connect(logic.select_folder)

    # Show the UI
    ui.show()

    # Execute the application
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
