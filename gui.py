import PySimpleGUI as sg
from hang_man import HangMan
# All the stuff inside your window.

class gui:

    def __init__(self):
        # Need a specialized layout, graveyard, hangman, image_index, win, and phrase.
        # Need a overall hang man, attempts, hint, input box, graveyard
        self.pictures = ['images/pic.png','images/pic1.png','images/pic2.png','images/pic3.png','images/pic4.png','images/pic5.png','images/pic6.png', 'images/gameover.png']
        self.win_picture = 'images/you_win.png'
        self.font = ('Arial', 18)
        self.image_index = 0

        self.num_hang_men = 4
        self.man = HangMan()
        self.hang_men = [HangMan() for _ in range(self.num_hang_men)]
        self.layouts = [[
            [sg.Text(f"Phrase #{i + 1}: " + ' '.join(self.get_blanks(self.hang_men[i].get_phrase())),
                     key=f"-PHRASE_{i}-",
                     font=self.font)]
        ] for i in range(self.num_hang_men)]
        self.layout = [
            [[sg.Image(self.pictures[self.image_index], key='pics')],
             self.layouts,
             [sg.T(f'Guesses left: {self.man.get_remaining_attempts()}', key='-ATTEMPTS-', font=self.font),
              sg.T('', key='-HINT-')]],
            [sg.InputText(key='-IN-'),
             sg.Multiline('Your incorrect guesses are: \n\n',
                          key='-OUTPUT-', size=(45, 5), font=self.font)],
            [sg.Button('Ok', font=self.font), sg.Button('Close', font=self.font), sg.B('Give Hint', font=self.font)]
        ]

        self.image_indices = [0 for _ in range(self.num_hang_men)]

        self.phrases = [self.hang_men[i].get_phrase() for i in range(self.num_hang_men)]



        self.image_index = 0
        self.man = HangMan()
        self.phrase = self.man.get_phrase()
        self.graveyard = self.man._graveyard

        self.check_if_won()

    def check_if_won(self):
        win = True
        for man in self.hang_men:
            # check each individually,
            # they should all be true if the player has won.
            win = win and man.win()
        self.win = win


    def open_window(self):
        # Create the Window
        window = sg.Window('Hang Man!', self.layout, return_keyboard_events = True, resizable=True)
        initial_chances = self.hang_men[0].get_remaining_attempts()
        while True: #this is where the game happens
            print(f"\nYou have {self.hang_men[0].get_remaining_attempts()} chances!")
            print("Phrase: ", [man.get_phrase() for man in self.hang_men])
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
                    found = False
                    for man in self.hang_men:
                        res = man.find_idx_of(values["-IN-"])
                        if len(res) > 0:
                            found = True
                    if not found:
                        self.hang_men[0].add_to_graveyard(values['-IN-'])
                        self.hang_men[0].fail_attempt()
                        window['-ATTEMPTS-'].update(f'Guesses left: {self.hang_men[0].get_remaining_attempts()}')
                    self.image_index = initial_chances - self.hang_men[0].get_remaining_attempts()
                    window['pics'].update(self.pictures[self.image_index])
                    for i in range(self.num_hang_men):
                        window[f'-PHRASE_{i}-'].update(
                            f'Phrase #{i + 1}: '
                            f'{self.fill_blanks(self.get_blanks(self.hang_men[i].get_phrase()), self.hang_men[i])}')

                    window['-IN-'].update('')
                else:
                    correct_for_one = False
                    for i, man in enumerate(self.hang_men):
                        correct = man.guess_phrase(values['-IN-'])
                        correct_for_one = correct_for_one or correct
                        if correct:
                            window[f'-PHRASE_{i}-'].update(f'Phrase #{i+1}: {" ".join(man.get_phrase())}')
                    if not correct_for_one:
                        self.hang_men[0].add_to_graveyard(values['-IN-'])

                string = 'Your incorrect guesses are: \n' + ', '.join(self.hang_men[0]._graveyard)
                window['-OUTPUT-'].update(string)
            if event == 'Give Hint':
                window['-HINT-'].update(f'Hint: {self.man.give_hint()}, {self.man.get_hints_left()} hints left',
                                        font=self.font)
            self.check_if_won()
            if self.win:
                window['pics'].update(self.win_picture)
                # window['-PHRASE-'].update(self.man.get_phrase())

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
    
    def fill_blanks(self, string : str, man) -> str:
        return man.get_phrase_underscore()

if __name__ == "__main__":
    g = gui()
    g.open_window()
