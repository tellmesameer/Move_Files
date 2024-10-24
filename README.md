# File Mover (Sort Your Folders)

File Mover is a simple GUI application built with PySide6 (Qt for Python) that allows you to organize files in a selected folder by moving them into subfolders based on their types. This application is ideal for sorting and managing downloaded files, especially from directories that tend to get cluttered.

![image](https://github.com/tellmesameer/Move_Files/assets/89124129/1a36e98b-1dad-4ac2-bc70-02dfafb08515)

## Features

- **User-Friendly Interface**: Provides an easy-to-use interface for organizing files.
- **File Selection by Type**: Move files based on categories like Images, PDFs, Executables, Text Files, Excel Files, Python Files, and more.
- **Confirmation Dialogs**: Ensures safety by asking for confirmation before moving files.
- **Progress Indicator**: Displays a progress dialog while moving files to provide feedback.
- **Dynamic UI**: Buttons are created dynamically, and their state changes based on user actions.
- **Conflict Handling**: Handles naming conflicts by automatically renaming files if a duplicate already exists in the destination folder.

## Getting Started

### Prerequisites

1. **Python 3.6+**: Make sure you have Python installed. If not, download it from [Python's official site](https://www.python.org/downloads/).

2. **Dependencies**: Install the dependencies listed below:
   - PySide6: For creating the graphical user interface.
   - Logging: Used to log application events.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/tellmesameer/Move_Files.git
   cd Move_Files
   ```

2. **Create a Virtual Environment**:

   It is highly recommended to create a virtual environment to keep project dependencies isolated and organized.

   #### On Windows:

   1. Create a virtual environment named `venv`:

      ```bash
      python -m venv venv
      ```

   2. Activate the virtual environment:

      ```bash
      venv\Scripts\activate
      ```

      After activation, you will see `(venv)` at the beginning of your command prompt, indicating that the virtual environment is active.

   #### On macOS/Linux:

   1. Create a virtual environment named `venv`:

      ```bash
      python3 -m venv venv
      ```

   2. Activate the virtual environment:

      ```bash
      source venv/bin/activate
      ```

      After activation, you will see `(venv)` at the beginning of your terminal prompt, indicating that the virtual environment is active.

3. **Install the Required Dependencies**:

   Once the virtual environment is activated, install the dependencies using `pip`:

   ```bash
   pip install PySide6
   ```

   If you have additional dependencies to install, you can also include them here.

### Running the Application

After installing the dependencies, you can run the application by executing:

```bash
python main.py
```

Make sure the virtual environment is activated before running the application to ensure all dependencies are properly used.

## Usage

- **Select Folder**: Click on the "Select Folder" button to choose the folder you want to organize.
- **Move Files by Category**: Once a folder is selected, the buttons for different file categories (e.g., Images, PDFs, Text Files) will be enabled.
  - Click on any of the category buttons (e.g., "Move Images") to move all files of that type into a corresponding subfolder within the selected directory.
- **Confirmation**: A confirmation dialog will pop up before moving files.
- **Progress Tracking**: During the move operation, a progress dialog will be displayed to track the progress of the file moving operation.

## Project Structure

```
Move_Files/
│
├── logic/
│   └── file_mover_logic.py      # The logic for file management and moving files
├── ui/
│   └── file_mover_ui.py         # The user interface setup code
├── resources/
│   └── resources_rc.py          # Compiled resources (icons, etc.)
├── main.py                      # The main entry point for the application
├── README.md                    # Project documentation
└── file_mover.log               # Log file (created during execution)
```

## Features in Detail

1. **Dynamic Button Creation**:
   - The UI generates buttons for different file types automatically, making it easy to add support for new file categories in the future.

2. **Category Management**:
   - Supported categories include:
     - Images (`.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`)
     - Executables (`.exe`, `.msi`)
     - PDFs (`.pdf`)
     - Excel Files (`.xlsx`, `.xls`, `.xlsm`, `.csv`)
     - Zip Files (`.zip`)
     - Text Files (`.txt`, `.json`)
     - Python Files (`.py`, `.ipynb`)
     - Word Documents (`.docx`)

3. **Logging**:
   - The application logs every action, including directory selection, file moves, errors, and user cancellations. Logs are saved to `file_mover.log`.

4. **Error Handling**:
   - Various exceptions such as `PermissionError`, `FileNotFoundError`, and general exceptions are handled gracefully, with user feedback and detailed logging.

## Screenshots

### Main Interface

![Main Interface](https://github.com/tellmesameer/Move_Files/assets/89124129/1a36e98b-1dad-4ac2-bc70-02dfafb08515)

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch-name`).
6. Open a pull request.

Please make sure to test your changes thoroughly.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you see fit.

## Feedback

Your feedback is valuable to us. If you encounter any issues or have suggestions for new features, please open an issue on GitHub.

## Authors

- Sameer ([https://github.com/tellmesameer](https://github.com/tellmesameer))

### Key Changes:

1. **Detailed Virtual Environment Setup**:
   - **Windows and macOS/Linux Instructions**: Added explicit steps for creating and activating a virtual environment on both Windows and macOS/Linux, with clear indications of command line prompts.
   - **Virtual Environment Activation Indication**: Mentioned that `(venv)` will appear in the prompt when the virtual environment is active, which helps users verify that they are working in the correct environment.

2. **Installation Section**:
   - Emphasized activating the virtual environment before installing dependencies, making sure that all installations happen inside the virtual environment.

This updated `README.md` should now provide a comprehensive guide for beginners and seasoned developers alike to create and work within a virtual environment, ensuring a clean and organized project setup.




## [![Repography logo](https://images.repography.com/logo.svg)](https://repography.com) / Recent activity [![Time period](https://images.repography.com/0/strawberry-graphql/strawberry/recent-activity/d751713988987e9331980363e24189ce_badge.svg)](https://repography.com)
[![Timeline graph](https://images.repography.com/0/strawberry-graphql/strawberry/recent-activity/d751713988987e9331980363e24189ce_timeline.svg)](https://github.com/strawberry-graphql/strawberry/commits)
[![Issue status graph](https://images.repography.com/0/strawberry-graphql/strawberry/recent-activity/d751713988987e9331980363e24189ce_issues.svg)](https://github.com/strawberry-graphql/strawberry/issues)
[![Pull request status graph](https://images.repography.com/0/strawberry-graphql/strawberry/recent-activity/d751713988987e9331980363e24189ce_prs.svg)](https://github.com/strawberry-graphql/strawberry/pulls)
[![Trending topics](https://images.repography.com/0/strawberry-graphql/strawberry/recent-activity/d751713988987e9331980363e24189ce_words.svg)](https://github.com/strawberry-graphql/strawberry/commits)
[![Top contributors](https://images.repography.com/0/strawberry-graphql/strawberry/recent-activity/d751713988987e9331980363e24189ce_users.svg)](https://github.com/strawberry-graphql/strawberry/graphs/contributors)
[![Activity map](https://images.repography.com/0/strawberry-graphql/strawberry/recent-activity/d751713988987e9331980363e24189ce_map.svg)](https://github.com/strawberry-graphql/strawberry/commits)


