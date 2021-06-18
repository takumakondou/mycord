import tkinter
import random
import tkinter.messagebox
import numpy as np
cursor_x=0
cursor_y=0
mouse_x=0
mouse_y=0
mouse_c=0
k=0
r=0
fig=0
px=0
py=0
sign=0
ai_filex=[]
#マウスの座標と、クリック
def mouse_move(e):
    global mouse_x,mouse_y
    mouse_x=e.x
    mouse_y=e.y
def mouse_press(e):
    global mouse_c
    mouse_c=1
def mouse_release(e):
    global mouse_c
    mouse_c=0
#持ち駒の表示
def bring_koma():
    global bring_ban
    for y in range(0,2,1):
        for x in range(0,7,1):
            if bring_ban[y][x]==11 and 1<=bring2_ban[0][x]:
                canvas.create_image(x*40+25,y*40+20,image=enehu,tag="TT")
            elif bring_ban[y][x]==12 and 1<=bring2_ban[0][x]:
                canvas.create_image(x*40+25,y*40+20,image=enekyo,tag="TT")
            elif bring_ban[y][x]==13 and 1<=bring2_ban[0][x]:
                canvas.create_image(x*40+25,y*40+20,image=enekei,tag="TT")
            elif bring_ban[y][x]==14 and 1<=bring2_ban[0][x]:
                canvas.create_image(x*40+25,y*40+20,image=enegin,tag="TT")
            elif bring_ban[y][x]==15 and 1<=bring2_ban[0][x]:
                canvas.create_image(x*40+25,y*40+20,image=enekin,tag="TT")
            elif bring_ban[y][x]==16 and 1<=bring2_ban[0][x]:
                canvas.create_image(x*40+25,y*40+20,image=enekaku,tag="TT")
            elif bring_ban[y][x]==17 and 1<= bring2_ban[0][x]:
                canvas.create_image(x*40+25,y*40+20,image=enehisha,tag="TT")

            if bring_ban[y][x]==1 and 1<= bring2_ban[1][x]:
                canvas.create_image(x*40+25,y*40+380,image=hu,tag="TT")
            if bring_ban[y][x]==2 and 1<=bring2_ban[1][x]:
                canvas.create_image(x*40+25,y*40+380,image=kyo,tag="TT")
            if bring_ban[y][x]==3 and 1<=bring2_ban[1][x]:
                canvas.create_image(x*40+25,y*40+380,image=kei,tag="TT")
            if bring_ban[y][x]==4 and 1<=bring2_ban[1][x]:
                canvas.create_image(x*40+25,y*40+380,image=gin,tag="TT")
            if bring_ban[y][x]==5 and 1<=bring2_ban[1][x]:
                canvas.create_image(x*40+25,y*40+380,image=kin,tag="TT")
            if bring_ban[y][x]==6 and 1<=bring2_ban[1][x]:
                canvas.create_image(x*40+25,y*40+380,image=kaku,tag="TT")
            if bring_ban[y][x]==7 and 1<=bring2_ban[1][x]:
                canvas.create_image(x*40+25,y*40+380,image=hisha,tag="TT")   

          

            if bring2_ban[0][x]==1:
                canvas.create_text(x*40+10,30,text=1,angle=180.0,tag="TT")  
            elif bring2_ban[0][x]==2:
                canvas.create_text(x*40+10,30,text=2,angle=180.0,tag="TT")
            elif bring2_ban[0][x]==3:
                canvas.create_text(x*40+10,30,text=3,angle=180.0,tag="TT")
            elif bring2_ban[0][x]==4:
                canvas.create_text(x*40+10,30,text=4,angle=180.0,tag="TT")
            elif bring2_ban[0][x]==5:
                canvas.create_text(x*40+10,30,text=5,angle=180.0,tag="TT") 
            elif bring2_ban[0][x]==6:
                canvas.create_text(x*40+10,30,text=6,angle=180.0,tag="TT") 
            elif bring2_ban[0][x]==7:
                canvas.create_text(x*40+10,30,text=7,angle=180.0,tag="TT") 
            elif bring2_ban[0][x]==8:
                canvas.create_text(x*40+10,30,text=8,angle=180.0,tag="TT") 
            elif bring2_ban[0][x]==9:
                canvas.create_text(x*40+10,30,text=9,angle=180.0,tag="TT")
            elif bring2_ban[0][x]==10:
                canvas.create_text(x*40+10,30,text=10,angle=180.0,tag="TT")
            elif bring2_ban[0][x]==11:
                canvas.create_text(x*40+10,30,text=11,angle=180.0,tag="TT") 
            elif bring2_ban[0][x]==12:
                canvas.create_text(x*40+10,30,text=12,angle=180.0,tag="TT")
            elif bring2_ban[0][x]==13:
                canvas.create_text(x*40+10,30,text=13,angle=180.0,tag="TT")
            elif bring2_ban[0][x]==14:
                canvas.create_text(x*40+10,30,text=14,angle=180.0,tag="TT")
            elif bring2_ban[0][x]==15:
                canvas.create_text(x*40+10,30,text=15,angle=180.0,tag="TT") 
            elif bring2_ban[0][x]==16:
                canvas.create_text(x*40+10,30,text=16,angle=180.0,tag="TT") 
            elif bring2_ban[0][x]==17:
                canvas.create_text(x*40+10,30,text=17,angle=180.0,tag="TT") 
            elif bring2_ban[0][x]==18:
                canvas.create_text(x*40+10,30,text=18,angle=180.0,tag="TT")

            if bring2_ban[1][x]==1:
                canvas.create_text(x*40+40,410,text=1,tag="TT")  
            elif bring2_ban[1][x]==2:
                canvas.create_text(x*40+40,410,text=2,tag="TT")
            elif bring2_ban[1][x]==3:
                canvas.create_text(x*40+40,410,text=3,tag="TT")
            elif bring2_ban[1][x]==4:
                canvas.create_text(x*40+40,410,text=4,tag="TT")
            elif bring2_ban[1][x]==5:
                canvas.create_text(x*40+40,410,text=5,tag="TT") 
            elif bring2_ban[1][x]==6:
                canvas.create_text(x*40+40,410,text=6,tag="TT") 
            elif bring2_ban[1][x]==7:
                canvas.create_text(x*40+40,410,text=7,tag="TT") 
            elif bring2_ban[1][x]==8:
                canvas.create_text(x*40+40,410,text=8,tag="TT") 
            elif bring2_ban[1][x]==9:
                canvas.create_text(x*40+40,410,text=9,tag="TT")
            elif bring2_ban[1][x]==10:
                canvas.create_text(x*40+40,410,text=10,tag="TT")
            elif bring2_ban[1][x]==11:
                canvas.create_text(x*40+40,410,text=11,tag="TT") 
            elif bring2_ban[1][x]==12:
                canvas.create_text(x*40+40,410,text=12,tag="TT")
            elif bring2_ban[1][x]==13:
                canvas.create_text(x*40+40,410,text=13,tag="TT")
            elif bring2_ban[1][x]==14:
                canvas.create_text(x*40+40,410,text=14,tag="TT")
            elif bring2_ban[1][x]==15:
                canvas.create_text(x*40+40,410,text=15,tag="TT") 
            elif bring2_ban[1][x]==16:
                canvas.create_text(x*40+40,410,text=16,tag="TT") 
            elif bring2_ban[1][x]==17:
                canvas.create_text(x*40+40,410,text=17,tag="TT") 
            elif bring2_ban[1][x]==18:
                canvas.create_text(x*40+40,410,text=18,tag="TT") 
#評価値をだしてその番号を返す。実際の手になる。  
def ban_hyoukati_player():
    global osero_ban
    ai_filex=AI_player(osero_ban,bring2_ban)
    r=random.randint(0,(len(ai_filex)-1))
    return ai_filex[r]
