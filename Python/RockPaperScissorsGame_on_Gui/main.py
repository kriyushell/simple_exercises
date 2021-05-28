from PyQt5.QtWidgets import (QMainWindow, QApplication)
from PyQt5.QtGui import (QPixmap, QTransform, QIcon)
from PyQt5.QtCore import (QSize)

from time import sleep
from random import randint
import sys

from _form import Ui_MainWindow


class MyApp(QMainWindow):
    ai_score = 0
    user_score = 0
    tie_score = 0
    round = 1

    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.setWindowIcon(QIcon(r'img\icon.png'))

        # define animation's pixmaps
        self.pixmap_user = QPixmap(r'img\animation_hand_left.png')
        self.pixmap_ai = QPixmap(r'img\animation_hand_right.png')

        self.ui.label_img_user.setPixmap(self.pixmap_user)
        self.ui.label_img_ai.setPixmap(self.pixmap_ai)

        self.customButton()

        self.ui.pushButton_rock.clicked.connect(self.rock_play)
        self.ui.pushButton_paper.clicked.connect(self.paper_play)
        self.ui.pushButton_scissors.clicked.connect(self.scissors_play)

        POSITIVE, NEGATIVE = 1, -1
        self.user_transforms = self.define_transforms(NEGATIVE)
        self.ai_transforms = self.define_transforms(POSITIVE)

    def customButton(self):
        # add style on app
        self.setStyleSheet(open("style.qss", "r").read())
        # add icon on buttons
        btns = (self.ui.pushButton_rock, self.ui.pushButton_paper, self.ui.pushButton_scissors)
        items = ("rock", "paper", "scissors")
        for btn, item in zip(btns, items):
            btn.setIcon(QIcon(rf"img\btn_{item}_icon.png"))
            btn.setIconSize(QSize(70, 70))



    ###########################################################################################################
    # Define transform objects #
    def define_transforms(self, signed):
        transform_objects = []
        for v in range(5*signed, 21*signed, 5*signed):
            t = QTransform()
            t.rotate(v)
            transform_objects.append(t)

        for v in range(15, -1, -5):
            t = QTransform()
            t.rotate(v)
            transform_objects.append(t)

        return transform_objects

    # play animation #
    def animation(self, player="user"):
        if player.lower() == "user":
            transforms = self.user_transforms
            pixmap = self.pixmap_user
            label = self.ui.label_img_user
        elif player.lower() == "ai":
            transforms = self.ai_transforms
            pixmap = self.pixmap_ai
            label = self.ui.label_img_ai
        else:
            raise Exception("Sorry, player is not defined.\nDefined players is 'user' and 'ai'")


        for t in transforms:
            rotated_pixmap = pixmap.transformed(t)
            label.setPixmap(rotated_pixmap)
            label.repaint()
            sleep(0.002)


    # Game Events #
    ###########################################################################################################
    
    # function that increases scores
    def increase_score(self, ai_is_win):
        if ai_is_win:
            self.ai_score += 1
            self.ui.label_aiWin_score.setText(str(self.ai_score))
        else:
            self.user_score += 1
            self.ui.label_userWin_score.setText(str(self.user_score))


    def play_ai(self, user_choice):
        pixmaps = (
            QPixmap(r'img\rock_right.png'),
            QPixmap(r'img\paper_right.png'),
            QPixmap(r'img\scissors_right.png')
        )

        # ROCK:0, PAPER:1, SCISSORS:2
        winning_combinations = {
            (0, 1): ("Paper beats Rock", False),   # ai is lose
            (1, 0): ("Paper beats Rock", True),    # ai is win
            (0, 2): ("Rock beats Scissors", True),
            (2, 0): ("Rock beats Scissors", False),
            (1, 2): ("Scissors beats Paper", False),
            (2, 1): ("Scissors beats Paper", True)
        }

        choice = randint(0, 2)
        self.animation("ai")

        img = pixmaps[choice]
        self.ui.label_img_ai.setPixmap(img)

        if choice != user_choice:
            text = winning_combinations[(choice, user_choice)][0]
            ai_is_win = winning_combinations[(choice, user_choice)][1]
            self.increase_score(ai_is_win)
        else:
            text = "Tie!!!"
            self.tie_score += 1
            self.ui.label_tie_score.setText(str(self.tie_score))
        self.ui.label_info.setText(text)


    def rock_play(self):
        self.animation("user")
        self.ui.label_img_user.setPixmap(QPixmap(r'img\rock_left.png'))
        self.play_ai(0)

    def paper_play(self):
        self.animation("user")
        self.ui.label_img_user.setPixmap(QPixmap(r'img\paper_left.png'))
        self.play_ai(1)

    def scissors_play(self):
        self.animation("user")
        self.ui.label_img_user.setPixmap(QPixmap(r'img\scissors_left.png'))
        self.play_ai(2)




def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()