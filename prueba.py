import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height))
pygame.display.set_caption('Rectangulos')

white = pygame.Color(255,0,0) #R G B

red = pygame.Color(115, 38, 80)

#se puede poner la tupla my_color=(200, 120, 30)

rect = pygame.Rect( 100, 150, 120, 60) #x, y, ancho, alto

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	surface.fill(white)	

	pygame.draw.rect(surface, red, rect) #superfice, color, rect

	pygame.display.update()