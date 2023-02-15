import PySimpleGUI as sg
from hang_man import HangMan
# All the stuff inside your window.

class gui:

    def __init__(self) -> None:
        self.pictures = ['./pic.png']
        self.man = HangMan()
        self.graveyard = self.man._graveyard
        self.layout = [ [ [sg.Image(self.pictures[0])], [sg.Text("Phrase: " + ' '.join(self.man.get_phrase()))]], [sg.Text('Your incorrect guesses are: ' + ' '.join(self.graveyard) + "\n\n"), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    def open_window(self):
        # Create the Window
        window = sg.Window('Hang Man!', self.layout)
        while not self.man.win(): #this is where the game happens
            
            print("\nYou have [WIP] chances!")
            print("Phrase: ",self.man.get_phrase())
            print('Your incorrect guesses are: ', self.graveyard)
            # Event Loop to process "events" and get the "values" of the inputs
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            self.graveyard += values[1]
            self.layout[1][0] = sg.Text('Your incorrect guesses are: ' + ' '.join(self.graveyard))
            #window['grave'].update(self.graveyard) 
            #gotta figure out a way to update the window.
        window.close()

if __name__ == "__main__":
    g = gui()
    g.open_window();
