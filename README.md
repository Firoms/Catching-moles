파이썬 GUI(tkinter), Thread를 메인으로 사용하여 만든 두더지 잡기 게임입니다.

※ 주의 사항
exe 파일 실행시 사진 및 음악파일의 경로를 알맞게 위치시켜야 파일이 실행됩니다.



1. 사용 라이브러리
from PIL import ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from playsound import playsound
import sys
import os
import random
import threading
import time
import sqlite3
import tkinter.messagebox
import time

Pyinstaller - .py 를 exe 파일로 바꿀때 CMD에서 사용

- 라이브러리 중 PILLOW와 PLAYSOUND, PYINSTALLER은 CMD에서 pip install 해서 다운
- 정확히는 기억이 잘 안나는데 이외에도 install 할게 더 있을지도 모름

2. 기능
1) 두더지 잡기 게임
- 9마리의 두더지로 1분간 두더지 잡기 게임을 진행.
- 튀어나온 두더지 클릭시 1점, 들어간 두더지 클릭시 -1 점으로 점수가 주어짐.
2) 두더지 확률
3)
