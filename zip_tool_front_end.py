#create a GUI that:
#select Files
#zip them 
#save them to destination folder

import PySimpleGUI as sg

#first widget to select files
label1 = sg.Text("Select files to compress")
input_box1 = sg.InputText(tooltip="Select a file")
select_files_button = sg.FileBrowse("Choose Files")


#second widget to save the zip to destination
label2 = sg.Text("Select files to compress")
input_box2 = sg.InputText(tooltip="Destination to save the zip")
select_destination_button = sg.FolderBrowse("Choose where to save")

#compress button
compress_button = sg.Button("Compress")

#create the window
window = sg.Window("File Compressor", 
                   layout=[[label1, input_box1, select_files_button], 
                            [label2, input_box2, select_destination_button],
                            [compress_button]])
window.read()
window.close()

