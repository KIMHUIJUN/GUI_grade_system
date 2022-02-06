from ast import Return
from tkinter import*
from tkinter import ttk
import tkinter.ttk
import tkinter
from matplotlib.pyplot import close
import pandas as pd
import csv
import numpy as np
from tkinter.simpledialog import*
import matplotlib.pyplot as plt

df = pd.DataFrame( columns=['번호','국어','영어','수학','총점','평균','환산'])

f = open('./num.txt', 'r')
      
while True:
    line = f.readline()
    
    if not line: 
          break    
    
    df= pd.read_csv('C:\kim\\{}.csv'.format(line.rstrip("\n")),encoding= ' UTF-8')

f.close()
df.index = df['번호']  
df = df.sort_index()

#창 설정
window = Tk()
window.title('Grade')
window.geometry('800x500')

#함수 설정
#점수 설정함수


def NewWin():
    
    
    new_window = tkinter.Toplevel()
    
    def Close():
        new_window.destroy()

    while True:
        
        new_window.geometry('500x500+1000+100')
        lab2 = Label(new_window, text= '학번')
        lab2.pack()
        st_num = askinteger("학번 입력","학번을 입력하세요", minvalue=1)    
        
        if st_num is None:
            new_window.destroy()
            break

        try:

            st_num = int(st_num)       
    
        except ValueError   as e:  # 학번이 정수인지 확인 
            lab3= Label(new_window, text= '{}는 입력할 수 없습니다.'.format(st_num))
            lab3.pack()
            continue
        else:
    
            i = []
            for a in range(len(df.index)): # 학번이 중복인지 확인 
                
                p = df.index[a] 
                i.append(p)
                continue
            
            if st_num <= 0: # 학번이 양수인지 확인 
                
                lab4= Label(new_window, text= '{}는 입력할 수 없습니다.'.format(st_num))
                lab4.pack()
                continue

            
            elif st_num in i : # 중복인지 확인 
                
                lab5= Label(new_window, text= '{}는 존재하는 학번입니다.'.format(st_num))
                lab5.pack()
                continue
            
            else:
                
                lab2.configure(text="학번 : "+ str(st_num))
                break
    
    while True:
        lab8 = Label(new_window, text='{}의 국어 점수'.format(st_num))
        lab8.pack()
        try:
            
            st_num_kor = askinteger("국어 점수 입력", '국어 점수를 입력하시오',minvalue=0, maxvalue=100)
        
        except ValueError as e:
            lab9 = Label(new_window, text='정수 0~100를 입력하시오')
            lab9.pack()
        else:
            
            if st_num_kor is None:
                new_window.destroy()
                break
            
            else:

                lab8.configure(text='{}의 국어 점수 : '.format(st_num)+str(st_num_kor))
                break

    while True:
        lab10 = Label(new_window, text='{}의 영어 점수'.format(st_num))
        lab10.pack()
        try:
            
            st_num_eng = askinteger("영어 점수 입력", '영어 점수를 입력하시오',minvalue=0, maxvalue=100)
        
        except ValueError as e:
            lab9 = Label(new_window, text='정수 0~100를 입력하시오')
            lab9.pack()
        else:
            
            if st_num_eng is None:
                new_window.destroy()
                break
            
            else:

                lab10.configure(text='{}의 영어 점수 : '.format(st_num)+str(st_num_eng))
                break

    while True:
        lab11 = Label(new_window, text='{}의 수학 점수'.format(st_num))
        lab11.pack()
        try:
            
            st_num_math = askinteger("수학 점수 입력", '수학 점수를 입력하시오',minvalue=0, maxvalue=100)
        
        except ValueError as e:
            lab9 = Label(new_window, text='정수 0~100를 입력하시오')
            lab9.pack()
        else:
            
            if st_num_math is None:
                new_window.destroy()
                break
            
            else:

                lab11.configure(text='{}의 수학 점수 : '.format(st_num)+str(st_num_math))
                break
    lab12 = Label(new_window, text='{}의 점수를 저장하시겠습니까(y/n)?'.format(st_num))
    lab12.pack()
    y_or_n = askstring("성적 저장여부", "저장시 y , 저장하지 않을시 n 을 입력해주세요")
    if y_or_n == 'n':
        lab12.configure(text = '{}의 성적 점수를 저장하지 않습니다,')
        new_window.destroy()
    elif y_or_n == 'y':

        df2 = pd.Series([st_num_math, st_num_eng, st_num_kor])
        b = int(df2.sum())
        c = float(df2.mean())
        c= round(c, 2)

        if c > 90:
            df.loc[len(df.index)] =  [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'A']
        elif 90> c >=80:
                df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'B']
        elif 80> c >=70:
                df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'C']
        elif 70> c >=60:
                df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'D']
        elif 60> c :
                df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'F']

        lab13 = Label(new_window, text = '학생 ({})의 점수 합계는 {}점, 평균은 {:.2f} 입니다.'.format(st_num,b ,c ))
        lab13.pack()
        df.index = df['번호']
        df.sort_index()
        btnScore = Button(new_window, text="확인 완료", command=Close)
        btnScore.pack()
        

