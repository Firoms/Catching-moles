파이썬을 기반으로 한 두더지잡기 게임입니다.   
GUI(tkinter)를 이용하여 화면을 구성하였으며,   
Thread를 이용하여 이벤트를 처리해 주었습니다.   
tkinter 모듈을 처음으로 도전해보았기 때문에,   
코드를 예쁘게 작성하지는 못했습니다.   

   ***
__※ 주의 사항__
exe 파일 실행시 사진 및 음악파일의 경로를 알맞게 위치시켜야 파일이 실행됩니다. (파일 위치를 변경할 때 주의해주세요)
   ***

# 두더지 잡기 게임
    보통의 두더지 잡기 게임과 유사한 형태의 두더지 잡기 게임입니다.   
    개인적으로 Thread를 각각의 두더지에 적용하여 사용하려 하면서,   
    Thread 이용이 생각보다 변수가 많고 어렵다는 것을 느꼈습니다.   
    그래도 많은 오류를 해결해가는 과정이 있어 좋았고 만족하고 있습니다.   
    더 추가하고 개선하고 싶은 부분들도 있지만,   
    시도하고 도전하고 싶은 프로젝트가 많아 일단 기본적인 게임만 완성해보았습니다.   
## 룰
    9마리의 두더지로 1분간 두더지 잡기 게임을 진행하여 높은 점수를 얻는 것이 목표인 게임입니다.   
    튀어나온 두더지를 클릭하면 1점을 획득하며   
    들어가 있는 두더지를 클릭하면 1점이 차감됩니다.   
    튀어나온 두더지를 연속으로 클릭해주어도 점수가 오르기 때문에   
    두더지가 들어갈 때까지 두더지를 클릭해주는 것이 중요합니다.    
## 사용한 모듈 & 라이브러리
    1. tkinter   
    > GUI를 구성하기 위해 사용한 모듈입니다.
    2. threading
    > 여러 이벤트와 동작을 동시에 처리하기 위해 사용한 모듈입니다.
    3. random
    > 두더지가 튀어나오는 확률을 조정하기 위해 사용한 모듈입니다.
    4. sqlite3
    > 점수를 저장하기 위해 사용한 Database 모듈입니다.
    5. time
    > 현재 시각을 받아오고 측정하기 위해 사용한 모듈입니다.
    6. pillow
    > 이미지를 처리하기 위해 사용한 라이브러리 입니다.
    7. playsound
    > 배경음악을 넣어주기 위해 사용한 라이브러리입니다.
    8. sys & os
    > 사진과 음악 파일의 위치를 쉽게 지정해주기 위해 사용한 모듈입니다.
    9. pyinstaller
    > python 파일을 exe 파일로 변환하기 위해서 사용한 라이브러리입니다.

## 기능
### 두더지 게임 화면
    기본적으로, 두더지가 나오고 들어가는 이벤트는 두더지 사진을 변경해주면서 적용이 됩니다.   
    우선, 각각의 두더지마다 1~100까지의 숫자중 랜덤 14개 숫자를 리스트로 가지게 되며    
    2초마다 1~100까지의 랜덤 숫자를 뽑아 이 랜덤 숫자가 리스트안에 존재하면 튀어나오는 방식입니다.   
    따라서 두더지를 누르게되면 두더지가 들어가지만, 랜덤 숫자가 변경될 때까지는 다시 튀어나옵니다.   

### Database (sqlite3 이용)
    두더지 게임이 종료되면, 현재 날짜와 시간   
    그리고 플레이어의 닉네임과 점수를 score.db 데이터베이스에 저장을 해주게 됩니다.   

### 점수판
    score.db 데이터베이스 파일에서 플레이어들의 점수를 점수가 높은 순으로 가져오며,   
    10등까지의 내용을 GUI 화면에 띄워주게 됩니다.   
    점수판의 디자인은 당장 중요한 요소라고 생각하지 않아서 꾸미진 않았습니다.   

## 코멘트
    처음 도전하는 부분들이 많아서 조금 아쉬운 부분들도 많지만,   
    모르는 부분, 오류가 나는 부분들을 직접 찾아가면서 스스로 해결해 완성했다는 것이   
    정말 뿌듯하고 좋았던 것 같습니다.   
    두더지 잡기 게임 프로젝트는 저에게 자신감을 가져다 주었고,   
    새로운 GUI 프로젝트에 도전하는 동기부여를 가져다 준 프로젝트여서   
    고생도 하고 힘들었지만 정말 기억에 남습니다.   