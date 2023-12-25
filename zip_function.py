import zipfile

def extract_archive(archievePath,dict_dir):
    with zipfile.ZipFile(archievePath,"r") as archive:
        archive.extractall(dict_dir)

if __name__  == "__main__":
    extract_archive("compressed.zip","E:\Himyansu\python\zip_extract")        
 