"""This homework was written by student Verbova Olga.
Task: 1. all files and folders are renamed using the normalize function.
2. file extensions do not change after renaming.
3. empty folders are deleted
4. the script ignores the folders archives, video, audio, documents, images;
5. unpacked archive contents are transferred to the archives folder
in a subfolder named the same as the archive, but without the extension at the end;
6. files with unknown extensions are left unchanged."""

from clean_folder.create_new_dir import make_new_dir
from clean_folder.parsing_the_folder import parsing_the_folder
from clean_folder.delete_empty_folders import delete_empty_folder
from clean_folder.rename_files_folders import rename_all_folders_files
from clean_folder.print_info import print_lists

def main():
    path_to_folder = input("Enter the folder path name: ")    
    make_new_dir(path_to_folder) # Create declared folders if they do not exist 
    parsing_the_folder(path_to_folder) # Move files by their extensions into folders
    delete_empty_folder(path_to_folder) # Delete all empty folders    
    rename_all_folders_files(path_to_folder) # Rename files and folders
    print_lists(path_to_folder) # Console output of file and race data   


if __name__ == "__main__":
    main()

