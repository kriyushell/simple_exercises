from tkinter import (Tk, Button)
from tkinter.font import Font
from tkinter.messagebox import askyesno

"""
Kodda herhangi bir hata veya
daha iyi bir cozumu oldugunu dusunuyorsaniz
bana discord adresimden ulasabilirsiniz.
DiscordAdresim: R4mp4g3#4290
"""

class GameWindow(Tk):
    def __init__(self):
        super(GameWindow, self).__init__()

        self.dataOfButtons = {}
        self.gameOrder = 0
        self.win_criteria = (
            ((0,0), (0,1), (0,2)),
            ((1,0), (1,1), (1,2)),
            ((2,0), (2,1), (2,2)),
            ((0,0), (1,0), (2,0)),
            ((0,1), (1,1), (2,1)),
            ((0,2), (1,2), (2,2)),
            ((0,0), (1,1), (2,2)),
            ((0,2), (1,1), (2,0)),
        )
        self.moveOfX, self.moveOfO = [], []
        


        self.customWindowProp()
        self.createButtons()
    def customWindowProp(self):
        TITLE = "Tic Tac Toe Game"
        WIDTH, HEIGHT = 500, 535
        GEOMETRY = "{}x{}+400+130".format(WIDTH, HEIGHT)
        ICON = "icon.ico"


        # change properties
        self.title(TITLE)
        self.geometry(GEOMETRY)
        self.minsize(WIDTH, HEIGHT)
        self.maxsize(WIDTH+5, HEIGHT+5)
        self.iconbitmap(ICON)


    def createButtons(self):
        WIDTH  = 3
        HEIGTH = 3
        PADX, PADY = 8, 10
        FONT = Font(family="Uni Sans", size=60)


        # Create Buttons
        ROW, COLUMN = 0, 0
        for i in range(9):
            button = Button(width=WIDTH, font=FONT)

            if i % 3 == 0:
                ROW = 0
                if i != 0: COLUMN += 1
                button.grid(row=ROW, column=COLUMN, padx=PADX, pady=PADY)
                self.dataOfButtons[(COLUMN, ROW)] = button
                ROW += 1
            else:
                button.grid(row=ROW, column=COLUMN, padx=PADX, pady=PADY)
                self.dataOfButtons[(COLUMN, ROW)] = button
                ROW += 1



        # DEFINE CLICKED EVETS FROM BUTTONS
        # bu kismi dongu ile yapmaliydim ama tkinter buna izin vermedi :/
        # siz bu kismi duzeltebilirseniz bana yazmayi unutmayin.
        self.dataOfButtons[(0, 0)].config(command=lambda: self.play((0, 0)))
        self.dataOfButtons[(1, 0)].config(command=lambda: self.play((1, 0)))
        self.dataOfButtons[(2, 0)].config(command=lambda: self.play((2, 0)))
        self.dataOfButtons[(0, 1)].config(command=lambda: self.play((0, 1)))
        self.dataOfButtons[(1, 1)].config(command=lambda: self.play((1, 1)))
        self.dataOfButtons[(2, 1)].config(command=lambda: self.play((2, 1)))
        self.dataOfButtons[(0, 2)].config(command=lambda: self.play((0, 2)))
        self.dataOfButtons[(1, 2)].config(command=lambda: self.play((1, 2)))
        self.dataOfButtons[(2, 2)].config(command=lambda: self.play((2, 2)))


    ####################################################################

    def play(self, coordinated):
        # coordinated format = (x, y)
        
        if self.gameOrder % 2 == 0:
            player = "X"
            moveOfPlayer = self.moveOfX
        else:
            player = "O"
            moveOfPlayer = self.moveOfO

        
        if not (self.dataOfButtons[coordinated]["text"]):
            self.dataOfButtons[coordinated]["text"] = player
            moveOfPlayer += [coordinated]
            self.gameOrder += 1

        # WINNING CONTROL
        for critical in self.win_criteria:
            playerMoves = tuple(i for i in moveOfPlayer if i in critical)
            if len(playerMoves) < 3: continue

            winningStatus = True
            for i in playerMoves:
                if i not in critical:
                    winningStatus = False

            if winningStatus:
                self.restratTheGame()
                questionMessage = f"Player {player} Won !!!\nQuit Game?"
                if askyesno("Devop", questionMessage): quit()

        # DRAW CONTROL
        if self.is_it_a_draw():
            self.restratTheGame()
            questionMessage = f"It was a draw.\nQuit Game?"
            if askyesno("Devop", questionMessage): quit()
                
    """END PLAY FUNC."""

    def is_it_a_draw(self):
        for button in self.dataOfButtons.values():
            if len(button["text"]) == 0:
                return False
        return True

    ####################################################################
    def restratTheGame(self):
        self.gameOrder = 0
        for button in self.dataOfButtons.values():
            button.config(text="")
        for i in self.moveOfX, self.moveOfO:
            i.clear()

"""END GameWindow CLASS"""

if __name__ == '__main__':
    win = GameWindow()
    win.mainloop()


