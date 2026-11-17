# Smart File Organizer

A Python-based file organization utility that automatically categorizes and moves files into folders based on their file extensions.

## Features

- Automatically categorizes files
- Creates category folders when required
- Handles duplicate filenames without overwriting
- Uses exception handling for file-operation errors
- Maintains an operation log
- Displays a summary after organization

## Categories

- Images
- Documents
- Videos
- Audio
- Archives
- Python
- Other

## Technologies

- Python
- os
- shutil
- File Handling
- Exception Handling
- Automation

## Project Structure

```text
Smart-File-Organizer/
│
├── main.py
├── organizer.py
├── config.py
├── README.md
│
├── logs/
│   └── organizer_log.txt
│
└── test_folder/
```

## How to Run

1. Open the project in VS Code.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

4. Enter the path of the folder you want to organize.

For testing, you can place sample files inside `test_folder` and provide its path.

## Example

Before:

```text
test_folder/
├── photo.jpg
├── notes.pdf
├── music.mp3
├── video.mp4
└── program.py
```

After:

```text
test_folder/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── notes.pdf
├── Audio/
│   └── music.mp3
├── Videos/
│   └── video.mp4
└── Python/
    └── program.py
```
