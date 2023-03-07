import PySimpleGUI as sg
from hang_man import HangMan
# All the stuff inside your window.

class gui:

    def __init__(self) -> None:
        self.pictures = ['images/pic.png','images/pic1.png','images/pic2.png','images/pic3.png','images/pic4.png','images/pic5.png','images/pic6.png', 'images/gameover.png']
        self.index = 0
        self.man = HangMan()
        self.graveyard = self.man._graveyard
        self.layout = [
            [ [sg.Image(self.pictures[self.index], key = 'pics')],
                          [sg.Text("Phrase: " + ' '.join(self.get_blanks(self.man.get_phrase())), key=["-PHRASE-"])]],
            [sg.Multiline(('Your incorrect guesses are: ' + ' '.join(self.man._graveyard) + "\n\n"), key='-OUTPUT-', size = (45,5)), sg.InputText(key='-IN-')],
                [sg.Button('Ok'), sg.Button('Cancel')] 
                ]
        self.win = self.man.win()

    def open_window(self):
        # Create the Window
        window = sg.Window('Hang Man!', self.layout, return_keyboard_events = True, resizable=True)
        while not self.man.win(): #this is where the game happens
            
            print("\nYou have [WIP] chances!")
            print("Phrase: ",self.man.get_phrase())
            print('Your incorrect guesses are: ', self.graveyard)
            # Event Loop to process "events" and get the "values" of the inputs
            
            string = 'Your incorrect guesses are: \n' + ', '.join(self.graveyard)
            
            event, values = window.read()
            print(f"event type {type(event)}")
            print(f"values type {type(values)}")
            print(values)
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            
            if event == 'Ok':
                try: 
                    self.man.find_idx_of(values["-IN-"][0])
                except:
                    do = "nothing"
                string = 'Your incorrect guesses are: \n' + ', '.join(self.man._graveyard)
                window['-OUTPUT-'].update(string)
                self.index = (self.index + 1) % 8
                window['pics'].update(self.pictures[self.index])
                window['-PHRASE-'].update(self.fill_blanks(self.get_blanks(self.man.get_phrase())))

            #window['grave'].update(self.graveyard) 
        window.close()

    def get_blanks(string : str) -> str:
        ret = ""
        for i in string:
            if i == " ":
                ret += i
            else:
                ret += "_"
        return ret
    
    def fill_blanks(self,string : str) -> str:
        ret = string;
        for i in range(len(self.phrase)):
            if self.phrase[i] in self.man._found_letters:
                ret[i] = self.phrase[i]
        return ret

if __name__ == "__main__":
    g = gui()
    g.open_window();
