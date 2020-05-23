import os
import random
import threading
import time

from tkinter import *
from PIL import ImageTk


img_path = os.path.join(os.getcwd(), "image")

class GameScreen :

    def __init__(self):
        self.screen = Tk()
        self.screen.title("두더지 잡기 게임")
        self.screen.geometry("504x504")
        self.screen.resizable(width=False, height = False)
        self.move = 0
        self.score = 0
        GameScreen.background = self.background()
        Title = self.contents()
        btn1 = self.Button(50,250)
        btn2 = self.Button(225, 250)
        btn3 = self.Button(400, 250)
        btn4 = self.Button(50, 325)
        btn5 = self.Button(225, 325)
        btn6 = self.Button(400, 325)
        btn7 = self.Button(50, 400)
        btn8 = self.Button(225, 400)
        btn9 = self.Button(400, 400)
        self.screen.mainloop()

    def background(self):
        final_path = os.path.join(img_path, 'Background.jpg')
        background_image = ImageTk.PhotoImage(file=final_path)
        background_image_label = Label(self.screen)
        background_image_label.configure(image =background_image)
        background_image_label.image = background_image
        background_image_label.place(x =0,y =0)


    def Button(self, x, y):
        change = []
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        def Button_clicked():
            button.configure(image = dead_image)
            if self.move in change:
                self.score += 1
            else:
                self.score -= 1
        dead_path = os.path.join(img_path, 'dead.png')
        do_path = os.path.join(img_path, 'do.jpg')
        do_image = ImageTk.PhotoImage(file=do_path)
        dead_image = ImageTk.PhotoImage(file=dead_path)
        button = Button(self.screen, command = Button_clicked)
        button.configure(image = dead_image)
        button.place(x=x, y=y)

        def buttonthread():
            while True:
                if self.move in change:
                    button.configure(image = do_image)
                else:
                    button.configure(image = dead_image)
                time.sleep(0.2)



        def percent(low,high):
            while True:
                self.move = random.randint(low,high)
                time.sleep(1)


        button_thread = threading.Thread(target=buttonthread)
        button_thread.start()
        percent_thread = threading.Thread(target=percent, args=(1, 100))
        percent_thread.start()
            

    def contents(self):
        title_label = Label(self.screen, text = '두더지 잡기 게임', background = 'blue', fg = 'green', font=("맑은 고딕", 10), height= 1)
        title_label.place(x=5,y=5)
        def scorethread():
            while True :
                score_label = Label(self.screen, text = f"점수 : {self.score} 점 입니다.", background = 'yellow', fg = 'purple', font=("맑은 고딕", 10), height= 1)
                score_label.place(x=300,y=5)
                time.sleep(0.5)

        score_thread = threading.Thread(target=scorethread)
        score_thread.start()





test = GameScreen()