#駒の勝ちの和の計算
def koma_eva(ban):
    eva_ti=0
    for y in range(1,10,1):
        for x in range(1,10,1):
            if ban[y][x]==1:
                eva_ti-=90
            elif ban[y][x]==2:
                eva_ti-=315
            elif ban[y][x]==3:
                eva_ti-=405
            elif ban[y][x]==4:
                eva_ti-=495
            elif ban[y][x]==5:
                eva_ti-=540
            elif ban[y][x]==6:
                eva_ti-=855
            elif ban[y][x]==7:
                eva_ti-=990
            elif ban[y][x]==8:
                eva_ti-=15000

            elif ban[y][x]==21 or ban[y][x]==22 or ban[y][x]==23 or ban[y][x]==24:
                eva_ti-=540
            elif ban[y][x]==26:
                eva_ti-=945
            elif ban[y][x]==27:
                eva_ti-=1395

            elif ban[y][x]==11:
                eva_ti+=90
            elif ban[y][x]==12:
                eva_ti+=315
            elif ban[y][x]==13:
                eva_ti+=405
            elif ban[y][x]==14:
                eva_ti+=495
            elif ban[y][x]==15:
                eva_ti+=540
            elif ban[y][x]==16:
                eva_ti+=855
            elif ban[y][x]==17:
                eva_ti+=990
            elif ban==18:
                eva_ti+=15000

            elif ban[y][x]==31 or ban[y][x]==32 or ban[y][x]==33 or ban[y][x]==34:
                eva_ti+=540
            elif ban[y][x]==36:
                eva_ti+=945
            elif ban[y][x]==37:
                eva_ti+=1395
    
    return eva_ti
#成れるときのメッセージボックス
def message_style():
    TorF=tkinter.messagebox.askyesno("確認","成りますか？")
    return TorF
