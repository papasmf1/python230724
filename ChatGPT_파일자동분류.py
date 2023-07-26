import os
import shutil

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

def move_files_by_extension(source_folder, target_folders, extensions):
    for root, _, files in os.walk(source_folder):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            for extension, target_folder in target_folders.items():
                if ext in extensions[extension]:
                    source_path = os.path.join(root, file)
                    create_folder_if_not_exists(target_folder)
                    target_path = os.path.join(target_folder, file)
                    shutil.move(source_path, target_path)
                    print(f"Moved {file} to {target_folder}")

if __name__ == "__main__":
    # Replace this with the actual download folder path if different
    downloaded_folder = r"C:\Users\student\Downloads"

    # Define the target folders for each category
    images_folder = os.path.join(downloaded_folder, "images")
    data_folder = os.path.join(downloaded_folder, "data")
    docs_folder = os.path.join(downloaded_folder, "docs")

    # Define the extensions for each category
    image_extensions = [".jpg", ".jpeg"]
    data_extensions = [".csv", ".xlsx"]
    doc_extensions = [".pdf"]

    # Map extensions to their corresponding target folders
    target_folders = {
        "image": images_folder,
        "data": data_folder,
        "doc": docs_folder
    }

    extensions = {
        "image": image_extensions,
        "data": data_extensions,
        "doc": doc_extensions
    }

    move_files_by_extension(downloaded_folder, target_folders, extensions)
