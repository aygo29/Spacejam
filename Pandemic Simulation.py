import pygame
import random,math
maxv=20
transmissionrate=0.6
mortality_rate = 0.03
recchance=0.65
class People():
    colour_code={"susceptible":"yellow","infected":"red","recovered":"green","dead":"black"}
    def __init__(self,x,y,category,sensible):
        self.x=x
        self.y=y
        self.category=category
        self.sensible=sensible
        self.xv=self.yv=0
        self.timesick=0
        self.radius=3.5
        self.rectime=random.randint(50,200)
        noconstraint=True
        if noconstraint:
            self.xv=random.uniform(-maxv,maxv)
            self.yv=random.uniform(-maxv,maxv)

    def move(self):
        self.x=self.x+self.xv
        self.y=self.y+self.yv
    def draw(self,screen):
        pygame.draw.circle(screen,pygame.Color(self.colour_code[self.category]),(round(self.x),round(self.y)),self.radius)
    def updation(self,screen,peoples):
        self.move()
        if self.category=="infected":
            self.timesick+=1
            if self.timesick==self.rectime and random.random()<=recchance:
                self.category="recovered"
        self.wallcollision(screen)
        for other in peoples:
            if self!=other:
                if self.mutualcoll(screen,other):
                    self.updatevel(screen,other)
                    if self.category=="infected" and other.category=="susceptible":
                        if random.random()<=transmissionrate:
                            other.category="infected"
                    if self.category=="susceptible" and other.category=="infected":
                        if random.random() <= transmissionrate:
                            self.category="infected"


    def wallcollision(self,screen):
        if self.x+self.radius>=screen.get_width() and self.xv>0:
            self.xv*=-1
        elif self.x-self.radius<=0 and self.xv<0:
            self.xv*=-1
        if self.y+self.radius>=screen.get_height() and self.yv>0:
            self.yv*=-1
        elif self.y-self.radius<=0 and self.yv<0:
            self.yv*=-1
    def mutualcoll(self,screen,other):
        distance=math.sqrt(pow(self.x-other.x,2)+pow(self.y-other.y,2))
        if distance<=(self.radius+other.radius):
            return True
        return False
    def updatevel(self,screen,other):
        if not (self.sensible) and not( other.sensible):
            tempx=self.xv
            tempy=self.yv
            self.xv=other.xv
            self.yv=other.yv
            other.xv=tempx
            other.yv=tempy
        elif other.sensible:
            self.xv*=-1
            self.yv*=-1







