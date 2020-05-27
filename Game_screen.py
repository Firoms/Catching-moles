import os
import random
import threading
import time

from tkinter import *
from PIL import ImageTk

################################
# 추가해야 할 점 (메모)
################################
# 0. 두더지 나오는 게 의도와는 다르지만 일단 ok >> 이후에 변경할지 말지 고려
# 1. 종료 버튼
# 2. 재시작 버튼
# 3. 점수 기록 (DB이용 시도)
# 4. 설명 화면을 따로 만들지 고민중
# 5. test 할 수 있는 기능 만들기...
# 6. 다양한 기능 (아이템) 추가하기
# 7. 시간 변경, 난이도 상승 등 추가하기
# 8. 망치 or +- 점수 표시와 같은 이펙트 만들기
# 9. 화면 비율 변경 가능하게 조정
################################

img_path = os.path.join(os.getcwd(), "image")

class GameScreen :

    def __init__(self):
        ###################################
        # 필요한 함수들
        self.screen = Tk()
        self.screen.title("두더지 잡기 게임")
        self.screen.geometry("504x504")
        self.screen.resizable(width=False, height = False)
        self.move = 0
        self.score = 0
        self.timer = 60
        self.start = 0
        self.button = 1
        self.judge = 0
        self.timer_start =0
        ###################################
        # 작동 화면들
        def GameStart():
            GameScreen_background = self.background('background2.jpg')
            start = self.intro()
            content = self.contents()
        #두더지들
            btn1 = self.Button(50,250)
            btn2 = self.Button(225, 250)
            btn3 = self.Button(400, 250)
            btn4 = self.Button(50, 325)
            btn5 = self.Button(225, 325)
            btn6 = self.Button(400, 325)
            btn7 = self.Button(50, 400)
            btn8 = self.Button(225, 400)
            btn9 = self.Button(400, 400)
        ###################################
        # 본격적인 시작(첫화면)
        Main_background = self.background('background1.png')
        start_button = Button(self.screen, text = "시작", command = GameStart, width = 5, height = 2)
        start_button.place(x=200, y=200)
        exit1_button = Button(self.screen, text = "종료", command = self.screen.destroy, width = 5, height = 2)
        exit1_button.place(x=260, y=200)
        
        ###################################


        ###################################
        
        ###################################
        self.screen.mainloop()

    def background(self,file):
        final_path = os.path.join(img_path, file)
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
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        change.append(random.randint(0,100))
        
        def Button_clicked():
            if self.move in change:
                self.score += 1
            else:
                if self.judge in change:
                    self.score += 1
                else:
                    self.score -= 1
            button.configure(image = dead_image)

        dead_path = os.path.join(img_path, 'dead.png')
        do_path = os.path.join(img_path, 'do.jpg')
        do_image = ImageTk.PhotoImage(file=do_path)
        dead_image = ImageTk.PhotoImage(file=dead_path)
        button = Button(self.screen, command = Button_clicked)
        button.configure(image = dead_image)
        button.place(x=x, y=y)

        def buttonthread():
            while self.start == 0:
                time.sleep(1)
            while self.timer > 0 :
                if self.move in change:
                    button.configure(image = do_image)
                else:
                    button.configure(image = dead_image)            
                time.sleep(0.1)



        def percent(low,high):
            while self.start == 0:
                time.sleep(1)
            while self.timer > 0 :
                self.move = random.randint(low,high)
                time.sleep(0.1)
                self.judge = self.move
                time.sleep(1.4)


        button_thread = threading.Thread(target=buttonthread)
        button_thread.daemon = True
        button_thread.start()
        percent_thread = threading.Thread(target=percent, args=(1, 100))
        percent_thread.daemon = True
        percent_thread.start()    

    def contents(self):
        title_label = Label(self.screen,
                            text='두더지 잡기 게임',
                            background='purple', 
                            fg='yellow',
                            font=("맑은 고딕", 10),
                            height=1)

        title_label.place(x=5, y=5)
        score_label = Label(self.screen, text = f"점수 : {self.score} 점 입니다.", background = 'yellow', fg = 'purple', font=("맑은 고딕", 10), height= 1)
        score_label.place(x=300,y=5)
        
        def scorethread():
            while self.start == 0:
                time.sleep(1)
            while self.timer > 0 :
                score_label = Label(self.screen, text = f"점수 : {self.score} 점 입니다.", background = 'yellow', fg = 'purple', font=("맑은 고딕", 10), height= 1)
                score_label.place(x=300,y=5)
                time.sleep(0.5)

        score_thread = threading.Thread(target=scorethread)
        score_thread.daemon = True
        score_thread.start()
    
    def intro(self):
        
        def timer():
            if self.timer_start == 0 :
                def timerthread():
                    while self.timer > 0 :
                        time.sleep(1)
                        self.timer -= 1
                        time_label.configure(text = self.timer)
                timer_thread = threading.Thread(target=timerthread)
                timer_thread.daemon = True
                timer_thread.start()
                self.start = 1
                self.timer_start = 1
            else:
                pass
        time_label = Label(self.screen, text = '60', background = 'green', fg = 'red', font=("맑은 고딕", 20), height= 1)
        time_label.place(x=230,y=50)
        intro_label = Label(self.screen, text = '두더지 잡기 게임 게임설명\n시작 버튼을 누르면 제한시간 60초가 주어집니다\n튀어오른 두더지를 잡으면 1점이며\n들어간 두더지를 잡을시 -1점입니다.', background = 'orange', fg = 'white', font=("맑은 고딕", 10), height= 4)
        intro_label.place(x=110,y=100)
        timer_button = Button(self.screen, text = "시작", command = timer, width = 5, height = 2)
        timer_button.place(x=200, y=200)
        exit2_button = Button(self.screen, text = "종료", command = self.screen.destroy, width = 5, height = 2)
        exit2_button.place(x=260, y=200)
        



test = GameScreen()