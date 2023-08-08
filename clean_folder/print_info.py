from pathlib import Path
import clean_folder.file_processing 

list_images = []
list_video = []
list_audio = []
list_archives = []
list_documents = []
list_unknown_exeptions = []
known_exeptions = []
unknown_exeptions = []

def list_files_in_a_category(path_to_folder: str):
    path = Path(path_to_folder)    

    for item in path.glob('**/*'):
        
        item_suffix = item.suffix.split('.')
        if item.is_file() and (item_suffix[-1].upper() in clean_folder.file_processing.IMAGES):
            list_images.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        elif item.is_file() and (item_suffix[-1].upper() in clean_folder.file_processing.AUDIO):
            list_audio.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        elif item.is_file() and (item_suffix[-1].upper() in clean_folder.file_processing.VIDEO):
            list_video.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        elif item.is_file() and (item_suffix[-1].upper() in clean_folder.file_processing.DOCUMENTS):
            list_documents.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        elif item.is_file() and (item_suffix[-1].upper() in clean_folder.file_processing.ARCHIVES):
            list_archives.append(item.name)
            if item_suffix[-1].upper() not in known_exeptions:
                known_exeptions.append(item_suffix[-1].upper())
        else:
            list_unknown_exeptions.append(item.name)
            if item_suffix[-1].upper() not in unknown_exeptions and item_suffix[-1].upper() != "":
                unknown_exeptions.append(item_suffix[-1].upper())         
   
        
        

def print_lists(path_to_folder: str):
    list_files_in_a_category(path_to_folder)
    print(f"images: {list_images}")
    print(f"video: {list_video}")
    print(f"audio: {list_audio}")
    print(f"documents {list_documents}")
    print(f"archives: {list_archives}")    
    print(f"known extensions: {known_exeptions}")
    print(f"unknown extensions: {unknown_exeptions}")