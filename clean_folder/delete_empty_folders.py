from pathlib import Path

def delete_empty_folder(path_to_folder: str):
    path = Path(path_to_folder)
    list_name = ["archives", "video", "audio", "documents", "images", "Previously unpacked archives"]

    for item in path.iterdir():
        if item.is_dir():
            delete_empty_folder(item)

    if not any(path.iterdir()) and path.name not in list_name:        
        path.rmdir()
        