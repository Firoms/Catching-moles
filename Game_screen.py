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
        GameScreen.background = self.background()
        Title = self.contents(5,5,'두더지 잡기 게임','blue','green',10)
        btn1 = self.Button(50,50)
        self.screen.mainloop()

    def background(self):
        final_path = os.path.join(img_path, 'Background.jpg')
        background_image = ImageTk.PhotoImage(file=final_path)
        background_image_label = Label(self.screen)
        background_image_label.configure(image =background_image)
        background_image_label.image = background_image
        background_image_label.place(x =0,y =0)


    def Button(self, x, y):
        def Button_clicked():
            button.configure(image = dead_image)
        dead_path = os.path.join(img_path, 'dead.png')
        do_path = os.path.join(img_path, 'do.jpg')
        do_image = ImageTk.PhotoImage(file=do_path)
        dead_image = ImageTk.PhotoImage(file=dead_path)
        button = Button(self.screen, command = Button_clicked)
        button.configure(image = do_image)
        button.image = do_image
        button.place(x=x, y=y)

    def contents(self, x, y, text, fg, background, font):
        label = Label(self.screen, text = text, background = background, fg = fg, font=("맑은 고딕", font), height= 1)
        label.place(x=x,y=y)


def percent(low,high):
    while True:
        move = random.randint(low,high)
        print(move)
        time.sleep(1)

t = threading.Thread(target=percent, args=(1, 10))
t.start()
test = GameScreen()