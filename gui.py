import PySimpleGUI as sg
from hang_man import HangMan
# All the stuff inside your window.

class gui:

    def __init__(self):
        self.pictures = ['images/pic.png','images/pic1.png','images/pic2.png','images/pic3.png','images/pic4.png','images/pic5.png','images/pic6.png', 'images/gameover.png']
        self.win_picture = 'images/you_win.png'
        self.index = 0
        self.man = HangMan()
        self.phrase = self.man.get_phrase()
        self.graveyard = self.man._graveyard
        self.font = ('Arial', 18)
        self.layout = [
            [ [sg.Image(self.pictures[self.index], key = 'pics')],
              [sg.Text("Phrase: " + ' '.join(self.get_blanks(self.man.get_phrase())), key="-PHRASE-", font=self.font)],
              [sg.T(f'Guesses left: {self.man.get_remaining_attempts()}', key='-ATTEMPTS-', font=self.font),
               sg.T('', key='-HINT-')]],
            [sg.InputText(key='-IN-'),
             sg.Multiline(('Your incorrect guesses are: ' + ' '.join(self.man._graveyard) + "\n\n"),
                          key='-OUTPUT-', size = (45,5), font=self.font)],
            [sg.Button('Ok', font=self.font), sg.Button('Close', font=self.font), sg.B('Give Hint', font=self.font)]
        ]
        self.win = self.man.win()

    def open_window(self):
        # Create the Window
        window = sg.Window('Hang Man!', self.layout, return_keyboard_events = True, resizable=True)
        initial_chances = self.man.get_remaining_attempts()
        while True: #this is where the game happens
            print(f"\nYou have {self.man.get_remaining_attempts()} chances!")
            print("Phrase: ", self.man.get_phrase())
            print('Your incorrect guesses are: ', self.graveyard)
            # Event Loop to process "events" and get the "values" of the inputs
            
            string = 'Your incorrect guesses are: \n' + ', '.join(self.graveyard)
            
            event, values = window.read()
            print(f"event type {type(event)}")
            print(f"values type {type(values)}")
            print(values)
            if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks close
                break
            
            if event == 'Ok':
                if len(values['-IN-']) == 1:
                    self.man.find_idx_of(values["-IN-"])
                    self.index = initial_chances - self.man.get_remaining_attempts()
                    window['pics'].update(self.pictures[self.index])
                    window['-PHRASE-'].update(self.fill_blanks(self.get_blanks(self.man.get_phrase())))
                    window['-IN-'].update('')
                else:
                    self.man.guess_phrase(values['-IN-'])
                string = 'Your incorrect guesses are: \n' + ', '.join(self.man._graveyard)
                window['-OUTPUT-'].update(string)
            if event == 'Give Hint':
                window['-HINT-'].update(f'Hint: {self.man.give_hint()}, {self.man.get_hints_left()} hints left',
                                        font=self.font)
            if self.man.win():
                window['pics'].update(self.win_picture)
                window['-PHRASE-'].update(self.man.get_phrase())

        window.close()

    @staticmethod
    def get_blanks(string: str) -> str:
        ret = ""
        for i in string:
            if i == " ":
                ret += i
            else:
                ret += "_"
        return ret
    
    def fill_blanks(self, string : str) -> str:
        return self.man.get_phrase_underscore()

if __name__ == "__main__":
    g = gui()
    g.open_window()
