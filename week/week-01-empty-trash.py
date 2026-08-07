"""
Nugget Lesson (file manipulation)
  os is more of low level
    example
      - os.getcwd()
      - os.remove()
  shutil more of high level
    example
      - shutil.copy()
      - shutil.move()
  pathlib
"""

import os
import shutil
from pathlib import Path

# so iyang dagan kay find the folder path
# loops through each files
# deletes all the files
# try and catch


def empty_trash(folder_path):

    try:
        trash = Path(folder_path).expanduser()

        if trash.exists():

            for item in trash.glob("*"):
                print(f"Deleting: {item.name}")

                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()

            print("Empty Trash")

        else:
            print("folder not found")

    except Exception as e:
        print(f"An error occured {e}")


empty_trash("~/.local/share/Trash")
