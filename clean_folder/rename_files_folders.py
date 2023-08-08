from pathlib import Path
from clean_folder.normalize import normalize

def rename_all_folders_files(path_to_folder: str):
    path = Path(path_to_folder)
    list_name = ["archives", "video", "audio", "documents", "images", "Previously unpacked archives"]
    version_folder = 1  


    for item in path.glob("**/*"):
        if item.is_file(): 
            rename = normalize(item.stem) + item.suffix
            result_name = item.with_name(rename)
            item.rename(result_name)

    for item in path.glob("**/*"):        
        if item.is_dir() and item.name not in list_name and item.exists():                      
            rename = normalize(item.name)            
            result_name = item.with_name(rename)
            item.rename(result_name) 

        if item.is_dir() and item.name not in list_name and item.exists() == False:
            while (path / item.name).exists():
                rename = normalize(item.name) + "_" + str(version_folder)
                version_folder += 1            
                result_name = item.with_name(rename)
                item.rename(result_name) 


            