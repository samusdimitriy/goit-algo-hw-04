import os
import shutil
import argparse
from pathlib import Path

def copy_files_by_extension(source_dir, dest_dir):
    Path(dest_dir).mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            file_extension = Path(file).suffix.lower()

            if not file_extension:
                extension_folder = 'no_extension'
            else:
                extension_folder = file_extension[1:]

            extension_dir = os.path.join(dest_dir, extension_folder)
            Path(extension_dir).mkdir(parents=True, exist_ok=True)

            dest_file_path = os.path.join(extension_dir, file)
            shutil.copy2(source_file_path, dest_file_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir")
    parser.add_argument("dest_dir", nargs='?', default="dist")
    args = parser.parse_args()

    if not os.path.exists(args.source_dir) or not os.path.isdir(args.source_dir):
        print("Ошибка: директория не найдена")
        return

    copy_files_by_extension(args.source_dir, args.dest_dir)

if __name__ == "__main__":
    main()
