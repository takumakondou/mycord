import tkinter
import random
import numpy as np
box=[None,0,0,0,0,0,0,0]
n=1
m=1
k=1
g=1
f=1
h=1
t=0
step=0
def banmen():
    global puyo_ban
    for y in range(1,22,1):
        for x in range(12):
            if puyo_ban[y][x] == 10:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="#505050",outline="#808080")

            elif puyo_ban[y][x] == 0:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="white",outline="#DDDDDD")
            
            elif puyo_ban[y][x] == 1:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="skyblue",outline="#DDDDDD")
            
            elif puyo_ban[y][x] == 2:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="#ff8000",outline="#DDDDDD")

            elif puyo_ban[y][x] == 3:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="#0000ff",outline="#DDDDDD")
            
            elif puyo_ban[y][x] == 4:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="#DDDD00",outline="#DDDDDD")

            elif puyo_ban[y][x] == 5:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="#ff00ff",outline="#DDDDDD")

            elif puyo_ban[y][x] == 6:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="#ff0000",outline="#DDDDDD")

            elif puyo_ban[y][x] == 7:
                canvas.create_rectangle(x*25,y*25-25,x*25+25,y*25+25-25,fill="#00ff00",outline="#DDDDDD")

def puyo_mino():
    global Ux,Uy,Dx,Dy,Rx,Ry,Lx,Ly
    global a
    if a == 1:
        Ux,Uy=5,0
        Dx,Dy=5,1
        Rx,Ry=5,2
        Lx,Ly=5,3

    if a == 2:
        Ux,Uy=6,0
        Dx,Dy=6,1
        Rx,Ry=5,1
        Lx,Ly=4,1

    if a == 3:
        Ux,Uy=4,0
        Dx,Dy=4,1
        Rx,Ry=5,1
        Lx,Ly=6,1

    if a == 4:
        Ux,Uy=5,0
        Dx,Dy=6,0
        Rx,Ry=5,1
        Lx,Ly=6,1

    if a == 5:
        Ux,Uy=5,0
        Dx,Dy=5,1
        Rx,Ry=4,1
        Lx,Ly=6,1

    if a == 6:
        Ux,Uy=5,0
        Dx,Dy=6,0
        Rx,Ry=6,1
        Lx,Ly=7,1

    if a == 7:
        Ux,Uy=5,0
        Dx,Dy=6,0
        Rx,Ry=5,1
        Lx,Ly=4,1

