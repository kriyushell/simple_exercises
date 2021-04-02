  
"""
Kodda herhangi bir hata veya
daha iyi bir cozumu oldugunu dusunuyorsaniz
bana discord adresimden ulasabilirsiniz.
DiscordAdresim: R4mp4g3#4290
"""

from tkinter import (Tk, Button, Label, Entry)
from random import randint


class GameWindow(Tk):
    def __init__(self, start=1, stop=100, lives=10):
        self.start, self.stop = start, stop
        super(GameWindow, self).__init__()
        self.randomNumber = randint(self.start, self.stop)
        self.isWin = False
        self.lives = self.startLives = lives
        self.setupUi()

    def setupUi(self):
        ### Define game's variables ###
        # Define window's variables
        TITLE = "Number Guessing Game"
        WIDTH, HEIGHT = 530, 520
        GEOMETRY = "{}x{}+400+130".format(WIDTH, HEIGHT)
        ICON = "_icon.ico"
        # Define label's variables
        LABEL_FONT = ("Helvetica", 25, "italic")
        self.LABEL_TEXT = text="""\
I kept a number between {start} and {stop},
guess what the number is?
You can make up to {lives} guesses.""".format(
            start=self.start, stop=self.stop, lives=self.lives
        )
        # Define button's variables
        BTNS_FONT = ("Helvetica", 15, "bold")
        self.COLOR = (
            {
                "bg": "green3",
                "fg": "white",
                "activebg": "green4",
                "activefg": "black"
            },
            {
                "bg": "red2",
                "fg": "white",
                "activebg": "red3",
                "activefg": "black"
            }
        )

        self.title(TITLE)
        self.geometry(GEOMETRY)
        self.minsize(WIDTH - 10, 420)
        self.iconbitmap(ICON)

        # Define a Label
        self.resultLabel = Label(
            self,
            text=self.LABEL_TEXT,
            font= LABEL_FONT
        )
        self.resultLabel.pack(pady=20)

        # Define an Entry
        val = self.register(self.callback)
        self.inputNumber = Entry(
            self,
            font=("Helvetica", 70),
            width=len(str(self.stop)),
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
            bg=self.COLOR[0]["bg"],
            fg=self.COLOR[0]["fg"],
            activebackground=self.COLOR[0]["activebg"],
            activeforeground=self.COLOR[0]["activefg"],
            command=self.play
        )
        self.btn_guess.pack(pady=(25,20))


        self.btn_restartGame = Button(
            self,
            text="Restart the game",
            font=BTNS_FONT,
            bg=self.COLOR[1]["bg"],
            fg=self.COLOR[1]["fg"],
            activebackground=self.COLOR[1]["activebg"],
            activeforeground=self.COLOR[1]["activefg"],
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
    def changeButtonsColor(self, isEnd):
        if isEnd:
            self.btn_guess.config(
                bg=self.COLOR[1]["bg"],
                fg=self.COLOR[1]["fg"],
                activebackground=self.COLOR[1]["activebg"],
                activeforeground=self.COLOR[1]["activefg"]
            )
            self.btn_restartGame.config(
                bg=self.COLOR[0]["bg"],
                fg=self.COLOR[0]["fg"],
                activebackground=self.COLOR[0]["activebg"],
                activeforeground=self.COLOR[0]["activefg"]
            )
        else:
            self.btn_guess.config(
                bg=self.COLOR[0]["bg"],
                fg=self.COLOR[0]["fg"],
                activebackground=self.COLOR[0]["activebg"],
                activeforeground=self.COLOR[0]["activefg"]
            )
            self.btn_restartGame.config(
                bg=self.COLOR[1]["bg"],
                fg=self.COLOR[1]["fg"],
                activebackground=self.COLOR[1]["activebg"],
                activeforeground=self.COLOR[1]["activefg"]
            )


    def play(self):
        if (num := self.inputNumber.get()).isdigit() and (not self.isWin):
            self.lives -= 1
            if (num := int(num)) == self.randomNumber:
                self.resultLabel.config(
                    text=f"Congratulations, you found the right\nanswer in {self.startLives - self.lives} attempts"
                )
                self.isWin = True
                self.changeButtonsColor(isEnd=True)

            elif (num > self.randomNumber) and (self.lives > 0):
                self.resultLabel.config(
                    text=f"you guessed wrong.\ntry a slightly smaller number\nRemaining lives: {self.lives}"
                )
            elif (num < self.randomNumber) and (self.lives > 0):
                self.resultLabel.config(
                    text=f"you guessed wrong.\ntry a slightly larger number\nRemaining lives: {self.lives}"
                )
            else:
                self.resultLabel.config(
                    text=f"I'm sorry your lives is over.\nYou have to try again."
                )
                self.changeButtonsColor(isEnd=True)


    def restartGame(self):
        self.randomNumber = randint(self.start, self.stop)
        self.resultLabel["text"] = self.LABEL_TEXT
        self.inputNumber.delete(0, "end")
        self.lives = self.startLives
        self.isWin = False
        self.changeButtonsColor(isEnd=False)



if __name__ == '__main__':
    win = GameWindow()
    win.mainloop()
