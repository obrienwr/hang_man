import PySimpleGUI as sg
from hang_man import HangMan
# All the stuff inside your window.

class gui:

    def __init__(self) -> None:
        self.pictures = ['./pic.png']
        self.man = HangMan()
        self.graveyard = self.man._graveyard
        self.blanks = self.man.get_phrase()
        self.layout = [ [ [sg.Image(self.pictures[0])], [sg.Text(self.blanks)]], [sg.Text(self.graveyard), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    def open_window(self):
        # Create the Window
        window = sg.Window('Hang Man!', self.layout)
        while True: #this is where the game happens
            # Event Loop to process "events" and get the "values" of the inputs
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            print('You entered ', values[1])
            if event == 'Ok':
                graveyard += values[1]
                self.layout[1][1] = sg.Text(graveyard)
                window.Refresh()
        window.close()

if __name__ == "__main__":
    g = gui()
    g.open_window();