def puyo_drop():
    global canvas,a,puyo_ban
    global Ux,Uy,Dx,Dy,Rx,Ry,Lx,Ly
    if a == 1:
        #Ｉミノ
        canvas.create_rectangle(Ux*25,Uy*25-25,Ux*25+25,Uy*25+25-25,
        fill="skyblue",outline="skyblue",tag="PAINT")
        canvas.create_rectangle(Dx*25,Dy*25-25,Dx*25+25,Dy*25+25-25,
        fill="skyblue",outline="skyblue",tag="PAINT")
        canvas.create_rectangle(Lx*25,Ly*25-25,Lx*25+25,Ly*25+25-25,
        fill="skyblue",outline="skyblue",tag="PAINT")
        canvas.create_rectangle(Rx*25,Ry*25-25,Rx*25+25,Ry*25+25-25,
        fill="skyblue",outline="skyblue",tag="PAINT")

    elif a == 2:
        #Ｌミノ
        canvas.create_rectangle(Ux*25,Uy*25-25,Ux*25+25,Uy*25+25-25,
        fill="#ff8000",outline="#ff8000",tag="PAINT")
        canvas.create_rectangle(Dx*25,Dy*25-25,Dx*25+25,Dy*25+25-25,
        fill="#ff8000",outline="#ff8000",tag="PAINT")
        canvas.create_rectangle(Lx*25,Ly*25-25,Lx*25+25,Ly*25+25-25,
        fill="#ff8000",outline="#ff8000",tag="PAINT")
        canvas.create_rectangle(Rx*25,Ry*25-25,Rx*25+25,Ry*25+25-25,
        fill="#ff8000",outline="#ff8000",tag="PAINT")
    elif a == 3:
        #Jミノ
        
        canvas.create_rectangle(Ux*25,Uy*25-25,Ux*25+25,Uy*25+25-25,
        fill="#0000ff",outline="#0000ff",tag="PAINT")
        canvas.create_rectangle(Dx*25,Dy*25-25,Dx*25+25,Dy*25+25-25,
        fill="#0000ff",outline="#0000ff",tag="PAINT")
        canvas.create_rectangle(Lx*25,Ly*25-25,Lx*25+25,Ly*25+25-25,
        fill="#0000ff",outline="#0000ff",tag="PAINT")
        canvas.create_rectangle(Rx*25,Ry*25-25,Rx*25+25,Ry*25+25-25,
        fill="#0000ff",outline="#0000ff",tag="PAINT")
    elif a == 4:
        #Ｏミノ
        
        canvas.create_rectangle(Ux*25,Uy*25-25,Ux*25+25,Uy*25+25-25,
        fill="#DDDD00",outline="#DDDD00",tag="PAINT")
        canvas.create_rectangle(Dx*25,Dy*25-25,Dx*25+25,Dy*25+25-25,
        fill="#DDDD00",outline="#DDDD00",tag="PAINT")
        canvas.create_rectangle(Lx*25,Ly*25-25,Lx*25+25,Ly*25+25-25,
        fill="#DDDD00",outline="#DDDD00",tag="PAINT")
        canvas.create_rectangle(Rx*25,Ry*25-25,Rx*25+25,Ry*25+25-25,
        fill="#DDDD00",outline="#DDDD00",tag="PAINT")
    elif a == 5:
        #Ｔミノ
        
        canvas.create_rectangle(Ux*25,Uy*25-25,Ux*25+25,Uy*25+25-25,
        fill="#ff00ff",outline="#ff00ff",tag="PAINT")
        canvas.create_rectangle(Dx*25,Dy*25-25,Dx*25+25,Dy*25+25-25,
        fill="#ff00ff",outline="#ff00ff",tag="PAINT")
        canvas.create_rectangle(Lx*25,Ly*25-25,Lx*25+25,Ly*25+25-25,
        fill="#ff00ff",outline="#ff00ff",tag="PAINT")
        canvas.create_rectangle(Rx*25,Ry*25-25,Rx*25+25,Ry*25+25-25,
        fill="#ff00ff",outline="#ff00ff",tag="PAINT")
    elif a == 6:
        #Zミノ
        
        canvas.create_rectangle(Ux*25,Uy*25-25,Ux*25+25,Uy*25+25-25,
        fill="#ff0000",outline="#ff0000",tag="PAINT")
        canvas.create_rectangle(Dx*25,Dy*25-25,Dx*25+25,Dy*25+25-25,
        fill="#ff0000",outline="#ff0000",tag="PAINT")
        canvas.create_rectangle(Lx*25,Ly*25-25,Lx*25+25,Ly*25+25-25,
        fill="#ff0000",outline="#ff0000",tag="PAINT")
        canvas.create_rectangle(Rx*25,Ry*25-25,Rx*25+25,Ry*25+25-25,
        fill="#ff0000",outline="#ff0000",tag="PAINT")
    elif a == 7:
        #Sミノ
        
        canvas.create_rectangle(Ux*25,Uy*25-25,Ux*25+25,Uy*25+25-25,
        fill="#00ff00",outline="#00ff00",tag="PAINT")
        canvas.create_rectangle(Dx*25,Dy*25-25,Dx*25+25,Dy*25+25-25,
        fill="#00ff00",outline="#00ff00",tag="PAINT")
        canvas.create_rectangle(Lx*25,Ly*25-25,Lx*25+25,Ly*25+25-25,
        fill="#00ff00",outline="#00ff00",tag="PAINT")
        canvas.create_rectangle(Rx*25,Ry*25-25,Rx*25+25,Ry*25+25-25,
        fill="#00ff00",outline="#00ff00",tag="PAINT")

    
