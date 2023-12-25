import zipfile
import PySimpleGUI as sg
def extract_archive(archievePath="",dict_dir=""):
    try:
        with zipfile.ZipFile(archievePath,"r") as archive:
            archive.extractall(dict_dir)
    except Exception as e:
        pass

if __name__  == "__main__":
    extract_archive("compressed.zip","E:\Himyansu\python\zip_extract")        
 