def LookScore():
    df2 = df.sort_index() 
    new_window = tkinter.Tk()
    new_window.title("성적 현황")
    new_window.geometry('900x700+1000+100')
    def Close():
        new_window.destroy()
    def showgrap():
        fig, ax = plt.subplots()
        ax.boxplot([df['국어'],df['영어'],df["수학"],df['평균']], sym='bo')
        plt.title("grape")
        plt.xticks([1,2,3,4], ['KOR','ENG','MATH','ADV'])
        plt.show()

    treeview = tkinter.ttk.Treeview(new_window, columns=['번호','국어','영어','수학','총점','평균','환산'],
                                        displaycolumns=['번호','국어','영어','수학','총점','평균','환산'] )

    treeview.pack()
    treeview.column("번호", width = 100, anchor="e")
    treeview.heading("번호", text= '번호', anchor= "e")
    
    treeview.column("국어", width = 100, anchor="e")
    treeview.heading("국어", text= '국어', anchor= "e")
    
    treeview.column("영어", width = 100, anchor="e")
    treeview.heading("영어", text= '영어', anchor= "e")
    
    treeview.column("수학", width = 100, anchor="e")
    treeview.heading("수학", text= '수학', anchor= "e")
    
    treeview.column("총점", width = 100, anchor="e")
    treeview.heading("총점", text= '총점', anchor= "e")
    
    treeview.column("평균", width = 100, anchor="e")
    treeview.heading("평균", text= '평균', anchor= "e")                            

    treeview.column("환산", width = 100, anchor="e")
    treeview.heading("환산", text= '환산', anchor= "e")                            

    treeview['show'] = 'headings'
    for i in range(len(df2.index)):
        treeviewList = []
        for col in range(len(df2.columns)):
            treeviewList.append(df2.iat[i,col])

        treeview.insert("","end", text="", values=treeviewList, iid=i) 

    btnshow = Button(new_window, text="그래프 보기", command=showgrap) 
    btnScore = Button(new_window, text="확인 완료", command=Close)
    btnshow.pack()
    btnScore.pack()

