import PySimpleGUI as sg
import zip_function as zp

sg.theme('black')
lable1 = sg.Text("select archieve:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose",key="archive")

lable2 = sg.Text("select dest. dir:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",key="folder")

extract_button = sg.Button("Extract")
output_lable = sg.Text(key = "output",text_color="green")

window = sg.Window("Archive Extractor",
                   layout = [[lable1,input1,choose_button1],
                             [lable2,input2,choose_button2],
                             [extract_button,output_lable]])
while True:
    event,values = window.read()
    zp.extract_archive(values["archive"],values["folder"])
    window['output'].update(value="extraction completed ")
    if event == sg.WINDOW_CLOSED:
        break
window.close()