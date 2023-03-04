import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:\\Users\kavya\\Downloads"
to_dir = "C:\\Users\\kavya\\OneDrive - Queens' School\\Documents\\Python VS\\Project\\C112 Project"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '': #''=folder
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:

        path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg gets each individual picture        
        path2 = to_dir + '/' + "Document_Files"                     # Example path2 : D:/My Files/Documents creates image file folder     
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   # Example path3 : D:/My Files/Documents/ImageName1.jpg copies from downloads to to_dir
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)