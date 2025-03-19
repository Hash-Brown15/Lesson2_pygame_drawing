import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill(("white"))
blue = "sky blue"
pygame.display.update()

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
circle = Circle(blue,(300,300),25,0)

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