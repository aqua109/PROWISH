import os
import shutil
from pathlib import Path
import zipfile

FILEPATH = './xapks/apps/social'
DESTINATION = './apks'

def create_sub_folder(package_name):
    try:
        os.mkdir(f'{FILEPATH}/{package_name}')
        return True
    
    except FileExistsError:
        return False
    
    except FileNotFoundError:
        return False

def delete_sub_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Directory '{folder_path}' and all its contents have been removed.")
    except FileNotFoundError:
        print(f"Error: The directory '{folder_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied. Cannot remove the directory '{folder_path}'.")
    except OSError as e:
        print(f"Error removing directory '{folder_path}': {e}")


def unpack_xapk(xapk_path, output_path):
    try:
        with zipfile.ZipFile(xapk_path, 'r') as zip:
            zip.extractall(output_path)
    except zipfile.BadZipFile:
        print(f'Failed to unzip [{xapk_path}] - BadZipFile')
        pass

def get_apk_file(file_name, output_path):
    path = Path(output_path)
    for file in path.iterdir():
        if file.is_file():
            if (file.stem == file_name):
                return file

def main():
    path = Path(FILEPATH)
    folders = []

    for file in path.iterdir():
        if file.is_file():
            if (file.suffix == '.xapk'):
                if (create_sub_folder(file.stem)):
                    output_path = f'{FILEPATH}/{file.stem}'
                    folders.append(output_path)
                    unpack_xapk(file, output_path)
                    apk_file = get_apk_file(file.stem, output_path)
                    try:
                        apk_file.rename(f'{DESTINATION}/{apk_file.name}')

                    except FileExistsError:
                        print(f'{apk_file.name} already exists. Skipping...')
                else:
                    pass
            elif (file.suffix == '.apk'):
                try:
                    file.rename(f'{DESTINATION}/{file.name}')

                except FileExistsError:
                    print(f'{apk_file.name} already exists. Skipping...')

    for folder in folders:
        print(folder)
        delete_sub_folder(folder)

if __name__ == '__main__':
    main()