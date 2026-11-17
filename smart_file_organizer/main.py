from organizer import organize_folder

def main():
    print("=" * 50)
    print("        SMART FILE ORGANIZER")
    print("=" * 50)

    folder_path = input("Enter the folder path to organize: ").strip()

    if not folder_path:
        print("No folder path provided.")
        return

    organize_folder(folder_path)


if __name__ == "__main__":
    main()
