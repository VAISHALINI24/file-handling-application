import os
import sys
def create_file():
    filename = input("Enter the file name to create: ")
    with open(filename, "w") as file:
        full_path = os.path.abspath(filename)
        print(f"File '{filename}' created successfully at: {full_path}")
def insert_data():
    filename = input("Enter the file name: ")
    with open(filename, "w") as file:
        name = input("Enter name: ")
        age = input("Enter age: ")
        file.write(f"Name: {name}, Age: {age}\n")
    full_path = os.path.abspath(filename)
    print(f"Data inserted successfully in file: {full_path}")
def append_data():
    filename = input("Enter the file name: ")
    with open(filename, "a") as file:
        name = input("Enter name: ")
        age = input("Enter age: ")
        file.write(f"Name: {name}, Age: {age}\n")
    full_path = os.path.abspath(filename)
    print(f"Data appended successfully in file: {full_path}")
def read_file():
    filename = input("Enter the file name: ")
    try:
        with open(filename, "r") as file:
            print("\n--- File Content ---")
            print(file.read())
            print("------------------")
    except FileNotFoundError:
        print("File not found. Please create it first.")
def replace_data():
    filename = input("Enter the file name: ")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        print("Current Data:")
        for i, line in enumerate(lines):
            print(f"{i+1}: {line.strip()}")
        line_num = int(input("Enter line number to replace: "))
        new_data = input("Enter new data: ")
        lines[line_num-1] = new_data + "\n"
        with open(filename, "w") as file:
            file.writelines(lines)
        print("Data replaced successfully!")
    except FileNotFoundError:
        print("File not found.")
    except IndexError:
        print("Invalid line number.")
def rename_file():
    old_name = input("Enter current file name: ")
    new_name = input("Enter new file name: ")
    try:
        os.rename(old_name, new_name)
        full_path = os.path.abspath(new_name)
        print(f"File renamed successfully. New file path: {full_path}")
    except FileNotFoundError:
        print("File not found.")
def delete_file():
    filename = input("Enter the file name to delete: ")
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully!")
    except FileNotFoundError:
        print("File not found.")
def change_directory():
    path = input("Enter path to change working directory: ")
    try:
        os.chdir(path)
        print("Working directory changed successfully to:", os.getcwd())
    except FileNotFoundError:
        print("Invalid path.")
def show_directory():
    print("Current Working Directory:", os.getcwd())
def exit_program():
    print("Exiting Program...")
    sys.exit()
while True:
    print("\n===== File Management System =====")
    print("1. Create File")
    print("2. Insert Data")      
    print("3. Append Data")       
    print("4. Read File")
    print("5. Replace Data")
    print("6. Rename File")
    print("7. Delete File")
    print("8. Change Working Directory")
    print("9. Show Current Directory")
    print("10. Exit Program")
    choice = input("Enter your choice (1-10): ")
    if choice == '1':
        create_file()
    elif choice == '2':
        insert_data()
    elif choice == '3':
        append_data()
    elif choice == '4':
        read_file()
    elif choice == '5':
        replace_data()
    elif choice == '6':
        rename_file()
    elif choice == '7':
        delete_file()
    elif choice == '8':
        change_directory()
    elif choice == '9':
        show_directory()
    elif choice == '10':
        exit_program()
    else:
        print("Invalid choice! Please try again.")
