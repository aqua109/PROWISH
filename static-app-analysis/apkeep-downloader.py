import subprocess
import csv

PATH = './apps-to-download.csv'
OUTPUT = './apks'

def get_package_list(csv_path):
    packages = []
    with open(csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            packages.append(row[0].strip())
            print(row[0])
    
    return packages

def download_package(package_name):
    try:
        subprocess.run(['apkeep', '-a', package_name, OUTPUT])

    except subprocess.CalledProcessError as e:
        print(f'Screenshot function failed with exit code: {e.returncode}')
        pass

def main():
    packages = get_package_list(PATH)
    
    for package in packages:
        download_package(package)

if __name__ == '__main__':
    main()