import pygame
import sys
import random


WHITE = (255,255,255)

BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PURPLE = (255,0,255)
ORANGE = (255,128,0)
AQUA = (0,255,255)
BACKGROUND = (200,200,200)

BOARDHEIGHT = 12
BOARDWIDHT = 6
S = 40
S2 = 20
page = 0

class Posi():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Puyo():
    def __init__(self,x,y,rot,color):
        self.x = x
        self.y = y
        self.rot = rot
        self.color = color
    
    def make_puyo(self):
        puyo = [Posi(0,0),Posi(0,-1)]

        for t in range((40000000+self.rot)%4):
            puyo = list(map(Puyo.rot_puyo,puyo))

        return puyo,self.color
    def rot_puyo(self):
        puyo = Posi(-self.y,self.x)

        return puyo
    
    def copy(self):
        return Puyo(self.x,self.y,self.rot,self.color)

    def draw(self,screen):
        block,color = self.make_puyo()

        for b,c in zip(block,color):
            if c == 2:
                pygame.draw.circle(screen,RED,[(self.x+b.x)*S+S2,(self.y+b.y)*S+S2],18)
            elif c == 3:
                pygame.draw.circle(screen,BLUE,[(self.x+b.x)*S+S2,(self.y+b.y)*S+S2],18)
            elif c == 4:
                pygame.draw.circle(screen,GREEN,[(self.x+b.x)*S+S2,(self.y+b.y)*S+S2],18)
            elif c == 5:
                pygame.draw.circle(screen,YELLOW,[(self.x+b.x)*S+S2,(self.y+b.y)*S+S2],18)
            elif c == 6:
                pygame.draw.circle(screen,PURPLE,[(self.x+b.x)*S+S2,(self.y+b.y)*S+S2],18)

class Field():
    def __init__(self):
        self.board = self.make_board()
        self.del_puyo=0
        self.delpuyo_color=0
    def make_board(self):
        make_board = []
        for t in range(BOARDHEIGHT):
            make_board.append([1,0,0,0,0,0,0,1])
        make_board.append([1,1,1,1,1,1,1,1])
        
        return make_board
    
    def delet_puyo(self):
        for y in range(BOARDHEIGHT):
            for x in range(1,BOARDWIDHT+1):
                if self.board[y][x] != 0:
                    self.delpuyo_color = self.board[y][x]
                    field=Field()
                    self.explore_puyo(x,y,field)
                    if self.del_puyo >= 4:
                        for y in range(BOARDHEIGHT):
                            for x in range(1,BOARDWIDHT+1):
                                if field.board[y][x] == self.delpuyo_color:
                                    self.board[y][x] = 0

                        for y in range(BOARDHEIGHT-1,-1,-1):
                            for x in range(1,BOARDWIDHT+1):
                                t = 1
                                if self.board[y][x] != 0:
                                    while True:
                                        if self.board[y+t][x] == 0:
                                            self.board[y+t][x] = self.board[y+t-1][x]
                                            self.board[y+t-1][x] = 0
                                            t += 1
                                        else:
                                            break

                                
                                    
                    self.del_puyo = 0
                    
    
    def explore_puyo(self,x,y,field):
        if self.board[y][x] != 1 and self.board[y][x] == self.delpuyo_color:
            self.del_puyo += 1
            field.board[y][x] += self.delpuyo_color
            if field.board[y-1][x] == 0:
                self.explore_puyo(x,y-1,field)
            if field.board[y+1][x] == 0:
                self.explore_puyo(x,y+1,field)
            if field.board[y][x-1] == 0:
                self.explore_puyo(x-1,y,field)
            if field.board[y][x+1] == 0:
                self.explore_puyo(x+1,y,field)
        
        
        
    def draw(self,screen):
        for y in range(BOARDHEIGHT + 1):
            for x in range(BOARDWIDHT + 2):
                if self.board[y][x] == 0:
                    pygame.draw.rect(screen,WHITE,[x*S,y*S,S,S],1)
                elif self.board[y][x] == 1:
                    pygame.draw.rect(screen,BLACK,[x*S,y*S,S,S])
                elif self.board[y][x] == 2:
                    pygame.draw.circle(screen,RED,[x*S+S2,y*S+S2],18)
                    pygame.draw.rect(screen,WHITE,[x*S,y*S,S,S],1)
                elif self.board[y][x] == 3:
                    pygame.draw.circle(screen,BLUE,[x*S+S2,y*S+S2],18)
                    pygame.draw.rect(screen,WHITE,[x*S,y*S,S,S],1)
                elif self.board[y][x] == 4:
                    pygame.draw.circle(screen,GREEN,[x*S+S2,y*S+S2],18)
                    pygame.draw.rect(screen,WHITE,[x*S,y*S,S,S],1)
                elif self.board[y][x] == 5:
                    pygame.draw.circle(screen,YELLOW,[x*S+S2,y*S+S2],18)
                    pygame.draw.rect(screen,WHITE,[x*S,y*S,S,S],1)
                elif self.board[y][x] == 6:
                    pygame.draw.circle(screen,PURPLE,[x*S+S2,y*S+S2],18)
                    pygame.draw.rect(screen,WHITE,[x*S,y*S,S,S],1)

    def score_draw(self,screen,score):
        font2=pygame.font.Font(None,30)
        txt = font2.render("SCORE : "+str(score),True,BLACK)
        screen.blit(txt,[320,500])