#実際にAIが指す関数
def judge_te(r):
    global osero_ban
    global bring2_ban
    S=0
    Ty=0
    Tx=0
    Nx=0
    
    S = r // 10000
    Tx = (r // 1000) - (S * 10)
    Ty = (r // 100) - ((Tx * 10) + (S * 100))
    Nx = (r // 10) - ((Ty * 10) + (Tx * 100) + (S * 1000))
    Ny = r % 10
    
    osero_ban[Ty][Tx]=0

    if osero_ban[Ny][Nx] != 0 and (1<=osero_ban[Ny][Nx] and osero_ban[Ny][Nx]<=7):
        bring2_ban[0][osero_ban[Ny][Nx]- 1] += 1
        print(bring2_ban)
        
    elif osero_ban[Ny][Nx] != 0 and (21<=osero_ban[Ny][Nx] and osero_ban[Ny][Nx]<=27):
        bring2_ban[0][osero_ban[Ny][Nx] - 21] += 1
    elif osero_ban[Ny][Nx] == 8:
        print("hello")
    elif osero_ban[Ny][Nx]==0 and Ty==0:
        bring2_ban[0][Tx]-=1
        print(bring2_ban)
        
    osero_ban[Ny][Nx]=S
#駒の表示のための関数
def koma(x,y,a,s):
     if osero_ban[y][x] == a:
                canvas.create_image(x*40-15,y*40+20,image=s,tag="TT")
#駒の可動範囲の表示をリセットする関数
def ban_clear():
    global banban
    for y in range(1,11,1):
        for x in range(0,10,1):
            if banban[y][x]==1:
                banban[y][x]=0
#そこのマスにある駒がプレイヤーの駒か判断
def judge(x,y):
    global osero_ban
    if (1<=osero_ban[y][x] and osero_ban[y][x]<=8) or  (21<=osero_ban[y][x] and osero_ban[y][x]<=27):
        return True
    else:
        False
#そこのマスにある駒がの駒か判断
def judge2(x,y):
    global osero_ban
    if (11<=osero_ban[y][x] and osero_ban[y][x]<=18) or  (31<=osero_ban[y][x] and osero_ban[y][x]<=37):
        return True
    else:
        False
#AI側が打てる手を全て算出する関数
def AI_player(osero_ban,bring2_ban):
    ai_filex=[]
    for t in range(1,9,1):
        for s in range(1,10,1):
            if osero_ban[t][s] == 0 and 1<=bring2_ban[0][0]:
                if osero_ban[8][s] != 11 and osero_ban[1][s] != 11 and osero_ban[2][s] != 11 and osero_ban[3][s] != 11 and osero_ban[4][s] != 11 and osero_ban[5][s] != 11 and osero_ban[6][s] != 11 and osero_ban[7][s] != 11:
                    ai_filex.append(11 * 10000 + 0 * 1000 + 0 * 100 + (s) * 10 + (t))

    for t in range(1,9,1):
        for s in range(1,10,1):
            if osero_ban[t][s] == 0 and 1<=bring2_ban[0][1]:
                ai_filex.append(12 * 10000 + 1 * 1000 + 0 * 100 + (s) * 10 + (t))

    for t in range(1,8,1):
        for s in range(1,10,1):
            if osero_ban[t][s] == 0 and 1<=bring2_ban[0][2]:
                ai_filex.append(13 * 10000 + 2 * 1000 + 0 * 100 + (s) * 10 + (t))

    for t in range(1,10,1):
        for s in range(1,10,1):
            if osero_ban[t][s] == 0 and 1<=bring2_ban[0][3]:
                ai_filex.append(14 * 10000 + 3 * 1000 + 0 * 100 + (s) * 10 + (t))


    for t in range(1,10,1):
        for s in range(1,10,1):
            if osero_ban[t][s] == 0 and 1<=bring2_ban[0][4]:
                ai_filex.append(15 * 10000 + 4 * 1000 + 0 * 100 + (s) * 10 + (t))

    for t in range(1,10,1):
        for s in range(1,10,1):
            if osero_ban[t][s] == 0 and 1<=bring2_ban[0][5]:
                ai_filex.append(16 * 10000 + 5 * 1000 + 0 * 100 + (s) * 10 + (t))

    for t in range(1,10,1):
        for s in range(1,10,1):
            if osero_ban[t][s] == 0 and 1<=bring2_ban[0][6]:
                ai_filex.append(17 * 10000 + 6 * 1000 + 0 * 100 + (s) * 10 + (t))


    for y in range(1,10,1): 
        for x in range(1,10,1):

            if osero_ban[y][x] == 11 and y + 1 <= 9:
                if osero_ban[y + 1][x] == 0 or judge(x,y+1):
                    if y + 1 != 9:
                        ai_filex.append(11 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))
            
                    elif y + 1 == 7 or y+1==8:
                        ai_filex.append(11 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))
                        ai_filex.append(31 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))
                    else:
                        ai_filex.append(31 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))


            if osero_ban[y][x] == 12:
                if y + 1 <= 9:
                    for t in range(y + 1,10,1):
                        if osero_ban[t][x] == 0 or judge(x,t):
                            if t != 9:
                                ai_filex.append(12 * 10000 + x * 1000 + y * 100 + (x) * 10 + (t))
                            elif t== 7 or t==8:
                                ai_filex.append(12 * 10000 + x * 1000 + y * 100 + (x) * 10 + (t))
                                ai_filex.append(32 * 10000 + x * 1000 + y * 100 + (x) * 10 + (t))
                            else:
                                ai_filex.append(32 * 10000 + x * 1000 + y * 100 + (x) * 10 + (t))
                        else:
                            break
                        if (31<=osero_ban[t][x] and osero_ban[t][x]<=37) or (11<=osero_ban[t][x] and osero_ban[t][x]<=18) or judge(x,t):
                            break

            if osero_ban[y][x] == 13 and y + 2 <= 9:
                if x + 1 <= 9:
                    if osero_ban[y + 2][x + 1] == 0 or judge(x+1,y+2):
                        if y + 2 == 8 or y + 2 == 9:
                            ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x + 1) * 10 + (y + 2))
                        elif y + 2 == 7:
                            ai_filex.append(13 * 10000 + x * 1000 + y * 100 + (x + 1) * 10 + (y + 2))
                            ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x + 1) * 10 + (y + 2))
                        else:
                            ai_filex.append(13 * 10000 + x * 1000 + y * 100 + (x + 1) * 10 + (y + 2))

                if 1 <= x - 1:
                    if osero_ban[y + 2][x - 1] == 0 or judge(x-1,y+2):
                        if y + 2 == 8 or y + 2 == 9:
                            ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x - 1) * 10 + (y + 2))
                        elif y + 2 == 7:
                            ai_filex.append(13 * 10000 + x * 1000 + y * 100 + (x - 1) * 10 + (y + 2))
                            ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x - 1) * 10 + (y + 2))
                        else:
                            ai_filex.append(13 * 10000 + x * 1000 + y * 100 + (x - 1) * 10 + (y + 2))

            if (osero_ban[y][x] == 14):
                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge(x,y+1): 
                        if y + 1 == 7 or y+1== 8 or y+1== 9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))
                        else:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))

                if 1 <= y - 1 and 1<= x - 1:
                    if osero_ban[y - 1][x-1] == 0 or judge(x-1,y-1): 
                        if y -1 == 7 or y-1== 8 or y-1== 9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y - 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y - 1))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y - 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y - 1))
                        else:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y - 1))
            
                if 1 <= y - 1 and x + 1 <= 9:
                    if osero_ban[y -1][x+1] == 0 or judge(x+1,y-1): 
                        if y - 1 == 7 or y-1== 8 or y-1== 9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y - 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y - 1))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y - 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y - 1))
                        else:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y - 1))
                
                if y + 1 <= 9 and 1 <= x - 1:
                    if osero_ban[y + 1][x-1] == 0 or judge(x-1,y+1): 
                        if y + 1 == 7 or y+1== 8 or y+1== 9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y + 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y + 1))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y + 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y + 1))
                        else:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y + 1))
                
                if y + 1 <= 9 and x + 1 <= 9:
                    if osero_ban[y + 1][x+1] == 0 or judge(x+1,y+1): 
                        if y + 1 == 7 or y+1== 8 or y+1== 9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y + 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y + 1))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y + 1))
                            ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y + 1))
                        else:
                            ai_filex.append(14 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y + 1))
                
            if osero_ban[y][x] == 15:
                if 1 <= y - 1:
                    if osero_ban[y - 1][x] == 0 or judge(x,y-1):
                        ai_filex.append(15 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y - 1))
  
                if y + 1 <= 9 and 1 <= x - 1:
                    if osero_ban[y + 1][x - 1] == 0 or judge(x-1,y+1):
                        ai_filex.append(15 * 10000 + x * 1000 + y * 100 + (x - 1) * 10 + (y + 1))

                if y + 1 <= 9 and x + 1 <= 9:
                    if osero_ban[y + 1][x + 1] == 0 or judge(x+1,y+1):
                        ai_filex.append(15 * 10000 + x * 1000 + y * 100 + (x + 1) * 10 + (y + 1))

                if 1 <= x - 1:
                    if osero_ban[y][x - 1] == 0 or judge(x-1,y):
                        ai_filex.append(15 * 10000 + x * 1000 + y * 100 + (x - 1) * 10 + (y))

                if x + 1 <= 9:
                    if osero_ban[y][x + 1] == 0 or judge(x+1,y):
                        ai_filex.append(15 * 10000 + x * 1000 + y * 100 + (x + 1) * 10 + (y))

                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge(x,y+1):
                        ai_filex.append(15 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + 1))

            if osero_ban[y][x] == 16:
                a = 1
                while (1 <= y - a and 1 <= x - a):
                    if osero_ban[y - a][x - a] == 0 or judge(x-a,y-a):
                        if y - a ==7 or y-a==8 or y-a==9:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y - a))
                            ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y - a))
                        elif 1<=y-a and y - a <=6:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y - a))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y - a))
                            ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y - a))
                        
                    if judge(x-a,y-a):
                        break
                    if (11<=osero_ban[y - a][x - a] and osero_ban[y-a][x-a]<=18) or (31<=osero_ban[y - a][x - a] and osero_ban[y-a][x-a]<=37):
                        break
                    
                    a=a+1
                
            if osero_ban[y][x] == 16:
                a = 1
                while (y + a <= 9 and x + a <= 9):
                    if osero_ban[y + a][x + a] == 0 or judge(x+a,y+a):
                        if y + a ==7 or y+a==8 or y+a==9:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y + a))
                            ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y + a))
                        elif 1<=y+a and y + a <=6:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y + a))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x+a) * 10 + (y + a))
                            ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x+a) * 10 + (y + a))
                        
                    if judge(x+a,y+a):
                        break
                    if (11<=osero_ban[y + a][x + a] and osero_ban[y+a][x+a]<=18) or (31<=osero_ban[y + a][x +a] and osero_ban[y+a][x+a]<=37):
                        break
                    
                    a=a+1
                
            if osero_ban[y][x] == 16:
                a = 1
                while (1 <= x - a and y + a <= 9):
                    if osero_ban[y + a][x - a] == 0 or judge(x-a,y+a):
                        if y + a ==7 or y+a==8 or y+a==9:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y + a))
                            ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y + a))
                        elif 1<=y+a and y + a <=6:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y + a))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y + a))
                            ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y + a))
                        
                    if judge(x-a,y+a):
                        break
                    if (11<=osero_ban[y + a][x - a] and osero_ban[y+a][x-a]<=18) or (31<=osero_ban[y +a][x - a] and osero_ban[y+a][x-a]<=37):
                        break
                    
                    a=a+1
                
            if osero_ban[y][x] == 16:
                a = 1
                while (x + a <= 9 and 1 <= y - a):
                    if osero_ban[y - a][x + a] == 0 or judge(x+a,y-a):
                        if y - a ==7 or y-a==8 or y-a==9:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y - a))
                            ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y - a))
                        elif 1<=y-a and y - a <=6:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y - a))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(16 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y - a))
                            ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y - a))
                        
                    if judge(x+a,y-a):
                        break
                    if (11<=osero_ban[y - a][x + a] and osero_ban[y-a][x+a]<=18) or (31<=osero_ban[y - a][x + a] and osero_ban[y-a][x+a]<=37):
                        break
                    
                    a=a+1
            if osero_ban[y][x] == 17:
                a = 1
                while (1 <= y - a):
                    if osero_ban[y - a][x] == 0 or judge(x,y-a):
                        if y - a ==7 or y-a==8 or y-a==9:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y - a))
                            ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y - a))
                        elif 1<=y - a and y-a<=6:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y - a))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y - a))
                            ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y - a))
                        
                    if judge(x,y-a):
                        break
                
                    if (11<=osero_ban[y - a][x] and osero_ban[y-a][x]<=18) or (31<=osero_ban[y - a][x] and osero_ban[y-a][x]<=37):
                        break
                
                    a=a+1
            if osero_ban[y][x] == 17:
                a = 1
                while y + a <= 9:
                    if osero_ban[y + a][x] == 0 or judge(x,y+a):
                        if y + a ==7 or y+ a==8 or y+a==9:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + a))
                            ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + a))
                        elif 1<=y + a and y+a<=6:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + a))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + a))
                            ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y + a))
                        
                    if judge(x,y+a):
                        break
                
                    if (11<=osero_ban[y + a][x] and osero_ban[y+a][x]<=18) or (31<=osero_ban[y + a][x] and osero_ban[y+a][x]<=37):
                        break
                
                    a=a+1
            if osero_ban[y][x] == 17:
                a = 1
                while 1 <= x - a:
                    if osero_ban[y][x-a] == 0 or judge(x-a,y):
                        if y ==7 or y==8 or y==9:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x-a) * 10 + (y))
                            ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x-a) * 10 + (y))
                        elif 1<=y and y<=6:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x-a) * 10 + (y))
                        elif y==7 or y==8 or y==9:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x-a) * 10 + (y))
                            ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x-a) * 10 + (y))
                        
                    if judge(x-a,y):
                        break
                
                    if (11<=osero_ban[y][x-a] and osero_ban[y][x-a]<=18) or (31<=osero_ban[y][x-a] and osero_ban[y][x-a]<=37):
                        break
                
                    a=a+1
            if osero_ban[y][x] == 17:
                a = 1
                while x + a <= 9:
                    if osero_ban[y][x+a] == 0 or judge(x+a,y):
                        if y ==7 or y==8 or y==9:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x+a) * 10 + (y))
                            ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x+a) * 10 + (y))
                        if 1<=y and y<=6:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x+a) * 10 + (y))
                        if y==7 or y==8 or y==9:
                            ai_filex.append(17 * 10000 + x * 1000 + y * 100 + (x+a) * 10 + (y))
                            ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x+a) * 10 + (y))
                        
                    if judge(x+a,y):
                        break
                
                    if (11<=osero_ban[y][x+a] and osero_ban[y][x+a]<=18) or (31<=osero_ban[y][x+a] and osero_ban[y][x+a]<=37):
                        break
                
                    a=a+1
            if osero_ban[y][x] == 18:
                if 1 <= y - 1:
                    if osero_ban[y - 1][x] == 0 or judge(x,y-1):
                        ai_filex.append(18 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y - 1))
                    
                if 1 <= y - 1 and 1 <= x - 1:
                    if osero_ban[y - 1][x-1] == 0 or judge(x-1,y-1):
                        ai_filex.append(18 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y - 1))

                if 1 <= y - 1 and x + 1 <= 9:
                    if osero_ban[y - 1][x+1] == 0 or judge(x+1,y-1):
                        ai_filex.append(18 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y - 1))

                if 1 <= x - 1:
                    if osero_ban[y][x-1] == 0 or judge(x-1,y):
                        ai_filex.append(18 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y))
                
                if x + 1 <= 9:
                    if osero_ban[y][x+1] == 0 or judge(x+1,y):
                        ai_filex.append(18 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y))

                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge(x,y+1):
                        ai_filex.append(18 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y +1))

                if 1 <= x - 1 and y + 1 <= 9:
                    if osero_ban[y + 1][x-1] == 0 or judge(x-1,y+1):
                        ai_filex.append(18 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y +1))

                if x + 1 <= 9 and y + 1 <= 9:
                    if osero_ban[y + 1][x+1] == 0 or judge(x+1,y+1):
                        ai_filex.append(18 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y +1))

            elif osero_ban[y][x] == 31:
                if 1 <= y - 1:
                    if osero_ban[y - 1][x] == 0 or judge(x,y-1):
                        ai_filex.append(31 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y -1))

                if y + 1 <= 9 and 1 <= x - 1:
                    if osero_ban[y +1][x-1] == 0 or judge(x-1,y+1):
                        ai_filex.append(31 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y+1))
               
                if y + 1 <= 9 and x + 1 <= 9:
                    if osero_ban[y + 1][x+1] == 0 or judge(x+1,y+1):
                        ai_filex.append(31 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y+1))
                if 1 <= x - 1:
                    if osero_ban[y][x-1] == 0 or judge(x-1,y):
                        ai_filex.append(31 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y))

                if x + 1 <= 9:
                    if osero_ban[y][x+1] == 0 or judge(x+1,y):
                        ai_filex.append(31 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y))
                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge(x,y+1):
                        ai_filex.append(31 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y+1))
            elif osero_ban[y][x] == 32:
                if 1 <= y - 1:
                    if osero_ban[y - 1][x] == 0 or judge(x,y-1):
                        ai_filex.append(32 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y -1))

                if y + 1 <= 9 and 1 <= x - 1:
                    if osero_ban[y +1][x-1] == 0 or judge(x-1,y+1):
                        ai_filex.append(32 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y+1))
               
                if y + 1 <= 9 and x + 1 <= 9:
                    if osero_ban[y + 1][x+1] == 0 or judge(x+1,y+1):
                        ai_filex.append(32 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y+1))
                if 1 <= x - 1:
                    if osero_ban[y][x-1] == 0 or judge(x-1,y):
                        ai_filex.append(32 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y))

                if x + 1 <= 9:
                    if osero_ban[y][x+1] == 0 or judge(x+1,y):
                        ai_filex.append(32 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y))
                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge(x,y+1):
                        ai_filex.append(32 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y+1))

            elif osero_ban[y][x] == 33:
                if 1 <= y - 1:
                    if osero_ban[y - 1][x] == 0 or judge(x,y-1):
                        ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y -1))

                if y + 1 <= 9 and 1 <= x - 1:
                    if osero_ban[y +1][x-1] == 0 or judge(x-1,y+1):
                        ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y+1))
               
                if y + 1 <= 9 and x + 1 <= 9:
                    if osero_ban[y + 1][x+1] == 0 or judge(x+1,y+1):
                        ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y+1))
                if 1 <= x - 1:
                    if osero_ban[y][x-1] == 0 or judge(x-1,y):
                        ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y))

                if x + 1 <= 9:
                    if osero_ban[y][x+1] == 0 or judge(x+1,y):
                        ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y))
                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge(x,y+1):
                        ai_filex.append(33 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y+1))

            if osero_ban[y][x] == 34:
                if 1 <= y - 1:
                    if osero_ban[y - 1][x] == 0 or judge(x,y-1):
                        ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y -1))

                if y + 1 <= 9 and 1 <= x - 1:
                    if osero_ban[y +1][x-1] == 0 or judge(x-1,y+1):
                        ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y+1))
               
                if y + 1 <= 9 and x + 1 <= 9:
                    if osero_ban[y + 1][x+1] == 0 or judge(x+1,y+1):
                        ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y+1))
                if 1 <= x - 1:
                    if osero_ban[y][x-1] == 0 or judge(x-1,y):
                        ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y))

                if x + 1 <= 9:
                    if osero_ban[y][x+1] == 0 or judge(x+1,y):
                        ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y))
                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge(x,y+1):
                        ai_filex.append(34 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y+1))

            if osero_ban[y][x] == 36:
                if 1 <= y - 1:
                    if osero_ban[y - 1][x] == 0 or judge(x,y-1):
                        ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y - 1))
                
                if 1 <= x - 1:
                    if osero_ban[y][x-1] == 0 or judge(x-1,y):
                        ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y))
                
                if x + 1 <= 9:
                    if osero_ban[y][x+1] == 0 or judge(x+1,y):
                        ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y))

                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge(x,y+1):
                        ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y +1))

            if osero_ban[y][x] == 36:
                a=1
                while 1 <= y - a and 1 <= x - a:
                    if osero_ban[y - a][x - a] == 0 or judge(x-a,y-a):
                        ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y - a))   
                    if judge(x-a,y-a):
                        break
                    if (11<=osero_ban[y - a][x - a] and osero_ban[y-a][x-a]<=18) or (31<=osero_ban[y - a][x - a] and osero_ban[y-a][x-a]<=37):
                        break
                    a=a+1

            if osero_ban[y][x] == 36:
                a = 1
                while y + a <= 9 and x + a <= 9:
                    if osero_ban[y + a][x + a] == 0 or judge(x+a,y+a):
                        ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y + a))  
                    if judge(x+a,y+a):
                        break
                    if (11<=osero_ban[y + a][x + a] and osero_ban[y+a][x+a]<=18) or (31<=osero_ban[y + a][x + a] and osero_ban[y+a][x+a]<=37):
                        break
                    a=a+1
            if osero_ban[y][x] == 36:
                a=1
                while 1 <= x - a and y + a <= 9:
                    if osero_ban[y + a][x - a] == 0 or judge(x-a,y+a):
                        ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x - a) * 10 + (y + a))   
                    if judge(x-a,y+a):
                        break
                    if (11<=osero_ban[y + a][x - a] and osero_ban[y+a][x-a]<=18) or (31<=osero_ban[y + a][x - a] and osero_ban[y+a][x-a]<=37):
                        break
                    a=a+1
                a = 1
                while x + a <= 9 and 1<= y - a:
                    if osero_ban[y - a][x + a] == 0 or judge(x+a,y-a):
                        ai_filex.append(36 * 10000 + x * 1000 + y * 100 + (x + a) * 10 + (y - a))   
                    if judge(x+a,y-a):
                        break
                    if (11<=osero_ban[y - a][x + a] and osero_ban[y-a][x+a]<=18) or (31<=osero_ban[y - a][x +a] and osero_ban[y-a][x+a]<=37):
                        break
                    a=a+1
            if osero_ban[y][x] == 37:
                a = 1
                while 1 <= y - a:
                    if osero_ban[y-a][x] == 0 or judge(x,y-a):
                        ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y-a))   
                    if judge(x,y-a):
                        break
                
                    if (11<=osero_ban[y-a][x] and osero_ban[y-a][x]<=18) or (31<=osero_ban[y-a][x] and osero_ban[y-a][x]<=37):
                        break
                    a=a+1
            if osero_ban[y][x] == 37:
                a = 1
                while y + a <= 9:
                    if osero_ban[y+a][x] == 0 or judge(x,y+a):
                        ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x) * 10 + (y+a))   
                    if judge(x,y+a):
                        break
                    if (11<=osero_ban[y+a][x] and osero_ban[y+a][x]<=18) or (31<=osero_ban[y+a][x] and osero_ban[y+a][x]<=37):
                        break
                    a=a+1
                
            if osero_ban[y][x] == 37:
                a = 1
                while 1<= x - a:
                    if osero_ban[y][x-a] == 0 or judge(x-a,y):
                        ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x-a) * 10 + (y))   
                    if judge(x-a,y):
                        break
                
                    if (11<=osero_ban[y][x-a] and osero_ban[y][x-a]<=18) or (31<=osero_ban[y][x-a] and osero_ban[y][x-a]<=37):
                        break
                    a=a+1

            if osero_ban[y][x] == 37:
                a = 1
                while x + a <= 9:
                    if osero_ban[y][x+a] == 0 or judge(x+a,y):
                        ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x+a) * 10 + (y))   
                    if judge(x+a,y):
                        break
                
                    if (11<=osero_ban[y][x+a] and osero_ban[y][x+a]<=18) or (31<=osero_ban[y][x+a] and osero_ban[y][x+a]<=37):
                        break
                    a=a+1
   
                if 1 <= y - 1 and 1 <= x - 1:
                    if osero_ban[y - 1][x-1] == 0 or judge(x-1,y-1):
                        ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y - 1))

                if 1 <= y - 1 and x + 1 <= 9:
                    if osero_ban[y - 1][x+1] == 0 or judge(x+1,y-1):
                        ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y - 1))

               

                if 1 <= x - 1 and y + 1 <= 9:
                    if osero_ban[y + 1][x-1] == 0 or judge(x-1,y+1):
                        ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x-1) * 10 + (y +1))

                if x + 1 <= 9 and y + 1 <= 9:
                    if osero_ban[y + 1][x+1] == 0 or judge(x+1,y+1):
                        ai_filex.append(37 * 10000 + x * 1000 + y * 100 + (x+1) * 10 + (y +1))
    return ai_filex
