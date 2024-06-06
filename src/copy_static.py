import os
import shutil


def recursive_copy_directory(curr_path, dest):

    items = os.listdir(curr_path)

    print(f"Searching in {curr_path}")
    for item in items:
        dir = os.path.join(curr_path, item)
        copy_dest = os.path.join(dest, item)
        if os.path.isfile(dir):
            print(f"Copying file: {item} | Directory: {os.path.abspath(dir)}")
            shutil.copy(dir, copy_dest)
            continue
        print(f"Copying directory: {item} | Directory: {os.path.abspath(dir)}")
        os.mkdir(copy_dest)
        recursive_copy_directory(
            os.path.join(curr_path, item), os.path.join(dest, item)
        )


def recursive_starter(curr_path, dest):
    if os.path.exists(dest):
        print(f"Deleting directory: {dest}")
        shutil.rmtree(dest)
    os.mkdir(dest)
    recursive_copy_directory(curr_path, dest)
