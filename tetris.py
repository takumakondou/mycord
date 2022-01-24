import pygame
import sys
import random


WHITE=(255,255,255)
WHITE2=(50,50,50)
BLACK=(0,0,0)
GLAY=(80,80,80)
PURPLE=(255,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,128,0)
AQUA=(0,255,255)

page=0

class Block():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def draw(self,screen,tile):
        s=15
        if tile[self.y][self.x]==0:
            pygame.draw.rect(screen,GLAY,[self.x*s,self.y*s,s,s])
            
        if tile[self.y][self.x]==1:
            pygame.draw.rect(screen,BLACK,[self.x*s,self.y*s,s,s])
            pygame.draw.rect(screen,WHITE2,[self.x*s,self.y*s,s,s],1)
        
        if tile[self.y][self.x]==2:
            pygame.draw.rect(screen,BLACK,[self.x*s,self.y*s,s,s])
            pygame.draw.rect(screen,GLAY,[self.x*s,self.y*s,s,s],1)


class Mino():
    def __init__(self,x,y,rot,shape):
        self.x=x
        self.y=y
        self.rot=rot
        self.shape=shape
        self.color=BLACK
    
    def rot_cal(self):
        b=Block(-self.y,self.x)
        return b

    def calcBlocks(self):
        if self.shape==1:
            blocks=[Block(-1,0),Block(0,0),Block(1,0),Block(0,-1)]#Tmino
        if self.shape==2:
            blocks=[Block(0,0),Block(0,-1),Block(0,1),Block(0,2)]#Imino
        if self.shape==3:
            blocks=[Block(1,0),Block(0,0),Block(1,1),Block(0,1)]#Omino
        if self.shape==4:
            blocks=[Block(-1,0),Block(0,0),Block(1,0),Block(1,-1)]#Lmino
        if self.shape==5:
            blocks=[Block(-1,-1),Block(-1,0),Block(0,0),Block(1,0)]#Jmino
        if self.shape==6:
            blocks=[Block(-1,0),Block(0,0),Block(0,1),Block(1,1)]#Smino
        if self.shape==7:
            blocks=[Block(-1,1),Block(0,1),Block(0,0),Block(1,0)]#Zmino

        if self.shape!=3:#Ominoの回転は不要。
            for r in range((400000000+self.rot)%4):
                blocks=list(map(Mino.rot_cal,blocks))

        return blocks
    def draw(self,screen):
        s=15
        for b in Mino.calcBlocks(self):
            pygame.draw.rect(screen,self.color,[(self.x+b.x)*s,(self.y+b.y)*s,s,s])
            pygame.draw.rect(screen,WHITE2,[(self.x+b.x)*s,(self.y+b.y)*s,s,s],1)

    def draw2(self,screen):
        s=15
        for b in Mino.calcBlocks(self):
            pygame.draw.rect(screen,WHITE,[(self.x+b.x)*s,(self.y+b.y)*s,s,s])
            pygame.draw.rect(screen,WHITE2,[(self.x+b.x)*s,(self.y+b.y)*s,s,s],1)
    
    def copy(self):
        return Mino(self.x,self.y,self.rot,self.shape)
            

class Field():
    def __init__(self):
        self.tile=[
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],#3
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],#6
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],#9
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],#12
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],#16
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,0,0,0,0,2],#20
            [2,2,2,2,2,2,2,2,2,2,2,2]
        ]
    def draw(self,screen):
        for y in range(21):
            for x in range(12):
                
                block=Block(x,y)
                block.draw(screen,self.tile)

    
    def putblock(self,x,y):
        for b in Mino.calcBlocks(self.mino):
            
            self.field.tile[b.y+y][b.x+x]=1

    
    def findline(self):
        for y in range(20):               
            if self.tile[y][1:12].count(1)==10:

                return y
            else:
                continue
        y=-1
        return y
    def deleteline(self,y):
        if y!=-1:
            self.tile.pop(y)
            self.tile.insert(0,[2,0,0,0,0,0,0,0,0,0,0,2]
            )
        
    def copy(self):
        return self.tile

            

