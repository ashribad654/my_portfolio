import os


def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f'{filename} created successfully!')
    except FileExistsError:
        print('The file already exists in the device.')
    except Exception as e:
        print(f'An error occurred: {e}')


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully!")
    except FileNotFoundError:
        print('Entered file does not exist in the device.')
    except Exception as e:
        print(f"An error occurred: {e}")


def view_all_files():
    files = os.listdir('.')
    print("Files in the current directory:")
    if files:
        for file in files:
            print(file)
    else:
        print("No files found.")


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"{filename} file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def edit_file(filename):
    try:
        text = input("Enter text to append: ")
        with open(filename, 'a') as f:
            f.write(text)
        print(f"Text appended to {filename}.")
    except FileNotFoundError:
        print(f"{filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("-" * 50)
    print("             File Management App")
    print("-" * 50)

    while True:
        print("1. Create a file")
        print("2. View files")
        print("3. Read a file")
        print("4. Edit a file")
        print("5. Delete a file")
        print("6. Exit Appliation")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            case 1:
                file_name = input("Enter the file name: ")
                create_file(file_name)
            case 2:
                view_all_files()
            case 3:
                file_name = input("Enter the file name to read: ")
                read_file(file_name)
            case 4:
                file_name = input("Enter the file name to edit: ")
                edit_file(file_name)
            case 5:
                file_name = input("Enter the file name to delete: ")
                delete_file(file_name)
            case 6:
                print("Exiting file management app...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