def puyo_line():
    global puyo_ban
    for y in range(20,0,-1):
        if puyo_ban[y][1]!=0 and puyo_ban[y][2]!=0 and puyo_ban[y][3]!=0 and puyo_ban[y][4]!=0 and puyo_ban[y][5]!=0 and puyo_ban[y][6]!=0 and\
            puyo_ban[y][7]!=0 and puyo_ban[y][8]!=0 and puyo_ban[y][9]!=0 and puyo_ban[y][10]!=0:

                for s in range(y,0,-1):
                    for x in range(1,11,1):
                        puyo_ban[s][x]=0
                        puyo_ban[s][x]=puyo_ban[s-1][x]


def puyo_judge():

    r = random.randint(1,7)
    return r

def puyo_loop():
    global box
    while True:
        r=puyo_judge()
        if box[r]==0:
            box[r]=r
            if box[1]!=0 and box[2]!=0 and box[3]!=0 and box[4]!=0 and box[5]!=0 and box[6]!=0 and box[7]!=0:
                for s in range(1,8,1):
                    box[s]=0
            return r
     
def puyo_spinreset():
    global n,m,k,g,f,h
    n,m,k,g,f,h=1,1,1,1,1,1
    

key = ""
def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""

a = puyo_judge()

def main_proc():
    global Ux,Uy,Dx,Dy,Rx,Ry,Lx,Ly
    global a,step
    global puyo_ban,key
    global n,m,k,g,f,h,t
   
    if step==0 and key=="space":
        banmen()
        puyo_mino()
        box[a]=a
        step=2
    elif step==2:
        
        if a==1 and key=="z":
            if n%2==1 and puyo_ban[Uy+1][Ux+2]==0 and puyo_ban[Dy][Dx+1]==0 and puyo_ban[Ly-2][Lx-1]==0:
                Uy=Uy+1
                Ux=Ux+2
                Dx=Dx+1
                Ry=Ry-1
                Ly=Ly-2
                Lx=Lx-1

            elif n%2==0 and puyo_ban[Uy-1][Ux-2]==0 and puyo_ban[Dy][Dx-1]==0 and puyo_ban[Ly+2][Lx+1]==0:
                Uy=Uy-1
                Ux=Ux-2
                Dx=Dx-1
                Ry=Ry+1
                Ly=Ly+2
                Lx=Lx+1
            else:
                n=n-1
            n=n+1
        if a==2 and key=="z":
            if m%4==1 and puyo_ban[Uy+2][Ux]==0 and puyo_ban[Dy+1][Dx-1]==0 and puyo_ban[Ly-1][Lx+1]==0:
                Uy=Uy+2
                Dy=Dy+1
                Dx=Dx-1
                Ly=Ly-1
                Lx=Lx+1
            elif m%4==2 and puyo_ban[Uy][Ux-2]==0 and puyo_ban[Dy-1][Dx-1]==0 and puyo_ban[Ly+1][Lx+1]==0:
                Ux=Ux-2
                Dy=Dy-1
                Dx=Dx-1
                Ly=Ly+1
                Lx=Lx+1
            elif m%4==3 and puyo_ban[Uy-2][Ux]==0 and puyo_ban[Dy][Dx+1]==0 and puyo_ban[Ly+1][Lx-1]==0:
                Uy=Uy-2
                Dy=Dy-1
                Dx=Dx+1
                Ly=Ly+1
                Lx=Lx-1
            elif m%4==0 and puyo_ban[Uy][Ux+2]==0 and puyo_ban[Dy+1][Dx+1]==0 and puyo_ban[Ly-1][Lx-1]==0:
                Ux=Ux+2
                Dy=Dy+1
                Dx=Dx+1
                Ly=Ly-1
                Lx=Lx-1
            else:
                m=m-1
            m=m+1
        if a==3 and key=="z":
            if k%4==1 and puyo_ban[Uy][Ux+2]==0 and puyo_ban[Dy-1][Dx+1]==0 and puyo_ban[Ly+1][Lx-1]==0:
                Ux=Ux+2
                Dy=Dy-1
                Dx=Dx+1
                Ly=Ly+1
                Lx=Lx-1
            elif k%4==2 and puyo_ban[Uy+2][Ux]==0 and puyo_ban[Dy+1][Dx*1]==0 and puyo_ban[Ly-1][Lx-1]==0:
                Uy=Uy+2
                Dy=Dy+1
                Dx=Dx+1
                Ly=Ly-1
                Lx=Lx-1
            elif k%4==3 and puyo_ban[Uy-1][Ux-2]==0 and puyo_ban[Dy][Dx-1]==0 and puyo_ban[Ly+2][Lx+1]==0:
                Ux=Ux-2
                Dy=Dy+1
                Dx=Dx-1
                Ly=Ly-1
                Lx=Lx+1
            elif k%4==0 and puyo_ban[Uy-2][Ux]==0 and puyo_ban[Dy-1][Dx-1]==0 and puyo_ban[Ly+1][Lx+1]==0:
                Uy=Uy-2
                Dy=Dy-1
                Dx=Dx-1
                Ly=Ly+1
                Lx=Lx+1
            else:
                k=k-1
            k=k+1
        if a==5 and key=="z":
            if g%4==1 and puyo_ban[Uy+1][Ux+1]==0 and puyo_ban[Ry-1][Rx+1]==0 and puyo_ban[Ly+1][Lx-1]==0:
                Uy=Uy+1
                Ux=Ux+1
                Ry=Ry-1
                Rx=Rx+1
                Ly=Ly+1
                Lx=Lx-1
            elif g%4==2 and puyo_ban[Uy+1][Ux-1]==0 and puyo_ban[Ry+1][Rx+1]==0 and puyo_ban[Ly-1][Lx-1]==0:
                Uy=Uy+1
                Ux=Ux-1
                Ry=Ry+1
                Rx=Rx+1
                Ly=Ly-1
                Lx=Lx-1
            elif g%4==3 and puyo_ban[Uy-1][Ux-1]==0 and puyo_ban[Ry+1][Rx-1]==0 and puyo_ban[Ly-1][Lx+1]==0:
                Uy=Uy-1
                Ux=Ux-1
                Ry=Ry+1
                Rx=Rx-1
                Ly=Ly-1
                Lx=Lx+1
            elif g%4==0 and puyo_ban[Uy-1][Ux+1]==0 and puyo_ban[Ry][Rx-1]==0 and puyo_ban[Ly+1][Lx+1]==0:
                Uy=Uy-1
                Ux=Ux+1
                Ry=Ry-1
                Rx=Rx-1
                Ly=Ly+1
                Lx=Lx+1
            else:
                g=g-1
            g=g+1
        if a==6 and key=="z":
            if f%2==1 and puyo_ban[Uy][Ux+2]==0 and puyo_ban[Dy+1][Dx+1]==0 and puyo_ban[Ly+1][Lx-1]==0:
                Ux=Ux+2
                Dy=Dy+1
                Dx=Dx+1
                Ly=Ly+1
                Lx=Lx-1
            elif f%2==0 and puyo_ban[Uy][Ux-2]==0 and puyo_ban[Dy-1][Dx-1]==0 and puyo_ban[Ly-1][Lx+1]==0:
                Ux=Ux-2
                Dy=Dy-1
                Dx=Dx-1
                Ly=Ly-1
                Lx=Lx+1
            else:
                f=f-1
            f=f+1
        if a==7 and key=="z":
            if h%2==1 and puyo_ban[Uy+1][Ux+1]==0 and puyo_ban[Dy+2][Dx]==0 and puyo_ban[Ly-1][Lx+1]==0:
                Uy=Uy+1
                Ux=Ux+1
                Dy=Dy+2
                Ly=Ly-1
                Lx=Lx+1
            elif h%2==0 and puyo_ban[Uy-1][Ux-1]==0 and puyo_ban[Dy-2][Dx]==0 and puyo_ban[Ly+1][Lx-1]==0:
                Uy=Uy-1
                Ux=Ux-1
                Dy=Dy-2
                Ly=Ly+1
                Lx=Lx-1
            else:
                h=h-1
            h=h+1


        if key=="Down" and puyo_ban[Uy+1][Ux] == 0 and puyo_ban[Dy+1][Dx]==0 and puyo_ban[Ry+1][Rx]==0 and puyo_ban[Ly+1][Lx]==0:
            Uy = Uy + 1
            Dy = Dy + 1
            Ry = Ry + 1
            Ly = Ly + 1

            
        if key=="Left" and puyo_ban[Uy][Ux-1] == 0 and puyo_ban[Dy][Dx-1] == 0 and puyo_ban[Ry][Rx-1] == 0 and puyo_ban[Ly][Lx-1] == 0:
            Ux = Ux - 1
            Dx = Dx - 1
            Lx = Lx - 1
            Rx = Rx - 1

        if key=="Right" and puyo_ban[Uy][Ux+1] == 0 and puyo_ban[Dy][Dx+1] == 0 and puyo_ban[Ry][Rx+1] == 0 and puyo_ban[Ly][Lx+1] == 0:
            Ux = Ux + 1
            Dx = Dx + 1
            Lx = Lx + 1
            Rx = Rx + 1
        

        if key!="Down" and puyo_ban[Uy+1][Ux] == 0 and puyo_ban[Dy+1][Dx] == 0\
            and puyo_ban[Ry+1][Rx] == 0 and puyo_ban[Ly+1][Lx] == 0 and\
                puyo_ban[Uy+1][Ux] != 10 and puyo_ban[Dy+1][Dx]!=10\
            and puyo_ban[Ry+1][Rx]!=10 and puyo_ban[Ly+1][Lx]!=10 and t%100==0:
                Uy = Uy + 1
                Dy = Dy + 1
                Ry = Ry + 1
                Ly = Ly + 1
            
        if puyo_ban[Uy+1][Ux] == 10 or puyo_ban[Dy+1][Dx]==10 or\
            puyo_ban[Ry+1][Rx]==10 or puyo_ban[Ly+1][Lx]==10\
                or puyo_ban[Uy+1][Ux] != 0 or puyo_ban[Dy+1][Dx]!=0 or\
            puyo_ban[Ry+1][Rx]!=0 or puyo_ban[Ly+1][Lx]!=0:
            puyo_ban[Uy][Ux] = a
            puyo_ban[Dy][Dx] = a
            puyo_ban[Ly][Lx] = a
            puyo_ban[Ry][Rx] = a
            puyo_line()
            puyo_line()
            puyo_line()
            puyo_line()
            banmen()
            a=puyo_loop()
            puyo_mino()
            puyo_spinreset()
            

        canvas.delete("PAINT")
        puyo_drop()
        t=t+20
    root.after(100,main_proc) 

root = tkinter.Tk()
root.title("テトリス")
root.resizable(False,False)
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
canvas = tkinter.Canvas(root,width=300,height=525,bg="skyblue")
canvas.pack()

puyo_ban=[10,0,0,0,0,0,0,0,0,0,0,10]*21+[10,10,10,10,10,10,10,10,10,10,10,10]
puyo_ban=np.array(puyo_ban)
puyo_ban=puyo_ban.reshape((-1,12))


main_proc()
root.mainloop()