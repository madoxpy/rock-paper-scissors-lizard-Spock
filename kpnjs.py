from pygame import *
import numpy as np
from time import sleep

black=(0,0,0)
white=(255,255,255)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)

res=[860,830]
init()
window=display.set_mode(res)
clock = time.Clock()
Font=font.SysFont("arial",20)

class Button(object):
	def __init__(self,num,x,y,r,text=""):
		self.x=x
		self.y=y
		self.r=r
		self.image=image.load(text)
		self.image=transform.scale(self.image,(200,200))
		self.Font=font.SysFont("arial",32)
		self.num=num
		
	def event(self,game):
		if self.click():
			if game.turn=="one":
				game.p1=self.num
				draw.circle(window,green,(self.x,self.y),self.r+10,4)
				display.flip()
				sleep(1.5)
				game.turn="two"
			elif game.turn=="two":
				game.p2=self.num
				draw.circle(window,blue,(self.x,self.y),self.r+10,4)
				display.flip()
				sleep(1.5)
				game.turn="results"


	def click(self):
		if mouse.get_pressed()[0]:
			if np.sqrt((mouse.get_pos()[0]-self.x)**2+(mouse.get_pos()[1]-self.y)**2)<self.r:
				return True

	def draw(self):

		if np.sqrt((mouse.get_pos()[0]-self.x)**2+(mouse.get_pos()[1]-self.y)**2)<self.r:
			draw.circle(window,green,(self.x,self.y),self.r,1)
		else:
			draw.circle(window,white,(self.x,self.y),self.r,1)
		#text = self.Font.render(self.text,True,white)
		window.blit(self.image,(self.x-100,self.y-100))

	
			
class Game(object):
	def __init__(self):
		self.buttons=[Button(0,430,120,120,"scissors.png"),Button(1,150,340,120,"paper.png"),Button(2,710,340,120,"rock.png"),Button(3,280,610,120,"lizard.png"),Button(4,580,610,120,"spock.png")]
		self.turn="one"
		self.p1=-1
		self.p2=-1
		self.winMatrix= [[False,True,False,True,False],
						 [False,False,True,False,True],
						 [True,False,False,True,False],
						 [False,True,False,False,True],
						 [True,False,True,False,False]]
		
	def event(self):
		for b in self.buttons:
			b.event(self)
	def draw(self):
		window.fill(black)
		for b in self.buttons:
			b.draw()
		if self.turn=="one":
			text= Font.render("Player 1",True,green)
			window.blit(text,(380,390))
		if self.turn=="two":
			text= Font.render("Player 2",True,blue)
			window.blit(text,(380,390))			
		if self.turn  =="results":
			if self.p1==self.p2:
				text= Font.render("Draw",True,red)
				window.blit(text,(390,390))	
			else:
				if self.winMatrix[self.p1][self.p2]:
					text= Font.render("Player 1 wins",True,red)
					window.blit(text,(370,390))	
				else:
					text= Font.render("Player 2 wins",True,red)
					window.blit(text,(370,390))		
			display.flip()
			sleep(4)
			self.turn="one"


game=Game()
end=False

while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True

	
	game.draw()
	game.event()

	clock.tick(20)
	display.flip()