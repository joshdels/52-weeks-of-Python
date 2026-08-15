"""
Since my download files gets very messy so i made it cleaning using file sorter
"""

import shutil
from pathlib import Path


def sort_files_by_extension(folder_path):
    try:
        folder = Path(folder_path).expanduser()

        if folder.exists():
            print("hey found it")

            for item in folder.iterdir():

                if item.is_file():

                    extension_folder = folder / item.suffix.lstrip(".")

                    extension_folder.mkdir(
                        parents=True,
                        exist_ok=True,
                    )

                    shutil.move(item, extension_folder / item.name)

            print("done processing")

        else:
            print("folder not found")

    except Exception as e:
        print(f"An error occured {e}")


sort_files_by_extension("~/Downloads")
