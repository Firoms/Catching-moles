import os
import random

from tkinter import *
from PIL import ImageTk


img_path = os.path.join(os.getcwd(), "image")
class GameScreen :

    def __init__(self):
        print (os.path.dirname(os.path.realpath(__file__)))
        self.screen = Tk()
        self.screen.title("두더지 잡기 게임")
        self.screen.geometry("504x504")
        self.screen.resizable(width=False, height = False)
        GameScreen.background = self.background()
        GameScreen.contents = self.contents()

    def background(self):
        final_path = os.path.join(img_path, 'Background.jpg')
        print(final_path)
        background_image = ImageTk.PhotoImage(file=final_path)
        background_image_label = Label(self.screen)
        background_image_label.configure(image =background_image)
        background_image_label.image = background_image
        background_image_label.place(x =0,y =0)
        
            
    def contents(self):
        title = Label(self.screen, text = "두더지 잡기 게임", background = "pink", fg = "blue", font=("맑은 고딕", 10), height= 1)
        title.place(x=5,y=5)
        print("contents까지는 갔음")


test = GameScreen()
