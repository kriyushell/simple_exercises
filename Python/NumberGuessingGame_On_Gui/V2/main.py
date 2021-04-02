"""
Algoritma: Codemy.com'dan alıntıdır.
Kodda herhangi bir hata veya
daha iyi bir cozumu oldugunu dusunuyorsaniz
bana discord adresimden ulasabilirsiniz.
DiscordAdresim: R4mp4g3#4290
"""


from tkinter import (Tk, Button, Label, Entry)
from random import randint


class GameWindow(Tk):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.start, self.stop = 1, 10
        self.randomNumber = randint(self.start, self.stop)

        self.setupUi()

    def setupUi(self):
        ### Define game's variables ###
        # Define window's variables
        TITLE = "Number Guessing Game"
        WIDTH, HEIGHT = 530, 520
        GEOMETRY = "{}x{}+400+130".format(WIDTH, HEIGHT)
        ICON = "_icon.ico"
        # Define button's variables
        BTNS_FONT = ("Helvetica", 15, "bold")

        self.title(TITLE)
        self.geometry(GEOMETRY)
        self.minsize(WIDTH - 10, 420)
        self.iconbitmap(ICON)

        # Define a Label
        self.resultLabel = Label(
            self, text="Pick A Number\nBetween 1 and 10!", font=("Brush Script MT", 32)
        )
        self.resultLabel.pack(pady=20)

        # Define an Entry
        val = self.register(self.callback)
        self.inputNumber = Entry(
            self,
            font=("Helvetica", 100),
            width=2,
            validate="key",
            validatecommand=(val, '%P')
        )
        self.inputNumber.bind("<Return>", lambda x: self.play())
        self.inputNumber.pack(pady=30)

        # Define buttons
        self.btn_guess = Button(
            self,
            text="   Submit   ",
            font=BTNS_FONT,
            command=self.play
        )
        self.btn_guess.pack(pady=(25,20))

        self.btn_restartGame = Button(
            self,
            text="New Number",
            font=BTNS_FONT,
            command=self.restartGame
        )
        self.btn_restartGame.pack()
    """End SetupUi Method"""

    @staticmethod
    def callback(input):
        if input.isdigit(): return True
        elif input == "": return True
        else: return False
    #########################################################
    def play(self):
        if (num := self.inputNumber.get()).isdigit():
            # Reset our label
            self.resultLabel.config(text="Pick A Number\nBetween 1 and 10!")
            # Find out how far away our pick was from the actual number
            num = int(num)
            dif = abs(self.randomNumber - num)

            # Check to see if correct
            if num == self.randomNumber:
                bc = "SystemButtonFace"
                self.resultLabel.config(text="\nCorrect!!")
            elif dif == 5:
                # Set background color to white
                bc = "white"
            elif dif < 5:
                bc = f'#ff{dif}{dif}{dif}{dif}'
            else:
                bc = f'#{dif}{dif}{dif}{dif}ff'
            # Change the background of the app
            self.config(bg=bc)
            # Change bg of label
            self.resultLabel.config(bg=bc)

        else:
            # Delete entry and throw error message
            self.inputNumber.delete(0, "end")
            self.resultLabel.config(text="Hey! That's Not A Number!")



    def restartGame(self):
        self.randomNumber = randint(self.start, self.stop)
        # Clear the guess box
        self.inputNumber.delete(0, "end")
        # Change the colors back to normal
        self.resultLabel.config(bg="SystemButtonFace", text="Pick A Number\nBetween 1 and 10!")
        self.config(bg="SystemButtonFace")



if __name__ == '__main__':
    win = GameWindow()
    win.mainloop()