#プレイヤー側が動ける範囲を示す。GUIに表示するときのための関数
def player(x,y):
    global osero_ban,bring2_ban
    global ai_filex,banban
    if osero_ban[y][x]!=0 and judge(x,y):
        banban[y][x]=1

    if y==10 and x==1:    
        banban[10][0]=1
    if y==10 and x==2:    
        banban[10][1]=1
    if y==10 and x==3:    
        banban[10][2]=1
    if y==10 and x==4:    
        banban[10][3]=1
    if y==10 and x==5:    
        banban[10][4]=1
    if y==10 and x==6:    
        banban[10][5]=1
    if y==10 and x==7:    
        banban[10][6]=1
  

            

    if y==10 and x==1:
        for t in range(1,9,1):
            for s in range(1,10,1):
                if osero_ban[t][s] == 0 and 1<=bring2_ban[1][0]:
                    if osero_ban[8][s] !=1 and osero_ban[9][s] !=1 and osero_ban[2][s] != 1 and osero_ban[3][s] !=1 and osero_ban[4][s] !=1 and osero_ban[5][s] !=1 and osero_ban[6][s] !=1 and osero_ban[7][s] !=1:
                        banban[t][s]=1


    if y==10 and x==2:
        for t in range(1,9,1):
            for s in range(1,10,1):
                if osero_ban[t][s] == 0 and 1<=bring2_ban[1][1]:
                    banban[t][s]=1

    if y==10 and x==3:
        for t in range(1,8,1):
            for s in range(1,10,1):
                if osero_ban[t][s] == 0 and 1<=bring2_ban[1][2]:
                    banban[t][s]=1

    if y==10 and x==4:
        for t in range(1,10,1):
            for s in range(1,10,1):
                if osero_ban[t][s] == 0 and 1<=bring2_ban[1][3]:
                    banban[t][s]=1

    if y==10 and x==5:
        for t in range(1,10,1):
            for s in range(1,10,1):
                if osero_ban[t][s] == 0 and 1<=bring2_ban[1][4]:
                    banban[t][s]=1

    if y==10 and x==6:
        for t in range(1,10,1):
            for s in range(1,10,1):
                if osero_ban[t][s] == 0 and 1<=bring2_ban[1][5]:
                    banban[t][s]=1

    if y==10 and x==7:
        for t in range(1,10,1):
            for s in range(1,10,1):
                if osero_ban[t][s] == 0 and 1<=bring2_ban[1][6]:
                    banban[t][s]=1





    if osero_ban[y][x] == 1 and 1 <= y - 1:
        if osero_ban[y - 1][x] == 0 or judge2(x,y-1):
            banban[y-1][x]=1


    if osero_ban[y][x] == 2:
        if  1 <= y - 1:
            for t in range(y-1,0,-1):
                if osero_ban[t][x] == 0 or judge2(x,t):
                    banban[t][x]=1
                else:
                    break
                if (21<=osero_ban[t][x] and osero_ban[t][x]<=27) or (1<=osero_ban[t][x] and osero_ban[t][x]<=8) or judge2(x,t):
                    break

    if osero_ban[y][x] == 3 and 1 <= y - 2:
        if 1<= x - 1:
            if osero_ban[y - 2][x - 1] == 0 or judge2(x-1,y-2):
                banban[y-2][x-1]=1

        if x + 1 <= 9:
            if osero_ban[y - 2][x + 1] == 0 or judge2(x+1,y-2):
                banban[y-2][x+1]=1

    if osero_ban[y][x] == 4:
        if 1 <= y - 1:
            if osero_ban[y - 1][x] == 0 or judge2(x,y-1): 
                banban[y-1][x]=1

        if 1 <= y - 1 and 1<= x - 1:
            if osero_ban[y - 1][x-1] == 0 or judge2(x-1,y-1): 
                banban[y-1][x-1]=1
            
        if 1 <= y - 1 and x + 1 <= 9:
            if osero_ban[y -1][x+1] == 0 or judge2(x+1,y-1):
                banban[y-1][x+1]=1
    
        if y + 1 <= 9 and 1 <= x - 1:
            if osero_ban[y + 1][x-1] == 0 or judge2(x-1,y+1):
                banban[y+1][x-1]=1
                    
                
        if y + 1 <= 9 and x + 1 <= 9:
            if osero_ban[y + 1][x+1] == 0 or judge2(x+1,y+1):
                banban[y+1][x+1]=1
                        
    if osero_ban[y][x] == 5:
        if 1 <= y - 1:
            if osero_ban[y - 1][x] == 0 or judge2(x,y-1):
                banban[y-1][x]=1
  
        if 1 <= y - 1 and 1 <= x - 1:
            if osero_ban[y - 1][x - 1] == 0 or judge2(x-1,y-1):
                banban[y-1][x-1]=1

        if 1 <= y - 1 and x + 1 <= 9:
            if osero_ban[y - 1][x + 1] == 0 or judge2(x+1,y-1):
                banban[y-1][x+1]=1

        if 1 <= x - 1:
            if osero_ban[y][x - 1] == 0 or judge2(x-1,y):
                banban[y][x-1]=1

        if x + 1 <= 9:
            if osero_ban[y][x + 1] == 0 or judge2(x+1,y):
                banban[y][x+1]=1

        if y + 1 <= 9:
            if osero_ban[y + 1][x] == 0 or judge2(x,y+1):
                banban[y+1][x]=1

    if osero_ban[y][x] == 6:
        a = 1
        while (1 <= y - a and 1 <= x - a):
            if osero_ban[y - a][x - a] == 0 or judge2(x-a,y-a):
                banban[y-a][x-a]=1
                        
            if judge2(x-a,y-a):
                break
            if (1<=osero_ban[y - a][x - a] and osero_ban[y-a][x-a]<=8) or (21<=osero_ban[y - a][x - a] and osero_ban[y-a][x-a]<=27):
                break
                    
            a=a+1
                
    if osero_ban[y][x] == 6:
        a = 1
        while (y + a <= 9 and x + a <= 9):
            if osero_ban[y + a][x + a] == 0 or judge2(x+a,y+a):
                banban[y+a][x+a]=1
                        
            if judge2(x+a,y+a):
                break
            if (1<=osero_ban[y + a][x + a] and osero_ban[y+a][x+a]<=8) or (21<=osero_ban[y + a][x +a] and osero_ban[y+a][x+a]<=27):
                break
                    
            a=a+1
                
    if osero_ban[y][x] == 6:
        a = 1
        while (1 <= x - a and y + a <= 9):
            if osero_ban[y + a][x - a] == 0 or judge2(x-a,y+a):
                banban[y+a][x-a]=1
                        
            if judge2(x-a,y+a):
                break
            if (1<=osero_ban[y + a][x - a] and osero_ban[y+a][x-a]<=8) or (21<=osero_ban[y +a][x - a] and osero_ban[y+a][x-a]<=27):
                break
                    
            a=a+1
                
    if osero_ban[y][x] == 6:
        a = 1
        while (x + a <= 9 and 1 <= y - a):
            if osero_ban[y - a][x + a] == 0 or judge2(x+a,y-a):
                banban[y-a][x+a]=1
    
            if judge2(x+a,y-a):
                break
            if (1<=osero_ban[y - a][x + a] and osero_ban[y-a][x+a]<=8) or (21<=osero_ban[y - a][x + a] and osero_ban[y-a][x+a]<=27):
                break
            a=a+1

    if osero_ban[y][x] == 7:
        a = 1
        while (1 <= y - a):
            if osero_ban[y - a][x] == 0 or judge2(x,y-a):
                banban[y-a][x]=1
                        
            if judge2(x,y-a):
                break
            if (1<=osero_ban[y - a][x] and osero_ban[y-a][x]<=8) or (21<=osero_ban[y - a][x] and osero_ban[y-a][x]<=27):
                break
                
            a=a+1
    if osero_ban[y][x] == 7:
        a = 1
        while y + a <= 9:
            if osero_ban[y + a][x] == 0 or judge2(x,y+a):
                banban[y+a][x]=1
                        
            if judge2(x,y+a):
                break
                
            if (1<=osero_ban[y + a][x] and osero_ban[y+a][x]<=8) or (21<=osero_ban[y + a][x] and osero_ban[y+a][x]<=27):
                break
                
            a=a+1
    if osero_ban[y][x] == 7:
        a = 1
        while 1 <= x - a:
            if osero_ban[y][x-a] == 0 or judge2(x-a,y):
                banban[y][x-a]=1        
            if judge2(x-a,y):
                break
                
            if (1<=osero_ban[y][x-a] and osero_ban[y][x-a]<=8) or (21<=osero_ban[y][x-a] and osero_ban[y][x-a]<=27):
                break
                          
            a=a+1
    if osero_ban[y][x] == 7:
        a = 1
        while x + a <= 9:
            if osero_ban[y][x+a] == 0 or judge2(x+a,y):
                banban[y][x+a]=1
                        
            if judge2(x+a,y):
                break            
            if (1<=osero_ban[y][x+a] and osero_ban[y][x+a]<=8) or (21<=osero_ban[y][x+a] and osero_ban[y][x+a]<=27):
                break
                
            a=a+1
    if osero_ban[y][x] == 8:
        if 1 <= y - 1:
            if osero_ban[y - 1][x] == 0 or judge2(x,y-1):
                banban[y-1][x]=1
                    
        if 1 <= y - 1 and 1 <= x - 1:
            if osero_ban[y - 1][x-1] == 0 or judge2(x-1,y-1):
                    banban[y-1][x-1]=1

        if 1 <= y - 1 and x + 1 <= 9:
            if osero_ban[y - 1][x+1] == 0 or judge2(x+1,y-1):
                banban[y-1][x+1]=1

        if 1 <= x - 1:
            if osero_ban[y][x-1] == 0 or judge2(x-1,y):
                banban[y][x-1]=1
                
        if x + 1 <= 9:
            if osero_ban[y][x+1] == 0 or judge2(x+1,y):
                banban[y][x+1]=1

        if y + 1 <= 9:
            if osero_ban[y + 1][x] == 0 or judge2(x,y+1):
                banban[y+1][x]=1

        if 1 <= x - 1 and y + 1 <= 9:
            if osero_ban[y + 1][x-1] == 0 or judge2(x-1,y+1):
                banban[y+1][x-1]=1

        if x + 1 <= 9 and y + 1 <= 9:
            if osero_ban[y + 1][x+1] == 0 or judge2(x+1,y+1):
                banban[y+1][x+1]=1

    if osero_ban[y][x] == 21 or osero_ban[y][x]==22 or osero_ban[y][x]==23 or osero_ban[y][x]==24:
        if 1 <= y - 1:
            if osero_ban[y - 1][x] == 0 or judge2(x,y-1):
                banban[y-1][x]=1

        if 1 <= y - 1 and 1 <= x - 1:
            if osero_ban[y-1][x-1] == 0 or judge2(x-1,y-1):
                banban[y-1][x-1]=1
               
        if 1 <= y - 1 and x + 1 <= 9:
            if osero_ban[y - 1][x+1] == 0 or judge2(x+1,y-1):
                banban[y-1][x+1]=1

        if 1 <= x - 1:
            if osero_ban[y][x-1] == 0 or judge2(x-1,y):
                banban[y][x-1]=1

        if x + 1 <= 9:
            if osero_ban[y][x+1] == 0 or judge2(x+1,y):
                banban[y][x+1]=1

        if y + 1 <= 9:
            if osero_ban[y + 1][x] == 0 or judge2(x,y+1):
                banban[y+1][x]=1
                
   

    if osero_ban[y][x] == 26:
                if 1 <= y - 1:
                    if osero_ban[y - 1][x] == 0 or judge2(x,y-1):
                        banban[y-1][x]=1
                
                if 1 <= x - 1:
                    if osero_ban[y][x-1] == 0 or judge2(x-1,y):
                        banban[y][x-1]=1
                
                if x + 1 <= 9:
                    if osero_ban[y][x+1] == 0 or judge2(x+1,y):
                        banban[y][x+1]=1

                if y + 1 <= 9:
                    if osero_ban[y + 1][x] == 0 or judge2(x,y+1):
                        banban[y+1][x]=1

    if osero_ban[y][x] == 26:
        a=1
        while 1 <= y - a and 1 <= x - a:
            if osero_ban[y - a][x - a] == 0 or judge2(x-a,y-a):
                banban[y-a][x-a]=1  
            if judge2(x-a,y-a):
                break
            if (1<=osero_ban[y - a][x - a] and osero_ban[y-a][x-a]<=8) or (21<=osero_ban[y - a][x - a] and osero_ban[y-a][x-a]<=27):
                break
            a=a+1

    if osero_ban[y][x] == 26:
        a = 1
        while y + a <= 9 and x + a <= 9:
            if osero_ban[y + a][x + a] == 0 or judge2(x+a,y+a):
                banban[y+a][x+a]=1
            if judge2(x+a,y+a):
                break
            if (1<=osero_ban[y + a][x + a] and osero_ban[y+a][x+a]<=8) or (21<=osero_ban[y + a][x + a] and osero_ban[y+a][x+a]<=27):
                break
            a=a+1
    if osero_ban[y][x] == 26:
        a=1
        while 1 <= x - a and y + a <= 9:
            if osero_ban[y + a][x - a] == 0 or judge2(x-a,y+a):
                banban[y+a][x-a]=1
            if judge2(x-a,y+a):
                break
            if (1<=osero_ban[y + a][x - a] and osero_ban[y+a][x-a]<=8) or (21<=osero_ban[y + a][x - a] and osero_ban[y+a][x-a]<=27):
                break
            a=a+1
    if osero_ban[y][x] == 26:
        a = 1
        while x + a <= 9 and 1<= y - a:
            if osero_ban[y - a][x + a] == 0 or judge2(x+a,y-a):
                banban[y-a][x+a]=1  
            if judge2(x+a,y-a):
                break
            if (1<=osero_ban[y - a][x + a] and osero_ban[y-a][x+a]<=8) or (21<=osero_ban[y - a][x +a] and osero_ban[y-a][x+a]<=27):
                break
            a=a+1
    if osero_ban[y][x] == 27:
        a = 1
        while 1 <= y - a:
            if osero_ban[y-a][x] == 0 or judge2(x,y-a):
                banban[y-a][x]=1  
            if judge2(x,y-a):
                break
            
            if (1<=osero_ban[y-a][x] and osero_ban[y-a][x]<=8) or (21<=osero_ban[y-a][x] and osero_ban[y-a][x]<=27):
                break
            a=a+1
    if osero_ban[y][x] == 27:
        a = 1
        while y + a <= 9:
            if osero_ban[y+a][x] == 0 or judge2(x,y+a):
                banban[y+a][x]=1   
            if judge2(x,y+a):
                break
            if (1<=osero_ban[y+a][x] and osero_ban[y+a][x]<=8) or (21<=osero_ban[y+a][x] and osero_ban[y+a][x]<=27):
                break
            a=a+1
                
    if osero_ban[y][x] == 27:
        a = 1
        while 1<= x - a:
            if osero_ban[y][x-a] == 0 or judge2(x-a,y):
                banban[y][x-a]=1  
            if judge2(x-a,y):
                break
                
            if (1<=osero_ban[y][x-a] and osero_ban[y][x-a]<=8) or (21<=osero_ban[y][x-a] and osero_ban[y][x-a]<=27):
                break
            a=a+1

    if osero_ban[y][x] == 27:
        a = 1
        while x + a <= 9:
            if osero_ban[y][x+a] == 0 or judge2(x+a,y):
                banban[y][x+a]=1   
            if judge2(x+a,y):
                break
                
            if (1<=osero_ban[y][x+a] and osero_ban[y][x+a]<=8) or (21<=osero_ban[y][x+a] and osero_ban[y][x+a]<=27):
                break
            a=a+1
   
        if 1 <= y - 1 and 1 <= x - 1:
            if osero_ban[y - 1][x-1] == 0 or judge2(x-1,y-1):
                banban[y-1][x-1]=1

        if 1 <= y - 1 and x + 1 <= 9:
            if osero_ban[y - 1][x+1] == 0 or judge2(x+1,y-1):
                banban[y-1][x+1]=1

        if 1 <= x - 1 and y + 1 <= 9:
            if osero_ban[y + 1][x-1] == 0 or judge2(x-1,y+1):
                banban[y+1][x-1]=1
                        
        if x + 1 <= 9 and y + 1 <= 9:
            if osero_ban[y + 1][x+1] == 0 or judge2(x+1,y+1):
                banban[y+1][x+1]=1
