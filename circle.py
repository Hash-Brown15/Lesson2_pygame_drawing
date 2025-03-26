import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))

blue = (64,237,234)
red = (224,36,55)
green = (72,214,56)
white = (255,255,255)
black = (0,0,0)
yellow = (72,214,56)
pygame.display.update()

screen.fill(("white"))
class Circle:
    def __init__(self,color,pos,radius,width):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        self.screen = screen

    def draw(self):
        self.draw_circle = pygame.draw.circle(
            self.screen,
            self.color,
            self.pos,
            self.radius,
            self.width
        )
    def grow(self,r):
        self.radius += r
        self.draw_circle = pygame.draw.circle(
        self.screen,
        self.color,
        self.pos,
        self.radius,
        self.width
        )
position = (300,300)
radius = 50
width = 2
pygame.draw.circle(screen,red,position,radius,width)
pygame.display.update
blueCircle = Circle(screen,blue,position,radius,width)

while 1 :
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circle.draw()
            pygame.display.update() 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circle.grow()
            pygame.display.update()