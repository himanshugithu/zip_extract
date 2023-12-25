import PySimpleGUI as sg

sg.theme('SystemDefault')  # Set the theme

layout = [
    [sg.Text("Choose a folder:")],
    [sg.InputText(key="folder_path"), sg.FolderBrowse()],
    [sg.Button("OK"), sg.Button("Cancel")]
]

window = sg.Window("Folder Chooser", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break
    elif event == "OK":
        chosen_folder = sg.PopupGetFolder("Select a folder")
        window["folder_path"].update(chosen_folder)  # Update the input field with the chosen folder
        sg.popup(f"Chosen folder: {chosen_folder}")
        break

window.close()
