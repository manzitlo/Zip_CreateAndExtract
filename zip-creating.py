import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select file to compress:       ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")  # file browser

label2 = sg.Text("Select Dest-folder Address: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")  # folder browser

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="red")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    filepath = values["files"]
    file_or_filepaths = filepath.split(";")
    folder_path = values["folder"]

    make_archive(file_or_filepaths, folder_path)
    window["output"].update(value="Successfully done!")

window.close()
