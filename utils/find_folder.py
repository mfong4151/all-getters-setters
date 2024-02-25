import os

def find_folder(target_folder, start_path='.'):
    for root, dirs, files in os.walk(start_path):
        if target_folder in dirs:
            return os.path.join(root, target_folder)
    return None