def Repair():
    global df
    df2 = df.sort_index()
    new_window = tkinter.Tk()
    new_window.title("성적 수정")
    new_window.geometry('900x900+1000+100')
    def Close():
        new_window.destroy()

    while True:    
        Re_num = askinteger("수정/ 삭제할 번호","수정/ 삭제할 번호를 입력하시오",minvalue=1)
    
        try:

            Re_num = int(Re_num)       

        except ValueError   as e:  # 학번이 정수인지 확인 
            lab3= Label(new_window, text= '{}는 입력할 수 없습니다.'.format(st_num))
            lab3.pack()
            continue
        else:

            i = []
            for a in range(len(df.index)): # 학번이 중복인지 확인 
                
                p = df.index[a] 
                i.append(p)
                continue
            
            if Re_num <= 0: # 학번이 양수인지 확인 
                
                lab4= Label(new_window, text= '{}는 입력할 수 없습니다.'.format(Re_num))
                lab4.pack()
                continue

            
            elif Re_num in i : # 중복인지 확인 
                
                lab5= Label(new_window, text= '학번 {}의 정보입니다.'.format(Re_num))
                lab5.pack()
                break
            
            elif Re_num not in i : # 중복인지 확인 
            
                lab6= Label(new_window, text= '학번 {}의 정보는 없습니다.'.format(Re_num))
                lab6.pack()
                continue

    treeview = tkinter.ttk.Treeview(new_window, columns=['번호','국어','영어','수학','총점','평균','환산'],
                                            displaycolumns=['번호','국어','영어','수학','총점','평균','환산'] )

    treeview.pack()
    treeview.column("번호", width = 100, anchor="e")
    treeview.heading("번호", text= '번호', anchor= "e")
    
    treeview.column("국어", width = 100, anchor="e")
    treeview.heading("국어", text= '국어', anchor= "e")
    
    treeview.column("영어", width = 100, anchor="e")
    treeview.heading("영어", text= '영어', anchor= "e")
    
    treeview.column("수학", width = 100, anchor="e")
    treeview.heading("수학", text= '수학', anchor= "e")
    
    treeview.column("총점", width = 100, anchor="e")
    treeview.heading("총점", text= '총점', anchor= "e")
    
    treeview.column("평균", width = 100, anchor="e")
    treeview.heading("평균", text= '평균', anchor= "e")                            

    treeview.column("환산", width = 100, anchor="e")
    treeview.heading("환산", text= '환산', anchor= "e")                            

    treeview['show'] = 'headings'
    treeviewList = []
    df3 =df2.loc[[Re_num]]
    del_in = df3.index
    del_in = del_in[0]
    print(df3)
    for col in range(len(df2.columns)):
        treeviewList.append(df3.iat[0,col])
    treeview.insert("","end", text="", values=treeviewList, iid=i) 
    lab1 = Label(new_window, text = "해당 정보가 맞습니까(y/n)")
    lab1.pack()
    y_or_n =askstring("해당 정보 확인","해당 정보가맞습니까?(y/n)")
    
    if y_or_n == 'n':
        new_window.destroy()
    
    elif y_or_n == 'y':
        lab1.configure(text='해당 정보가 맞습니까(y/n): y')
        lab2 = Label(new_window, text="(1)수정  (2)삭제")
        lab2.pack()
    lab3 = Label(new_window, text='>>>')
    lab3.pack()
    re_or_drop =askinteger("수정/삭제","수정(1)  삭제(2)")
    
    if re_or_drop == 2:
        lab3.configure(text='>>> 2')
        df = df2.drop(del_in)
        lab7 = Label(new_window, text="{} 의 성적 정보를 삭제 했습니다.".format(Re_num))
        lab7.pack()
        btn_de = Button(new_window, text="완료", command=Close)
        btn_de.pack()
    elif re_or_drop == 1:
        
        lab3.configure(text=">>> 1")
        lab10 = Label(new_window,text="국어 (기본점수 : {}) >".format(df.at[del_in, '국어']))
        lab10.pack()
        
        def cal(event):
            global st_num_kor2
            a = ent1.get()
            if a is "":
                st_num_kor2 = df.at[del_in, '국어']
                lab10.configure(text='국어 (기본 점수 : {}) >'.format(st_num_kor2))
            else:
                try:
                    a =int(a)
                except ValueError as e:
                    lab10.configure(text="정수 0 ~ 100를 입력하시오")
                else:
                    if a < 0:
                        lab10.configure(text="정수 0 ~ 100를 입력하시오")
                    elif a > 100:
                        lab10.configure(text="정수 0 ~ 100를 입력하시오")
                    else:
                        lab10.configure(text='국어 (기본 점수 : {}) > {}'.format(df.at[del_in, '국어'], a ))
                        st_num_kor2 = a

        ent1 =Entry(new_window)
        ent1.bind("<Return>", cal)
        ent1.pack()
        
        lab11 = Label(new_window,text="영어 (기본점수 : {}) >".format(df.at[del_in, '영어']))
        lab11.pack()
        
        def cal2(event):
            global st_num_eng2
            a = ent2.get()
            if a is "":
                st_num_eng2 = df.at[del_in, '영어']
                lab11.configure(text='영어 (기본 점수 : {}) >'.format(st_num_eng2))
            else:
                try:
                    a =int(a)
                except ValueError as e:
                    lab11.configure(text="정수 0 ~ 100를 입력하시오")
                else:
                    if a < 0:
                        lab11.configure(text="정수 0 ~ 100를 입력하시오")
                    elif a > 100:
                        lab11.configure(text="정수 0 ~ 100를 입력하시오")
                    else:
                        lab11.configure(text='영어 (기본 점수 : {}) > {}'.format(df.at[del_in, '영어'], a ))
                        st_num_eng2 = a
        ent2 =Entry(new_window)
        ent2.bind("<Return>", cal2)
        ent2.pack()
        
        lab12 = Label(new_window,text="수학 (기본점수 : {}) >".format(df.at[del_in, '수학']))
        lab12.pack()
        
        def cal3(event):
            global st_num_math2
            a = ent3.get()
            if a is "":
                st_num_math2 = df.at[del_in, '수학']
                
                lab12.configure(text='수학 (기본 점수 : {}) >'.format(st_num_math2))
            else:
                try:
                    a =int(a)
                except ValueError as e:
                    lab12.configure(text="정수 0 ~ 100를 입력하시오")
                else:
                    if a < 0:
                        lab12.configure(text="정수 0 ~ 100를 입력하시오")
                    elif a > 100:
                        lab12.configure(text="정수 0 ~ 100를 입력하시오")
                    else:
                        lab12.configure(text='수학 (기본 점수 : {}) > {}'.format(df.at[del_in, '수학'], a ))
                        st_num_math2 = a
        ent3 =Entry(new_window)
        ent3.bind("<Return>", cal3)
        ent3.pack()

        def fin():
            lab13 = Label(new_window, text='국어 : {}'.format(st_num_kor2))
            lab14 = Label(new_window, text='영어 : {}'.format(st_num_eng2))
            lab15 = Label(new_window, text='수학 : {}'.format(st_num_math2))
            lab16 = Label(new_window, text='위 내용대로 수정 하시겠습니까?(y/n) :')
            lab13.pack()
            lab14.pack()
            lab15.pack()
            lab16.pack()
            yes_or_no = askstring("수정 여부", "수정 내용 저장 여부(y/n) ")
            if yes_or_no == "n":
                new_window.destroy()
            elif yes_or_no == 'y':
                df3 = pd.Series([st_num_kor2, st_num_eng2, st_num_math2])
                b =int(df3.sum())
                c = float(df3.mean())
                c = round(c,2)

                if c >= 90:
                    df.loc[del_in] = [Re_num, st_num_kor2, st_num_eng2, st_num_math2, b, c, 'A']
                elif 90 > c >=80:
                    df.loc[del_in] = [Re_num, st_num_kor2, st_num_eng2, st_num_math2, b, c, 'B']
                elif 80 > c >=70:
                    df.loc[del_in] = [Re_num, st_num_kor2, st_num_eng2, st_num_math2, b, c, 'C']
                elif 70 > c >=60:
                    df.loc[del_in] = [Re_num, st_num_kor2, st_num_eng2, st_num_math2, b, c, 'D']
                elif 60 > c :
                    df.loc[del_in] = [Re_num, st_num_kor2, st_num_eng2, st_num_math2, b, c, 'F']

                new_window.destroy()
        
        bnt_fin = Button(new_window, text ="입력완료", command=fin)
        bnt_fin.pack()

def exit():
    
    fileName = askstring("저장할 파일 이름","파일이름을 입력하시오 :")
    df.to_csv('C:\kim\\{}.csv'.format(fileName), mode ='w', index = False)
    with open('num.txt', 'w', encoding='UTF-8')as f:
        f.write(fileName+'\n')
    window.destroy()
btnList =  [None] * 4

#메인창 출력 
label1 = Label(window, text = '=================================')
label2 = Label(window, text = '==피식 고등학교 성적처리 프로그램==')
label3 = Label(window, text = '=================================')
label4 = Label(window, text = '<<메뉴>>')
btnList[0] = Button(window, text = '1. 성적입력',command=NewWin)
btnList[1] = Button(window, text = '2. 성적현황',command=LookScore)
btnList[2] = Button(window, text = '3. 성적수정',command=Repair)
btnList[3] = Button(window, text = '4. 종료', command=exit)
label9 = Label(window, text = '================================')


label1.pack()
label2.pack()
label3.pack()
label4.pack()
for btn in btnList:
    btn.pack()
    
label9.pack()

window.mainloop()
