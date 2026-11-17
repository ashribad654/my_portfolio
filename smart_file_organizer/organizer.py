import os
import shutil
from datetime import datetime
from config import FILE_CATEGORIES

LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
LOG_FILE = os.path.join(LOG_DIR, "organizer_log.txt")


def get_category(extension):
    """Return the folder category for a file extension."""
    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


def get_unique_path(destination_folder, filename):
    """Avoid overwriting an existing file by creating a unique filename."""
    name, extension = os.path.splitext(filename)
    counter = 1
    destination_path = os.path.join(destination_folder, filename)

    while os.path.exists(destination_path):
        new_name = f"{name}_{counter}{extension}"
        destination_path = os.path.join(destination_folder, new_name)
        counter += 1

    return destination_path


def write_log(message):
    """Write an operation message to the log file."""
    os.makedirs(LOG_DIR, exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")


def organize_folder(folder_path):
    """Organize files in the selected folder into category folders."""
    folder_path = os.path.abspath(folder_path)

    if not os.path.isdir(folder_path):
        print("Error: The specified folder does not exist.")
        return

    moved = 0
    skipped = 0
    errors = 0

    print("\nScanning files...\n")

    for filename in os.listdir(folder_path):
        source_path = os.path.join(folder_path, filename)

        # Ignore directories and this project's own folders.
        if not os.path.isfile(source_path):
            continue

        try:
            extension = os.path.splitext(filename)[1]
            category = get_category(extension)

            destination_folder = os.path.join(folder_path, category)
            os.makedirs(destination_folder, exist_ok=True)

            destination_path = get_unique_path(destination_folder, filename)
            shutil.move(source_path, destination_path)

            print(f"Moved: {filename} -> {category}/")
            write_log(f"Moved '{filename}' -> '{destination_path}'")
            moved += 1

        except (OSError, shutil.Error) as error:
            print(f"Could not move {filename}: {error}")
            write_log(f"ERROR moving '{filename}': {error}")
            errors += 1

    print("\n" + "=" * 50)
    print("ORGANIZATION COMPLETE")
    print("=" * 50)
    print(f"Files moved : {moved}")
    print(f"Files skipped: {skipped}")
    print(f"Errors      : {errors}")
    print(f"Log file    : {LOG_FILE}")
