from PIL import ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import os
import random
import threading
import time
import sqlite3
import tkinter.messagebox
import time

################################
# 추가해야 할 점 (메모)
################################
# 0. 두더지 나오는 게 의도와는 다르지만 일단 ok >> 이후에 변경할지 말지 고려
# 1. 종료 버튼 O
# 2. 재시작 버튼 O
# 3. 점수 기록 (DB이용 시도)
# 4. 설명 화면을 따로 만들지 고민중
# 5. test 할 수 있는 기능 만들기...
# 6. 다양한 기능 (아이템) 추가하기
# 7. 시간 변경, 난이도 상승 등 추가하기
# 8. 망치 or +- 점수 표시와 같은 이펙트 만들기
# 9. 화면 비율 변경 가능하게 조정
################################

img_path = os.path.join(os.getcwd(), "image")


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


class GameScreen:
    def __init__(self):
        ###################################
        # 필요한 함수들
        self.screen = Tk()
        self.screen.title("두더지 잡기 게임")
        self.screen.geometry("504x504")
        self.screen.resizable(width=False, height=False)
        self.move = 0
        self.score = 0
        self.timer = 60
        self.start = 0
        self.button = 1
        self.judge = 0
        self.timer_start = 0
        self.date = time.strftime('%Y/%m/%d')
        self.time = time.strftime('%H.%M.%S')
        self.name = 'test'
        self.db = sqlite3.connect("score.db", check_same_thread=False)
        self.cursor = self.db.cursor()
        ###################################
        # 작동 화면들

        def GameStart():
            GameScreen_background = self.background("background2.jpg")
            start = self.intro()
            content = self.contents()
            # 두더지들
            btn1 = self.Button(50, 250)
            btn2 = self.Button(225, 250)
            btn3 = self.Button(400, 250)
            btn4 = self.Button(50, 325)
            btn5 = self.Button(225, 325)
            btn6 = self.Button(400, 325)
            btn7 = self.Button(50, 400)
            btn8 = self.Button(225, 400)
            btn9 = self.Button(400, 400)

        def jump():
            score = self.Scoreboard()

        def Main():
            Where = self.center_window(504, 504)
            Make_menu = self.Game_menu()
            self.screen.iconbitmap('do_icon.ico')
            Main_background = self.background("background1.png")
            self.start_img_path = os.path.join(img_path, "start.png")
            self.exit_img_path = os.path.join(img_path, "exit.png")
            self.score_img_path = os.path.join(img_path, "score_btn.png")
            self.start_image = ImageTk.PhotoImage(file=self.start_img_path)
            self.exit_image = ImageTk.PhotoImage(file=self.exit_img_path)
            self.score_image = ImageTk.PhotoImage(file=self.score_img_path)
            start_button = Button(self.screen, command=GameStart)
            start_button.configure(image=self.start_image)
            start_button.place(x=150, y=200)
            score_button = Button(self.screen, command=jump)
            score_button.configure(image=self.score_image)
            score_button.place(x=225, y=200)
            exit_button = Button(self.screen, command=self.screen.destroy)
            exit_button.configure(image=self.exit_image)
            exit_button.place(x=300, y=200)

        ###################################

        ###################################

        ###################################
        Main()
        self.screen.mainloop()

    def DB(self):
        insert_query = \
            f"INSERT INTO Score_table VALUES('{self.date}', '{self.time}', '{self.name}', '{self.score}')"
        self.cursor.execute(insert_query)
        self.db.commit()

    def Scoreboard(self):
        Score_background = self.background("background3.png")
        if self.timer == 0:
            Save = self.DB()
        self.cursor.execute(
            "SELECT * FROM Score_table ORDER BY Score DESC")
        score_title_label = Label(
            self.screen, text="점수판", background="green", fg="red", font=("맑은 고딕", 20), height=1)
        score_title_label.place(x=10, y=10)
        for i in range(1, 11):
            rank_label = Label(
                self.screen, text=f"{i}등 : {self.cursor.fetchone()}점", background="green", fg="red", font=("맑은 고딕", 12), height=1)
            rank_label.place(x=10, y=(i*40)+40)
        # db.close()

    def center_window(self, width, height):
        screen_width = self.screen.winfo_screenwidth()
        screen_height = self.screen.winfo_screenheight()

        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)

        self.screen.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def Game_menu(self):
        def _quit():
            self.screen.quit()
            self.screen.destroy()
            exit()

        def _msgBox():
            tkinter.messagebox.showinfo(
                'About', 'Firoms가 처음 만드는 Gui 게임\n두더지잡기 게임인데 아직 조금 미숙함\n재밌게 플레이 하세요')

        menu_bar = Menu(self.screen)
        self.screen.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New Game", command=restart_program)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=_quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=_msgBox)

    def background(self, file):
        final_path = os.path.join(img_path, file)
        background_image = ImageTk.PhotoImage(file=final_path)
        background_image_label = Label(self.screen)
        background_image_label.configure(image=background_image)
        background_image_label.image = background_image
        background_image_label.place(x=0, y=0)

    def Button(self, x, y):
        change = []
        for i in range(14):
            change.append(random.randint(0, 100))

        def Button_clicked():
            if self.move in change:
                self.score += 1
            else:
                if self.judge in change:
                    self.score += 1
                else:
                    self.score -= 1
            button.configure(image=dead_image)

        dead_path = os.path.join(img_path, "dead.png")
        do_path = os.path.join(img_path, "do.jpg")
        do_image = ImageTk.PhotoImage(file=do_path)
        dead_image = ImageTk.PhotoImage(file=dead_path)
        button = Button(self.screen, command=Button_clicked)
        button.configure(image=dead_image)
        button.place(x=x, y=y)

        def buttonthread():
            while self.start == 0:
                time.sleep(1)
            while self.timer > 0:
                if self.move in change:
                    button.configure(image=do_image)
                else:
                    button.configure(image=dead_image)
                time.sleep(0.1)

        def percent(low, high):
            while self.start == 0:
                time.sleep(1)
            while self.timer > 0:
                self.move = random.randint(low, high)
                time.sleep(0.1)
                self.judge = self.move
                time.sleep(2)

        button_thread = threading.Thread(target=buttonthread)
        button_thread.daemon = True
        button_thread.start()
        percent_thread = threading.Thread(target=percent, args=(1, 100))
        percent_thread.daemon = True
        percent_thread.start()

    def contents(self):
        title_label = Label(
            self.screen,
            text="두더지 잡기 게임",
            background="purple",
            fg="yellow",
            font=("맑은 고딕", 10),
            height=1,
        )

        title_label.place(x=5, y=5)
        score_label = Label(
            self.screen,
            text=f"점수 : {self.score} 점 입니다.",
            background="yellow",
            fg="purple",
            font=("맑은 고딕", 10),
            height=1,
        )
        score_label.place(x=300, y=5)

        def scorethread():
            while self.start == 0:
                time.sleep(1)
            while self.timer > 0:
                score_label = Label(
                    self.screen,
                    text=f"점수 : {self.score} 점 입니다.",
                    background="yellow",
                    fg="purple",
                    font=("맑은 고딕", 10),
                    height=1,
                )
                score_label.place(x=300, y=5)
                time.sleep(0.5)
            Score_board = self.Scoreboard()

        score_thread = threading.Thread(target=scorethread)
        score_thread.daemon = True
        score_thread.start()

    def intro(self):
        def timer():
            self.name = name.get()
            name_entered.configure(state='disabled')
            if self.timer_start == 0:

                def timerthread():
                    while self.timer > 0:
                        time.sleep(1)
                        self.timer -= 1
                        time_label.configure(text=self.timer)

                timer_thread = threading.Thread(target=timerthread)
                timer_thread.daemon = True
                timer_thread.start()
                self.start = 1
                self.timer_start = 1
            else:
                pass

        time_label = Label(
            self.screen, text="60", background="green", fg="red", font=("맑은 고딕", 20), height=1
        )
        time_label.place(x=230, y=50)
        intro_label = Label(
            self.screen,
            text="두더지 잡기 게임 게임설명\n시작 버튼을 누르면 제한시간 60초가 주어집니다\n튀어오른 두더지를 잡으면 1점이며\n들어간 두더지를 잡을시 -1점입니다.",
            background="orange",
            fg="white",
            font=("맑은 고딕", 10),
            height=4,
        )
        intro_label.place(x=110, y=100)
        ttk.Label(self.screen, text="닉네임 입력 : ").place(x=110, y=200)
        name = tkinter.StringVar()
        name_entered = ttk.Entry(
            self.screen, textvariable=name)
        name_entered.place(x=110, y=220, height=20, width=80)
        timer_button = Button(self.screen,
                              command=timer)
        timer_button.configure(image=self.start_image)
        timer_button.place(x=220, y=200)
        exit2_button = Button(
            self.screen, command=self.screen.destroy
        )
        exit2_button.configure(image=self.exit_image)
        exit2_button.place(x=330, y=200)


test = GameScreen()
