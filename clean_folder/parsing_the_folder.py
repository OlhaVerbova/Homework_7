from pathlib import Path
import shutil
from clean_folder.file_processing import images_processing, documents_processing,\
audio_processing, video_processing, archives_processing

def rename_file(file_name: str, version: int)-> str: 
    name = file_name.stem
    suffix = file_name.suffix
    result_name = name + "_" + str(version) + suffix
    return result_name

def parsing_the_folder(path_to_folder: str):
    #Commit the paths to the move target folders
    path_images = Path(path_to_folder) / "images"
    path_video = Path(path_to_folder) / "video"
    path_audio = Path(path_to_folder) / "audio"
    path_documents = Path(path_to_folder) / "documents"
    path_archives = Path(path_to_folder) / "archives"
    path_previously_unpacked_archives = Path(path_archives) / "Previously unpacked archives"
    
    list_name = ["archives", "video", "audio", "documents", "images"]
    version_archives = 1
    path = Path(path_to_folder) 
    
    for item in path.glob("**/*"):
        """If the object is a file, 
        its suffix is in the Images list and 
        the file is not in the target folders where we will move the files. """
        if item.is_file() and images_processing(item.name) and ("images" not in str(item)) \
            and ("video" not in str(item))and ("audio" not in str(item)) and ("documents" not in str(item))\
                and ("archives" not in str(item)) and ("Previously unpacked archives" not in str(item)): 
            
            file_path = path_images / item.name
            version_images = 1
            if file_path.exists() == False:
                shutil.move(item, path_images)                           
            else:
                new_item_name = rename_file(item, version_images) 
                version_images += 1    
                item.rename(new_item_name)
                shutil.move(new_item_name, path_images)
        
        if item.is_file() and video_processing(item.name) and ("images" not in str(item)) \
            and ("video" not in str(item))and ("audio" not in str(item)) and ("documents" not in str(item))\
                and ("archives" not in str(item)) and ("Previously unpacked archives" not in str(item)):  #path.name not in list_name
            
            file_path = path_video / item.name
            version_video = 1
            if file_path.exists() == False:
                shutil.move(item, path_video)                           
            else:
                new_item_name = rename_file(item, version_video) 
                version_video += 1    
                item.rename(new_item_name)
                shutil.move(new_item_name, path_video)

        if item.is_file() and audio_processing(item.name) and ("images" not in str(item)) \
            and ("video" not in str(item))and ("audio" not in str(item)) and ("documents" not in str(item))\
                and ("archives" not in str(item)) and ("Previously unpacked archives" not in str(item)):  
            file_path = path_audio / item.name
            version_audio = 1
            if file_path.exists() == False:
                shutil.move(item, path_audio)                           
            else:
                new_item_name = rename_file(item, version_audio) 
                version_audio += 1    
                item.rename(new_item_name)
                shutil.move(new_item_name, path_audio)

        if item.is_file() and documents_processing(item.name) and ("images" not in str(item)) \
            and ("video" not in str(item))and ("audio" not in str(item)) and ("documents" not in str(item))\
                and ("archives" not in str(item)) and ("Previously unpacked archives" not in str(item)):  
            file_path = path_documents / item.name
            version_documents = 1
            if file_path.exists() == False:
                shutil.move(item, path_documents)                           
            else:
                new_item_name = rename_file(item, version_documents) 
                version_documents += 1    
                item.rename(new_item_name)
                shutil.move(new_item_name, path_documents)


        if item.is_file() and archives_processing(item.name) and ("images" not in str(item)) \
            and ("video" not in str(item))and ("audio" not in str(item)) and ("documents" not in str(item))\
                and ("archives" not in str(item)) and ("Previously unpacked archives" not in str(item)):  
            
            file_path = path_archives / item.name
            
            try:
                if file_path.exists() == False:                    
                    folder_for_archives = path_archives / item.stem
                    shutil.unpack_archive(item, folder_for_archives)                    
            
                else:                    
                    new_item_name = rename_file(item, version_archives)
                    version_archives += 1                                
                    item.rename(new_item_name)
                    folder_for_archives = path_archives / (item.stem + str(version_archives))
                    shutil.unpack_archive(new_item_name, folder_for_archives)  
            except FileExistsError:
                print(f"Problem with unpacking the archive")               
                        
        
        if item.is_file() and archives_processing(item.name) and ("images" not in str(item)) \
            and ("video" not in str(item))and ("audio" not in str(item)) and ("documents" not in str(item))\
                and ("archives" not in str(item)) and ("Previously unpacked archives" not in str(item)):  
            
            file_path = path_previously_unpacked_archives / item.name
            
            try:
                if file_path.exists() == False:
                    folder_for_archives = path_archives / item.stem                                      
                    shutil.move(item, path_previously_unpacked_archives)        
                else:
                    version_archives += 1
                    new_item_name = rename_file(item, version_archives)         
                    item.rename(new_item_name)
                    folder_for_archives = path_archives / (item.stem + str(version_archives))                
                    shutil.move(new_item_name, path_previously_unpacked_archives)
            except FileExistsError:
                print(f"Problem with mooving the archive")
                continue   

                

        

                
                
                    
                        

                
                
                
            



