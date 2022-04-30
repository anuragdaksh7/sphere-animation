import pygame
import math

winWidth = 1360
winHeight = 680

win = pygame.display.set_mode((winWidth, winHeight))



class Sphere:
	def __init__(self,x_center,y_center,radius,in_angle,increament,color):

		self.x_center = x_center
		self.y_center = y_center
		self.radius = radius
		#self.factor = factor
		self.in_angle = in_angle
		self.increament = increament
		self.color = color
		self.a_angle = 0
		self.x = -1
		self.y = -1
		self.h = 0
	def move1(self):
		self.a_angle += 0.0210
	def move2(self):
		self.in_angle += self.increament
	def draw(self):
		self.h = self.radius*math.sin(self.in_angle)
		self.x = self.radius*math.cos(self.in_angle)*math.sin(self.a_angle) + self.x_center
		self.y = (self.radius*math.cos(self.a_angle)*math.cos(self.in_angle)  )/5+ self.y_center+ self.h
		pygame.draw.circle(win,self.color,(self.x,self.y),1,0)
a =Sphere(680,340,200,math.pi/2,0.0209,(0,0,0))
b =Sphere(680,340,200,-math.pi/2,-0.0209,(0,0,0))
win.fill((225,225,225))
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	#win.fill((0,0,0))
	b.draw()
	b.move1()
		#pygame.draw.line(win,(180,180,180),(a.x,a.y),(680,640),1)
	if b.a_angle > 2*math.pi:
		b.move2()
		b.a_angle = 0
	#while a.in_angle < 4.643096326794913:
	a.draw()
	#pygame.draw.line(win,(0,0,0),(a.x,a.y),(680,340),1)
	a.move1()
	#pygame.draw.line(win,(180,180,180),(a.x,a.y),(680,640),1)
	if a.a_angle > 2*math.pi:
		a.move2()
		a.a_angle = 0
	#pygame.draw.line(win,(135,135,135),(a.x,a.y),(b.x,b.y),1)
	pygame.display.update()
	#print(a.x,a.y,a.h)
	#print(a.in_angle)
pygame.quit()
