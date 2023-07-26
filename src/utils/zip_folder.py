import os
import zipfile

def zip_folder(folder_path:str, output_path:str):
    """zip files from folder to destination

    Args:
        folder_path (str): folder path
        output_path (str): destination path including file name
    """    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)