#実際にGUIに表示する線の生成
def player_posi():
    global banban
    for y in range(1,10,1):
        for x in range(1,10,1):
            if banban[y][x]==1:
                canvas.create_line(x*40-35,y*40,x*40-35,y*40+39,fill="#FF00FF",width=2,tag="TB")
                canvas.create_line(x*40+4,y*40,x*40+4,y*40+39,fill="#FF00FF",width=2,tag="TB")
                canvas.create_line(x*40-35,y*40,x*40+4,y*40,fill="#FF00FF",width=2,tag="TB")
                canvas.create_line(x*40-35,y*40+39,x*40+4,y*40+39,fill="#FF00FF",width=2,tag="TB")

    for x in range(0,7,1):
        if banban[10][x]==1:
                canvas.create_line(x*40+5,10*40,x*40+5,10*40+39,fill="#FF00FF",width=2,tag="TB")
                canvas.create_line(x*40+44,10*40,x*40+44,10*40+39,fill="#FF00FF",width=2,tag="TB")
                canvas.create_line(x*40+5,10*40,x*40+44,10*40,fill="#FF00FF",width=2,tag="TB")
                canvas.create_line(x*40+5,10*40+39,x*40+44,10*40+39,fill="#FF00FF",width=2,tag="TB")
#駒が成れるかどうかチェック
def nari_check(FIG,cursor_x,cursor_y,px,py):
    if (FIG==1 or FIG==2 or FIG==3) and cursor_y==1:
        FIG=FIG+20
        return FIG
    elif FIG==3 and cursor_y==2 and py!=10:
        FIG=FIG+20
        return FIG
    elif 4<=FIG and FIG<=7 and 1<= cursor_y and cursor_y<=3 and FIG!=5 and py!=10 and (cursor_x!=px or cursor_y!=py):
        t=message_style()
        if t==True:
            FIG=FIG+20
            return FIG
        elif t==False:
            print("FIG="+str(FIG))
            return FIG
    elif (FIG==1 or FIG==2) and 2<= cursor_y and cursor_y<=3 and py!=10 and (cursor_x!=px or cursor_y!=py):
        t=message_style()
        if t==True:
            FIG=FIG+20
            return FIG
        elif t==False:
            return FIG
    elif FIG==3 and cursor_y==3 and (cursor_x!=px or cursor_y!=py):
        t=message_style()
        if t==True:
            FIG=FIG+20
            return FIG
        elif t==False:
            return FIG
    elif 4<=FIG and FIG<=7 and 1<=py and py<=3 and FIG!=5 and (cursor_x!=px or cursor_y!=py):
        t=message_style()
        if t==True:
            FIG=FIG+20
            return FIG
        elif t==False:
            return FIG

    else:
        return FIG