class Game():
    def __init__(self):
        self.field = Field()
        self.puyo=Puyo(3,1,0,[random.randint(2,6),random.randint(2,6)])
        self.movex=0
        self.movey=0
        self.mover=0
        self.count=0
    def proc(self,screen,tmr):
        global page

        if self.movex != 0:
            move = self.puyo.copy()
            move.x += self.movex
            if self.rangecheck(move) == True:
                self.puyo.x += self.movex


            self.movex = 0

        if self.movey != 0:
            move = self.puyo.copy()
            move.y += self.movey
            if self.rangecheck(move) == True:
                self.puyo.y += self.movey
            else:
                puyo,color = Puyo.make_puyo(move)
                cnt = 0
                for b in puyo:
                    if self.field.board[b.y+self.puyo.y+1][b.x+self.puyo.x] != 0:
                        self.field.board[b.y+self.puyo.y][b.x+self.puyo.x] = color[cnt]
                    
                    elif self.field.board[b.y+self.puyo.y+2][b.x+self.puyo.x] != 0 and self.puyo.rot%4 == 2:
                        self.field.board[b.y+self.puyo.y][b.x+self.puyo.x] = color[cnt]
                        
                    else:
                        t=1
                        while True:
                            if self.field.board[b.y+self.puyo.y+t][b.x+self.puyo.x] == 0:
                                t += 1
                            else:
                                self.field.board[b.y+self.puyo.y+t-1][b.x+self.puyo.x] = color[cnt]
                                break
                    cnt += 1
                for t in range(19):
                    self.field.delet_puyo()
                self.puyo = Puyo(3,0,0,[random.randint(2,6),random.randint(2,6)])

            self.movey = 0

        if self.mover != 0:
            move = self.puyo.copy()
            move.rot += self.mover
            if self.rangecheck(move) == True:
                self.puyo.rot += self.mover
        
            self.mover = 0


        

        screen.fill(BACKGROUND)
        self.field.draw(screen)
        self.field.score_draw(screen,self.count*1000)
        self.puyo.draw(screen)

    def rangecheck(self,move):
        block,color = Puyo.make_puyo(move)
        for b in block:
            if self.field.board[b.y+move.y][b.x+move.x] != 0:
                return False
        return True

def main():
    global page
    pygame.init()
    pygame.display.set_caption("puyopuyo")

    screen=pygame.display.set_mode((600,525))
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,50)
    font2=pygame.font.Font(None,30)
    game=Game()

    tmr = 0
    while True:
        tmr += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game.mover += 1
                if event.key == pygame.K_d:
                    game.mover -= 1
                # if event.key == pygame.K_UP:
                #     game.minoQick += 1
                #     tmr = 0

        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT] == 1 and tmr%3 == 0:
            game.movex += -1
        if key[pygame.K_RIGHT] == 1 and tmr%3 == 0:
            game.movex += 1
        if key[pygame.K_DOWN] == 1 and tmr%3 == 0:
            game.movey += 1
        elif tmr%50 == 0:
            game.movey += 1
  
        if page == 0:
            screen.fill(WHITE)
            txt = font2.render("GAMESTART[SPACE]",True,BLACK)
            screen.blit(txt,[125,200])
            key=pygame.key.get_pressed()
            if key[pygame.K_SPACE] == 1:
                page=1
        elif page == 1:
            game.proc(screen,tmr)
        elif page == 2:
            screen.fill(WHITE)
            txt = font.render("GAMEOVER",True,BLACK)
            screen.blit(txt,[30,150])
    


        pygame.display.update()
        clock.tick(50)      
    


if __name__ == "__main__":
    main()
