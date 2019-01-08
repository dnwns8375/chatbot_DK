import tkinter as tk
from tkinter import messagebox
import random
import requests
from bs4 import BeautifulSoup
import re
import datetime
import webbrowser



#url
google = 'http://google.com'
inven =  'http://inven.com'
naver = 'http://naver.com'
dgu = 'http://www.dongguk.edu/mbs/kr/index.jsp'
bugs = 'https://music.bugs.co.kr/'

#chatbot 명령어 list형 정의
ws_g = ['구글', '구글켜','구글켜줘']
ws_n = ['네이버', '네이버켜','네이버켜줘']
ws_i = ['인벤', '인벤켜','인벤켜줘']
ws_d = ['동국대켜', '동국대홈피','동대켜','동대','동국대']
greetings1 = ['안녕','안녕!','그래 안녕!', 'ㅎㅇ', '반갑습니다', '안녕하세요', '헬로', '하이', 'gd',',그래!','안녕하세요!','hello','hi','hola','반가워','반가워!','반가워요']
greetinganswer1 = ['반갑습니다!', '안녕하세요!', '반가워요!']
greetings2 = ['그래', 'ㅇㅇ', '알았어','ㅇㅋ','dd','알았삼','야','너']
greetinganswer2 = ['날씨가 좋아요', '식사는 하셨어요?','전 당신의 비서에요']
question1 = ['밥뭐먹지', '저녁추천', '점심추천','밥추천','배달추천','뭐먹지','배고파','암헝그리','아침추천','밥줘','식사추천']
answer1 = ['오늘은 순두부를 드시는게 어때요?', '오늘은 김치찌개를 드시는게 어때요?','오늘은 라면이에요!','오늘은 내가 짜파게티 요리사!']
question2 = ['밥먹었어?', '식사했어?','밥뭇나','니밥뭇나']
answer2 = ['저는 밥을 먹지 않습니다.']
question3 = ['이름이 뭐야?', '넌 이름이뭐야?','너이름이 뭐야?','너이름이뭐야','이름이?',',이름뭐야','이름알려줘','이름','이름이뭐야','이름이뭐야?']
answer3 = ['제이름은 덕배에요.','저는 덕배라고해요']
question4 = ['뭐해?','자니?','뭐해','자니','야','무슨생각해','뭐하는중','뭐하니']
answer4 = ['당신에게 도움을 드리기 위해 기다리고있답니다.','저는 당신만을 생각해요']

searchrank = ['실검','실시간검색','순위','실검띄워']
searchmusic = ['음악순위','음악','노래','들을만한 노래','노래추천','노래순위','음악검색']
time = ['몇시야?', '지금몇시야?','왓타임이즈 나우?','몇시니?','몇시지?','몇시야','시간','현재시간']
normalspeach = ['음' ,'저기' ,'','흠','심심해','뭐할까','글쎄']
speach = ['즐거운 오후에요', '행복한 하루 보내셨나요?' ,'찾고싶은게 있으시면 말씀해주세요.']


base = tk.Tk()
input_message=tk.StringVar(base)
input_message.set("")
base.title('채팅봇')
base.geometry('500x600')


#메인프레임
frame1 = tk.Frame(height=60, width=70, bg="#A9D0F5")
frame2 = tk.Frame(height=400, width=70, bg="#A9D0F5")
frame3 = tk.Frame(height=80, width=70, bg="#A9D0F5")
frame1.pack(fill='x', side='top')
frame2.pack(fill='both', expand='YES')
frame3.pack(fill='x', side='bottom')


#봇이름 라벨
bot_name = tk.Label(frame1,text='  채 팅 봇 김 덕 배',bg='#A9D0F5', font=('tium', 12), width=15, height=2)
bot_name.pack(side='left')


#메세지 박스
message_window=tk.Text(frame2,bg='#CED8F6',yscrollcommand='YES', font = ('NanumGothic',12))
message_window.insert('end','\n덕배   :\t'+'안녕! 궁금한것이 있다면 도움말을 클릭해줘!\n')
message_window.config(state='disabled')
message_window.pack(side='top',expand='YES',fill='both')

#파싱

#네이버
html1 = requests.get(naver).text
soup1 = BeautifulSoup(html1, 'html.parser')
title_list = soup1.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
#벅스랭킹
html2 = requests.get(bugs).text
soup2 = BeautifulSoup(html2, 'html.parser')





#도움말 표시
def show_author():
    messagebox.showinfo("도움말","실시간검색\n\n실시간 인기 음악차트 \n\n대화\n\n밥 추천\n\n시간\n\n웹브라우저\n\n여러가지 기능을 사용해보세요.\n\n 더많은 도움말은 \n\n http://bitly.kr/N2hS")
    showinfo.text.tag_config("hyper", foreground="blue", underline=1)
    showinfo.tag_bind("hyper", "", lambda x: self.top_text.config(cursor="hand2"))
    showinfo.tag_bind("hyper", "", lambda x: self.top_text.config(cursor=""))
    showinfo.tag_bind("hyper", "", text_click)
#도움말 button
about_button = tk.Button(frame1,text='도움말', width=10, height=2,relief='groove', bg='#81BEF7',command=show_author)
about_button.pack(side='right')
input_entry=tk.Entry(frame3,width=10,bg='white',textvariable=input_message,font=('NanumGothic',12))
input_entry.pack(side='left',expand='YES',fill='both')