#GUIの盤を生成
def bg_banmen():
    for y in range(0,9,1):
        for x in range(0,9,1):
            canvas.create_rectangle(x*40+5,y*40+40,x*40+45,y*40+80,outline="#000000")
#駒の画像表示
def banmen():
    global osero_ban
    
    for y in range(1,10,1):
        for x in range(1,10,1):
            koma(x,y,1,hu)
            koma(x,y,2,kyo)
            koma(x,y,3,kei)
            koma(x,y,4,gin)
            koma(x,y,5,kin)
            koma(x,y,6,kaku)
            koma(x,y,7,hisha)
            koma(x,y,8,ou)
            koma(x,y,11,enehu)
            koma(x,y,12,enekyo)
            koma(x,y,13,enekei)
            koma(x,y,14,enegin)
            koma(x,y,15,enekin)
            koma(x,y,16,enekaku)
            koma(x,y,17,enehisha)
            koma(x,y,18,enegyoku)
            koma(x,y,21,hunari)
            koma(x,y,22,kyonari)
            koma(x,y,23,keinari)
            koma(x,y,24,ginnari)
            koma(x,y,26,kakunari)
            koma(x,y,27,hishanari)
            koma(x,y,31,enehunari)
            koma(x,y,32,enekyonari)
            koma(x,y,33,enekeinari)
            koma(x,y,34,eneginnari)
            koma(x,y,36,enekakunari)
            koma(x,y,37,enehishanari)