class Game():
    def __init__(self):
        self.next=Next()
        self.mino=self.makemino()
        self.minoVx=0 
        self.minoVy=0
        self.minoVr=0
        self.minoQick=0
        self.field=Field()
        
    
    def makemino(self):
        r=self.next.nextmino()
        return Mino(5,0,0,r)
    def move_check(self,mino,field):
        blocks=Mino.calcBlocks(mino)
        for b in blocks:
            if 1<=b.x+mino.x and b.x+mino.x<=10 and 0<=b.y+mino.y and b.y+mino.y<=20:
                if field[b.y+mino.y][b.x+mino.x]==0:
                    continue
                else:
                    return False
            else:
                return False
        return True

        

        
    def proc(self,screen,tmr):
        global page
        if self.minoVx!=0:
            af_move=self.mino.copy()
            af_move.x+=self.minoVx
            
            if Game.move_check(self,af_move,self.field.tile)==True:
                self.mino.x+=self.minoVx
            else:
                af_move.x-=self.minoVx
            self.minoVx=0
        if self.minoVy!=0:
            af_move=self.mino.copy()
            af_move.y+=self.minoVy
            if Game.move_check(self,af_move,self.field.tile)==True:
                self.mino.y+=self.minoVy
            else:
                af_move.y-=self.minoVy
            self.minoVy=0

        if self.minoQick!=0:
            while True:
                af_move=self.mino.copy()
                af_move.y+=1
                if Game.move_check(self,af_move,self.field.tile)==True:
                    self.mino.y+=1
                else:
                    af_move.y-=1
                    self.minoQick=0
                    break


        if self.minoVr!=0:
            af_move=self.mino.copy()
            af_move.rot+=self.minoVr
            if Game.move_check(self,af_move,self.field.tile)==True:
                self.mino.rot+=self.minoVr
            else:
                af_move.rot-=self.minoVr
            self.minoVr=0

        if tmr%30==0:
            af_move=self.mino.copy()
            af_move.y+=1
            if Game.move_check(self,af_move,self.field.tile)==True:
                self.mino.y+=1
            else:
                Field.putblock(self,self.mino.x,self.mino.y)
                if 1 in self.field.tile[0][:]:
                    page=2
                else:
                    for t in range(4): 
                        y=Field.findline(self.field)
                        Field.deleteline(self.field,y)
                    r=self.next.nextmino()
                    self.mino=Mino(5,0,0,r)
                    
                    

        screen.fill(GLAY)
        self.next.draw(screen)
        self.field.draw(screen)
        self.mino.draw(screen)
        copytile=self.field.copy()
        copymino=self.mino.copy()
        

class Next():
    def __init__(self):
        self.r=[1,2,3,4,5,6,7]
        self.next=[1]
        self.color=1
        #random.shuffle(self.next)
        self.minoCount=[]
    def nextmino(self):
        while True:
            r=random.choice(self.r)
            if r in self.minoCount:
                continue
            else:
                
                self.next.append(r)
                self.minoCount.append(r)
                near_next=self.next[0]
                self.next.pop(0)
                if len(self.minoCount)==7:
                    self.minoCount=[]
                return near_next

    def shuffle(self,r):
        return random.shuffle(r)
   

    def draw(self,screen):
        s=15
        for num,next in enumerate(self.next):
            mino=Mino(0,0,0,next)
            for b in mino.calcBlocks():
                pygame.draw.rect(screen,BLACK,[200+(+mino.x+b.x)*s,50*num+(25+(mino.y+b.y)*s),s,s])
                pygame.draw.rect(screen,WHITE2,[200+(+mino.x+b.x)*s,50*num+(25+(mino.y+b.y)*s),s,s],1)
                



def main():
    global page
    pygame.init()
    pygame.display.set_caption("tetris")

    screen=pygame.display.set_mode((280,315))
    screen.fill(GLAY)
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,50)
    font2=pygame.font.Font(None,30)
    game=Game()
    #game.next.minoCount.append(r)
    #game.next.next.insert(0,r)
    #game.next.next.pop(0)
    tmr=0
    while True:
        tmr+=1

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    game.minoVr+=1
                if event.key==pygame.K_d:
                    game.minoVr-=1
                if event.key==pygame.K_UP:
                    game.minoQick+=1
                    tmr=0
                if event.key==pygame.K_SPACE:
                    page=1
            
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]==1 and tmr%3==0:
            game.minoVx=-1
        if key[pygame.K_RIGHT]==1 and tmr%3==0:
            game.minoVx=1
        if key[pygame.K_DOWN]==1 and tmr%3==0:
            game.minoVy=1
  
        if page==0:
            screen.fill(WHITE)
            txt=font2.render("GAMESTART[SPACE]",True,BLACK)
            screen.blit(txt,[30,150])
        elif page==1:
            game.proc(screen,tmr)
        elif page==2:
            screen.fill(WHITE)
            txt=font.render("GAMEOVER",True,BLACK)
            screen.blit(txt,[30,150])
    


        pygame.display.update()
        clock.tick(50)      

def sub():
    global page
    pygame.init()
    pygame.display.set_caption("tetris")

    screen=pygame.display.set_mode((280,315))
    screen.fill(GLAY)
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,50)
    font2=pygame.font.Font(None,30)
    game=Game()
    tmr=0
    while True:
        tmr+=1

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    page=1

        if page==0:
            screen.fill(WHITE)
            txt=font2.render("GAMESTART[SPACE]",True,BLACK)
            screen.blit(txt,[30,150])
        elif page==1:
            game.proc(screen,tmr)
        elif page==2:
            screen.fill(WHITE)
            txt=font.render("GAMEOVER",True,BLACK)
            screen.blit(txt,[30,150])
    


        pygame.display.update()
        clock.tick(50)


if __name__=="__main__":
    main()
