import pygame
import sys

pygame.init()  #metodo init para arrancar todos los metodos

width = 400
height = 500

surface = pygame.display.set_mode( (width, height)) # config de la pantalla
pygame.display.set_caption('Careta') #titulo pantalla

white = pygame.Color(255,255,255) #R G B

red = pygame.Color(115, 38, 80)
green = (52, 157, 89)
blue = (0, 0 , 255)

#se puede poner la tupla my_color=(200, 120, 30)

rect = pygame.Rect( 100, 150, 120, 60) #x, y, ancho, alto
rect.center = (width // 2, height // 2)

print(rect.x)
print(rect.y)

rect2 = (100, 100, 80, 40)
#si el rectangulo solo es para pintar usar tupla, si requiere movimiento usar pygame.Rect


surface2 = pygame.Surface((200, 200))


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:    #si se cierra, se termina el proceso
			pygame.quit()
			sys.exit()  #se importa sys para que no de error

	surface.fill(white)	

	surface.blit(surface2, (100,100)) #segunda superficie

	#pygame.draw.rect(surface, red, rect) #superfice, color, rect
	#pygame.draw.circle(surface, green, (100, 200), 40 )
	#pygame.draw.line(surface, blue, (100,100), (150,100), 2)

	pygame.draw.polygon(surface, green, ((0,400),(100,300),(200,400))) #triangulo

	#pentagono
	pygame.draw.polygon(surface, red, ((146,0),(291,106),(236,277),(56,277),(0,106)))

	pygame.display.update()