#입출력 부분
def add_text(mw,st,imsg):
#mw:message window/st:state/imsg:input message
    message_send_by_bot=''
    message_send_by_human = imsg.get()

    if message_send_by_human in greetings1:
        message_send_by_human='\n나   :\t'+imsg.get()+'\n'
        message_send_by_bot='\n덕배   :\t'+ random.choice(greetinganswer1)+'\n'
        mw.config(state='normal')               #entery 상태 기본값
        mw.insert('end',message_send_by_human)  #사용자 메세지 추가
        mw.insert('end',message_send_by_bot)    #봇 메세지 추가
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

    elif message_send_by_human in greetings2:
        message_send_by_human='\n나   :\t'+imsg.get()+'\n'
        message_send_by_bot='\n덕배   :\t'+ random.choice(greetinganswer2)+'\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

    elif message_send_by_human in question1:
            message_send_by_human='\n나   :\t'+imsg.get()+'\n'
            message_send_by_bot='\n덕배   :\t'+ random.choice(answer1)+'\n'
            mw.config(state='normal')
            mw.insert('end',message_send_by_human)
            mw.insert('end',message_send_by_bot)
            imsg.set("")
            mw.see('end')
            mw.config(state='disabled')


    elif message_send_by_human in question2:
            message_send_by_human='\n나   :\t'+imsg.get()+'\n'
            message_send_by_bot='\n덕배   :\t'+ random.choice(answer2)+'\n'
            mw.config(state='normal')
            mw.insert('end',message_send_by_human)
            mw.insert('end',message_send_by_bot)
            imsg.set("")
            mw.see('end')
            mw.config(state='disabled')

    elif message_send_by_human in question3:
            message_send_by_human='\n나   :\t'+imsg.get()+'\n'
            message_send_by_bot='\n덕배   :\t'+ random.choice(answer3)+'\n'
            mw.config(state='normal')
            mw.insert('end',message_send_by_human)
            mw.insert('end',message_send_by_bot)
            imsg.set("")
            mw.see('end')
            mw.config(state='disabled')

    elif message_send_by_human in question4:
            message_send_by_human='\n나   :\t'+imsg.get()+'\n'
            message_send_by_bot='\n덕배   :\t'+ random.choice(answer4)+'\n'
            mw.config(state='normal')
            mw.insert('end',message_send_by_human)
            mw.insert('end',message_send_by_bot)
            imsg.set("")
            mw.see('end')
            mw.config(state='disabled')


    elif message_send_by_human in normalspeach:
            message_send_by_human='\n나   :\t'+imsg.get()+'\n'
            message_send_by_bot='\n덕배   :\t'+ random.choice(speach)+'\n'
            mw.config(state='normal')
            mw.insert('end',message_send_by_human)
            mw.insert('end',message_send_by_bot)
            imsg.set("")
            mw.see('end')
            mw.config(state='disabled')


    elif message_send_by_human in time:
        message_send_by_human='\n나   :\t'+imsg.get()+'\n'
        message_send_by_bot= datetime.datetime.now()
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')


#파싱검색 명령
    elif message_send_by_human in searchrank:
        message_send_by_human='\n나   :\t'+imsg.get()+'\n\n'
        message_send_by_bot='\n덕배   :\t'+ '네이버 실시간 검색중..\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        count_searchrank=0
        for idx,title in enumerate(title_list,1):
            count_searchrank += 1
            mw.insert ('end',str(count_searchrank)+"위\t")
            mw.insert('end',title.text+'\n')
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

    elif message_send_by_human in searchmusic:
        message_send_by_human='\n나   :\t'+imsg.get()+'\n\n'
        message_send_by_bot='\n덕배   :\t'+ '차트 실시간 검색중..\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        count_musicrank=0
        for link2 in soup2.find_all(name = 'p', attrs={"class":"title"}):
            count_musicrank += 1
            mw.insert ('end',str(count_musicrank)+"위")
            mw.insert ('end', link2.text+"\n")
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

#웹브라우져 켜기
    elif message_send_by_human in ws_g:
        webbrowser.open(google)
        message_send_by_human='\n나   :\t'+imsg.get()+'\n'
        message_send_by_bot='\n덕배   :\t'+'구글을 켭니다.\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

    elif message_send_by_human in ws_n:
        webbrowser.open(naver)
        message_send_by_human='\n나   :\t'+imsg.get()+'\n'
        message_send_by_bot='\n덕배   :\t'+ '네이버를 켭니다.\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

    elif message_send_by_human in ws_i:
        webbrowser.open(inven)
        message_send_by_human='\n나   :\t'+imsg.get()+'\n'
        message_send_by_bot='\n덕배   :\t'+ '인벤을 켭니다.\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

    elif message_send_by_human in ws_d:
        webbrowser.open(dgu)
        message_send_by_human='\n나   :\t'+imsg.get()+'\n'
        message_send_by_bot='\n덕배   :\t'+ '동국대 홈페이지를 켭니다.\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')


    else :
        message_send_by_human='\n나   :\t'+imsg.get()+'\n'
        message_send_by_bot='\n덕배   :\t'+ '뭐라고 하는지 잘 모르겠어요 다시 말해주세요.' +'\n'
        mw.config(state='normal')
        mw.insert('end',message_send_by_human)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')


#입력버튼
send_button = tk.Button(frame3,text='입력',width=10,height=2,relief='groove',bg='#81BEF7',state='active',command=lambda :add_text(message_window,input_entry,input_message))
send_button.pack(side='right')
base.bind('<Return>',lambda x:add_text(message_window,input_entry,input_message))   #엔터키 사용


base.mainloop()