#ゲームのメインとなる関数
def game_main():
    global osero_ban,bring2_ban
    global cursor_x,cursor_y,mouse_c
    global k,r
    global ai_filex
    global fig,px,py,sign
    
    cursor_x=int((mouse_x-5)/40)+1
    cursor_y=int((mouse_y)/40)
    canvas.delete("TT")
    canvas.create_oval(cursor_x*40-25,cursor_y*40+10,cursor_x*40-5,cursor_y*40+30,outline="#CCFF00",fill="#CCFF00",tag="TT")
    canvas.create_image(350,420,image=icon,tag="TT")
    if mouse_c==1 and sign==0 and fig==0 and 5 <= mouse_x and mouse_x <=455 and 0 <= mouse_y and mouse_y <= 439:
        player(cursor_x,cursor_y)
        player_posi()
        if 1 <= cursor_y and cursor_y<=9:
            if osero_ban[cursor_y][cursor_x]!=0 and judge(cursor_x,cursor_y):
                fig=osero_ban[cursor_y][cursor_x]
                osero_ban[cursor_y][cursor_x]=0
                px=cursor_x
                py=cursor_y
                sign=1

        elif cursor_y==10:
            if bring2_ban[1][cursor_x-1]!=0:
                fig=bring_ban[1][cursor_x-1]
                bring2_ban[1][cursor_x-1]-=1
                px=cursor_x
                py=cursor_y
                sign=1

    elif mouse_c==1 and sign==0 and 5 <= mouse_x and mouse_x <=455 and 0 <= mouse_y and mouse_y <= 439:
        if fig!=0 and banban[cursor_y][cursor_x]==1:
            canvas.delete("TB")
            
            sign=1
            if (11 <= osero_ban[cursor_y][cursor_x] and osero_ban[cursor_y][cursor_x] <= 17):
                bring2_ban[1][osero_ban[cursor_y][cursor_x]-11]+=1
                osero_ban[cursor_y][cursor_x]=nari_check(fig,cursor_x,cursor_y,px,py)
                fig=0
                ban_clear()
                if cursor_x!=px or cursor_y!=py:
                    judge_te(ban_hyoukati_player())
            
            elif osero_ban[cursor_y][cursor_x]==18:
                tkinter.messagebox.showinfo("勝ち","あなたの勝ちです")
                mouse_c=2
            elif (31 <= osero_ban[cursor_y][cursor_x] and osero_ban[cursor_y][cursor_x] <= 37):
                bring2_ban[1][osero_ban[cursor_y][cursor_x]-31]+=1
                osero_ban[cursor_y][cursor_x]=nari_check(fig,cursor_x,cursor_y,px,py)
                fig=0
                ban_clear()
                if cursor_x!=px or cursor_y!=py:
                    judge_te(ban_hyoukati_player())
                
            else:
                osero_ban[cursor_y][cursor_x]=nari_check(fig,cursor_x,cursor_y,px,py)
                fig=0
                ban_clear()
                if cursor_x!=px or cursor_y!=py:
                    judge_te(ban_hyoukati_player())
        elif fig!=0 and py==10:
            canvas.delete("TB")
            sign=1
            bring2_ban[1][px-1]+=1
            fig=0
            ban_clear()

    elif mouse_c==0:
        sign=0

    if mouse_c==2:
        root.after_cancel(k)


    banmen() 
    bring_koma()
    
    k=root.after(50,game_main)


