import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Валентинка")
icon = pygame.image.load("pygame/free-icon-heart-2589175.png")
pygame.display.set_icon(icon)

screen.fill((255, 132, 152))

square = pygame.Surface((50, 90))
square.fill('Blue')
myfont = pygame.font.Font('pygame/Zametka_Parletter.otf', 20)
text_surface = myfont.render('Пойдешь со мной на свидание?', False , 'Black')
# b = pygame.image.load('')

running = True
while running:

    pygame.display.update()
    screen.blit(text_surface, (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                screen.fill((255, 0, 0))
            elif event.key == pygame.K_2: 
                screen.blit(square, (0, 0))
            elif event.key == pygame.K_3:
                pygame.draw.circle(screen, 'Green', (250, 150), 30)


# import pygame
# # import pygame_widgets
# # from pygame_widgets.button import Button

# # pygame.init()
# # screen = pygame.display.set_mode((600, 300))
# # pygame.display.set_caption("Валентинка")
# # icon = pygame.image.load("Valentinka/image.png")
# # pygame.display.set_icon(icon)

# # screen.fill((255, 132, 152))

# # square = pygame.Surface((50, 90))
# # square.fill('Blue')
# # myfont = pygame.font.Font('pygame/Zametka_Parletter.otf', 20)
# # text_surface = myfont.render('Пойдешь со мной на свидание?', False , 'Black')
# # # b = pygame.image.load('')

# # button1 = Button(
# #     # Mandatory Parameters
# #     screen,  # Surface to place button on
# #     50,  # X-coordinate of top left corner
# #     100,  # Y-coordinate of top left corner
# #     100,  # Width
# #     75,  # Height

# #     # Optional Parameters
# #     text='Hello',  # Text to display
# #     fontSize=50,  # Size of font
# #     margin=20,  # Minimum distance between text/image and edge of button
# #     inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
# #     hoverColour=(150, 0, 0),  # Colour of button when being hovered over
# #     pressedColour=(0, 200, 20),  # Colour of button when being clicked
# #     radius=20,  # Radius of border corners (leave empty for not curved)
# #     onClick=lambda: print('Click')  # Function to call when clicked on
# # )

# # button2 = Button(
# #     # Mandatory Parameters
# #     screen,  # Surface to place button on
# #     200,  # X-coordinate of top left corner
# #     100,  # Y-coordinate of top left corner
# #     100,  # Width
# #     75,  # Height

# #     # Optional Parameters
# #     text='Hello',  # Text to display
# #     fontSize=50,  # Size of font
# #     margin=20,  # Minimum distance between text/image and edge of button
# #     inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
# #     hoverColour=(150, 0, 0),  # Colour of button when being hovered over
# #     pressedColour=(0, 200, 20),  # Colour of button when being clicked
# #     radius=20,  # Radius of border corners (leave empty for not curved)
# #     onClick=lambda: print('Click')  # Function to call when clicked on
# # )



# # running = True
# # while running:
# #     screen.blit(text_surface, (100, 100))

# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #             pygame.quit()

# #     # pygame_widgets.update(event)
# #     pygame.display.update()


# import pygame 
# import sys 


# # initializing the constructor 
# pygame.init() 

# # screen resolution 
# res = (720,720) 

# # opens up a window 
# screen = pygame.display.set_mode(res) 

# # white color 
# color = (255,255,255) 

# # light shade of the button 
# color_light = (170,170,170) 

# # dark shade of the button 
# color_dark = (100,100,100) 

# # stores the width of the 
# # screen into a variable 
# width = screen.get_width() 

# # stores the height of the 
# # screen into a variable 
# height = screen.get_height() 

# # defining a font 
# smallfont = pygame.font.SysFont('Corbel',35) 

# # rendering a text written in 
# # this font 
# text = smallfont.render('quit' , True , color) 

# while True: 
	
# 	for ev in pygame.event.get(): 
		
# 		if ev.type == pygame.QUIT: 
# 			pygame.quit() 
			
# 		#checks if a mouse is clicked 
# 		if ev.type == pygame.MOUSEBUTTONDOWN: 
			
# 			#if the mouse is clicked on the 
# 			# button the game is terminated 
# 			if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
# 				pygame.quit() 
				
# 	# fills the screen with a color 
# 	screen.fill((60,25,60)) 
	
# 	# stores the (x,y) coordinates into 
# 	# the variable as a tuple 
# 	mouse = pygame.mouse.get_pos() 
	
# 	# if mouse is hovered on a button it 
# 	# changes to lighter shade 
# 	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
# 		pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
		
# 	else: 
# 		pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
	
# 	# superimposing the text onto our button 
# 	screen.blit(text , (width/2+50,height/2)) 
	
# 	# updates the frames of the game 
# 	pygame.display.update() 

