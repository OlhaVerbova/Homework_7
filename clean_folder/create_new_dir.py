from pathlib import Path

def make_new_dir(path_to_folder: str):
    path = Path(path_to_folder)

    for _ in path.glob("**/*"): # Going through all folders and subfolders
        if (path / "images").exists(): # Check for the imaged folder            
            break # If such a folder already exists, exit the loop
        else:
            folder_images = path.joinpath("images")
            folder_images.mkdir() # Create an images folder             
    
    for _ in path.glob("**/*"):
        if (path / "video").exists():            
            break
        else:
            folder_video = path.joinpath("video")
            folder_video.mkdir()
            

    for _ in path.glob("**/*"):
        if (path / "audio").exists():            
            break
        else:
            folder_audio = path.joinpath("audio")
            folder_audio.mkdir()            

    for _ in path.glob("**/*"):
        if (path / "documents").exists():            
            break
        else:
            folder_documents = path.joinpath("documents")
            folder_documents.mkdir()            

    for _ in path.glob("**/*"):
        if (path / "archives").exists():            
            break
        else:
            folder_archives = path.joinpath("archives")
            folder_archives.mkdir()

    for _ in path.glob("**/*"): # I added this subfolder to put already unzipped archives in it
        path_to_archive = Path(path_to_folder) / "archives"
        if (path_to_archive / "Previously unpacked archives").exists():            
            break
        else:            
            folder_previously = path_to_archive.joinpath("Previously unpacked archives")
            folder_previously.mkdir()





    


            
