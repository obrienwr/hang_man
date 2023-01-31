import PySimpleGUI as sg

# All the stuff inside your window.

pictures = ['./pic.png']
blanks = ""
graveyard = "sample text"


layout = [ [ [sg.Image(pictures[0])], [sg.Text(blanks)]], [sg.Text(graveyard), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

#layout2 = [[sg.Image(r'./pic.png')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[1])
    if event == 'Ok':
        graveyard += values[1]
        layout[1][1] = sg.Text(graveyard)
        window.Refresh()

window.close()