root = tkinter.Tk()
root.title("将棋")
root.resizable(False,False)
canvas=tkinter.Canvas(root,width=365,height=435,bg="skyblue")
canvas.pack()
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
root.bind("<ButtonRelease>",mouse_release)

hu=tkinter.PhotoImage(file="hu.png")
hunari=tkinter.PhotoImage(file="hunari.png")
kyo=tkinter.PhotoImage(file="kyo.png")
kyonari=tkinter.PhotoImage(file="kyonari.png")
kei=tkinter.PhotoImage(file="kei.png")
keinari=tkinter.PhotoImage(file="keinari.png")
gin=tkinter.PhotoImage(file="gin.png")
ginnari=tkinter.PhotoImage(file="ginnari.png")
kin=tkinter.PhotoImage(file="kin.png")
ou=tkinter.PhotoImage(file="ou.png")
kaku=tkinter.PhotoImage(file="kaku.png")
kakunari=tkinter.PhotoImage(file="kakunari.png")
hisha=tkinter.PhotoImage(file="hisha.png")
hishanari=tkinter.PhotoImage(file="hishanari.png")
enehu=tkinter.PhotoImage(file="enehu.png")
enehunari=tkinter.PhotoImage(file="enehunari.png")
enekyo=tkinter.PhotoImage(file="enekyo.png")
enekyonari=tkinter.PhotoImage(file="enekyonari.png")
enekei=tkinter.PhotoImage(file="enekei.png")
enekeinari=tkinter.PhotoImage(file="enekeinari.png")
enegin=tkinter.PhotoImage(file="enegin.png")
eneginnari=tkinter.PhotoImage(file="eneginnari.png")
enekin=tkinter.PhotoImage(file="enekin.png")
enegyoku=tkinter.PhotoImage(file="enegyoku.png")
enekaku=tkinter.PhotoImage(file="enekaku.png")
enekakunari=tkinter.PhotoImage(file="enekakunari.png")
enehisha=tkinter.PhotoImage(file="enehisha.png")
enehishanari=tkinter.PhotoImage(file="enehishanari.png")
ban=tkinter.PhotoImage(file="ban.png")

icon=tkinter.PhotoImage(file="amongus.png")
icon = icon.subsample(9)
osero_ban=[[20,20,20,20,20,20,20,20,20,20,20],
           [20,12,13,14,15,18,15,14,13,12,20],#1
           [20,0,17,0,0,0,0,0,16,0,20],
           [20,11,11,11,11,11,11,11,11,11,20],
           [20,0,0,0,0,0,0,0,0,0,20],#4
           [20,0,0,0,0,0,0,0,0,0,20],
           [20,0,0,0,0,0,0,0,0,0,20],
           [20,1,1,1,1,1,1,1,1,1,20],
           [20,0,6,0,0,0,0,0,7,0,20],#8
           [20,2,3,4,5,8,5,4,3,2,20],
           [20,20,20,20,20,20,20,20,20,20,20]]

bring_ban=[
    [11,12,13,14,15,16,17],
    [1,2,3,4,5,6,7],
    ]
bring2_ban=[
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]
bg_ban=[[0,0,0,0,0,0,0,0,0],#1
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],#4
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],#8
        [0,0,0,0,0,0,0,0,0]]

banban=[[20,20,20,20,20,20,20,20,20,20,20],
           [20,0,0,0,0,0,0,0,0,0,20],#1
           [20,0,0,0,0,0,0,0,0,0,20],
           [20,0,0,0,0,0,0,0,0,0,20],
           [20,0,0,0,0,0,0,0,0,0,20],#4
           [20,0,0,0,0,0,0,0,0,0,20],
           [20,0,0,0,0,0,0,0,0,0,20],
           [20,0,0,0,0,0,0,0,0,0,20],
           [20,0,0,0,0,0,0,0,0,0,20],#8
           [20,0,0,0,0,0,0,0,0,0,20],
           [0,0,0,0,0,0,0,20,20,20,20]]

bg_banmen()
game_main()

root.mainloop()