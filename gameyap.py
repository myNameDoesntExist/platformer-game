import pygame, typing # type: ignore  # noqa: E401
pygame.init()
lists=typing.TypeVar('lists',list,tuple)
num=typing.TypeVar('num',int,float)

#i srsly dont konow how to code classes
#ow to use git efficiently vro 🥀💔

class Obj:
    def __init__(self,name:str) -> None:
        '''creates name for obj and puts it in a dictionary'''
        self.obj={}
        self.obj[name]=None
    def rect(self,initpos:lists,width:num,height:num,color:lists,name):
        '''uses name (bc its easier to code lmao), it MUST match the name you used when initiating the object'''
        holder=pygame.Rect((width,height),initpos)
        holder.center=initpos
        holderreal=[color,holder]
        if name:
            if name in self.obj:
                self.obj[name]=holderreal
            else:
                raise AttributeError("nuh uh, did it match yet?")
    class circle:
        def __init__(center:lists,radius:num,color) -> None:

            pass

class Gravity:
    objects={}
    objecttypes={}
    def __init__(self,gravity:num=9.81)->None:
        '''gravity is acceleration speed added to object every second in pixels. default is 9.81 lmao'''
        self.gravity=gravity
    class Body:
        DYNAMIC:int=1
        STATIC:int=2
        KINETIC:int=3
        def add(self,*args:pygame.Rect,objtype:int=DYNAMIC)->None:
            '''adds gravity to object, pygame.Rect type only'''
            #self.objects[]=args    ill figure later

scr=pygame.display.set_mode([960, 720])
run=1
#test=Obj('ok')
#test=Obj.rect()
#cirtest=pygame.draw.circle(scr,[0,0,255],(100,100),25) #does not yield rect as circle
#print(test,test[1].center,cirtest)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=0
    scr.fill([255,255,255])
#    pygame.draw.rect(scr,*test) #lmao
#    pygame.draw.rect(scr,[0,0,255],[100,100,1,1]) #pixel at 100,100
#    pygame.draw.rect(scr,[0,0,200],cirtest) #rect generated by pygame.draw.circle
    pygame.draw.circle(scr,[0,0,253.4],(100,100),25) #actual cirtest
    pygame.display.flip()