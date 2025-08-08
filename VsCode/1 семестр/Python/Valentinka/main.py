import pygame
import time
import random
import sys
import gif_pygame
import threading
import os
import cv2
import turtle
import math
import ctypes
import asyncio


pygame.init()
screen = pygame.display.set_mode((900, 400), pygame.NOFRAME)
pygame.display.set_caption("Валентинка")
#icon = pygame.image.load("Valentinka\image.png")
#pygame.display.set_icon(icon)
sound = pygame.mixer.Sound(r'D:\projects\VsCode\1 семестр\Python\Valentinka\Sound.MP3')
sound1 = pygame.mixer.Sound(r'D:\projects\VsCode\1 семестр\Python\Valentinka\\1126.MP3')
sound3 = pygame.mixer.Sound(r'D:\projects\VsCode\1 семестр\Python\Valentinka\\5642.MP3')
sound4 = pygame.mixer.Sound(r'D:\projects\VsCode\1 семестр\Python\Valentinka\\5642.MP3')
gif_wolf = gif_pygame.load(r'D:\projects\VsCode\1 семестр\Python\Valentinka\wolf.gif')
gif_litvin = gif_pygame.load(r'D:\projects\VsCode\1 семестр\Python\Valentinka\litvin.gif')
gif_scary1 = gif_pygame.load(r'D:\projects\VsCode\1 семестр\Python\Valentinka\scary1.gif')
gif_scary2 = gif_pygame.load(r'D:\projects\VsCode\1 семестр\Python\Valentinka\scary2.gif')
gif_tanos = gif_pygame.load(r'D:\projects\VsCode\1 семестр\Python\Valentinka\\tanos.gif')
gif_smail = gif_pygame.load(r'D:\projects\VsCode\1 семестр\Python\Valentinka\smile-happy.gif')
img_angry = pygame.image.load(r'D:\projects\VsCode\1 семестр\Python\Valentinka\\agry.jpg')
img_angry = pygame.transform.scale(img_angry, (400, 400))
s = True
s2 = True

myfont = pygame.font.Font(r'D:\projects\VsCode\1 семестр\Python\Valentinka/Zametka_Parletter.otf', 20)
def make_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imwrite(r"D:\projects\VsCode\1 семестр\Python\Valentinka\screen.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()

make_photo()


screen.fill((255, 132, 152))
color_white = (255, 255, 255)
color_dark_white = (200, 200, 200)

tec_slaid=1

def podlost():
    os.system('dir C:\Windows\System32')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"D:\projects\VsCode\1 семестр\Python\Valentinka\\agry.jpg" , 0)
    time.sleep(3)
    os.system("ping 8.8.8.8")



def slaid1(color=color_white):
    myfont = pygame.font.Font(r'D:\projects\VsCode\1 семестр\Python\Valentinka\Zametka_Parletter.otf', 60)
    text_surface = myfont.render('Привет', False , 'White')
    button = pygame.Surface((200, 100))
    button.fill(color)
    btnfont = pygame.font.Font(r'D:\projects\VsCode\1 семестр\Python\Valentinka\Zametka_Parletter.otf', 40)
    button_text = btnfont.render('Привет', True, 'Black')
    screen.fill((255, 132, 152))
    gif_wolf.render(screen, (50, 0))
    gif_wolf.render(screen, (600, 0))
    screen.blit(text_surface, (350, 50))
    screen.blit(button, (350, 200))
    screen.blit(button_text, (380, 233))


def slaid2(color=color_white):
    screen.fill((255, 132, 152))
    text = pygame.font.Font(r'D:\projects\VsCode\1 семестр\Python\Valentinka\Zametka_Parletter.otf', 32)
    mytext = text.render('Какой ты красивый', True, 'Black')
    textm = pygame.font.Font(r'D:\projects\VsCode\1 семестр\Python\Valentinka\Zametka_Parletter.otf', 20)
    thanks = textm.render('Спасибо', True, 'Black')
    button = pygame.Surface((200, 50))
    button.fill(color)
    gif_wolf.render(screen, (50, 0))
    gif_wolf.render(screen, (600, 0))
    imageweb = pygame.image.load('screen.jpg')
    screen.blit(imageweb, (300, 80))
    screen.blit(mytext, (300, 20))
    screen.blit(button, (350, 330))
    screen.blit(thanks, (400, 340))


def slaid3(color = color_white, a = 0):
    screen.fill((255, 132, 152))
    text = pygame.font.Font(r'D:\projects\VsCode\1 семестр\Python\Valentinka\Zametka_Parletter.otf', 32)
    mytext = text.render('Пойдешь со мной', True, 'Black')
    mytext1 = text.render('на свидание?)))', True, 'Black')
    no = text.render('Нет(', True, 'Black')
    yes = text.render('Конечно)', True, 'Black')
    buttonYes = pygame.Surface((200, 90))
    buttonNo = pygame.Surface((200, 90))
    if a == 0:
        buttonNo.fill(color)
        buttonYes.fill(color)
    elif a == 1:
        buttonNo.fill(color_white)
        buttonYes.fill(color)
    elif a == 2:
        buttonNo.fill(color)
        buttonYes.fill(color_white)
    gif_litvin.render(screen, (0, 0))
    gif_litvin.render(screen, (620, 0))
    screen.blit(mytext, (300, 20))
    screen.blit(mytext1, (330, 60))
    screen.blit(buttonYes, (350, 150))
    screen.blit(buttonNo, (350, 280))
    screen.blit(yes, (380, 180))
    screen.blit(no, (410, 310))

def slaid4(): #Да
    global s
    if s:
        sound.stop()
        sound1.play()
        s = False
    screen.fill((255, 132, 152))
    text = pygame.font.Font(None, 80)
    textm = pygame.font.Font(None, 40)
    text1 = text.render('Правильный ответ)', True, 'Black')
    text2 = textm.render('Позвони мне 89044636433))', True, 'Black')
    gif_tanos.render(screen, (0, 50))
    gif_tanos.render(screen, (650, 50))
    gif_smail.render(screen, (250, 100))
    screen.blit(text1, (200, 20))
    screen.blit(text2, (260, 70))

def slaid5(color = color_white, a = 0): #Нет
    sound.stop()
    screen.fill((255, 132, 152))
    text = pygame.font.Font(None, 80)
    texts = pygame.font.Font(None, 30)
    text1 = text.render('Всмысле нет', True, 'Black')
    text2 = text.render('Точно?', True, 'Black')
    yes = texts.render('Да, точно(((', True, 'Black')
    no = texts.render('Я передумал, пойду)))', True, 'Black')
    button1 = pygame.Surface((200, 90))
    button2 = pygame.Surface((250, 70))

    if a == 0:
        button1.fill(color)
        button2.fill(color)
    elif a == 1:
        button2.fill(color_white)
        button1.fill(color)
    elif a == 2:
        button1.fill(color_white)
        button2.fill(color)

    gif_scary2.render(screen, (10, 50))
    gif_scary2.render(screen, (650, 50))
    screen.blit(text1, (280, 50))
    screen.blit(text2, (360, 100))
    screen.blit(button1, (350, 170))
    screen.blit(button2, (330, 300))
    screen.blit(yes, (390, 205))
    screen.blit(no, (340, 320))

def slaid6():
    global s2
    if s2:
        sound3.play()
        s2 = False
    screen.fill((0, 0, 0))
    text1 = pygame.font.Font(None, 80)
    text = text1.render('И зря...', True, 'White')
    screen.blit(text, (350, 200))
    pygame.display.update()
    time.sleep(3)
    screen.fill((0, 0, 0))
    text = text1.render('Многое теряешь.....', True, 'White')
    screen.blit(text, (220, 200))
    pygame.display.update()
    time.sleep(3)
    screen.fill((0, 0, 0))
    text = text1.render('В таком случае............................................', True, 'White')
    screen.blit(text, (50, 200))
    pygame.display.update()
    time.sleep(3)
    sound3.stop()
    sound4.play()
    screen.fill((0 ,0, 0))
    screen.blit(img_angry, (300, 0)) 
    pygame.display.update()
    podlost()




sound.play()
run = True
while run:
    pygame.display.update()

    mouse = pygame.mouse.get_pos()

        

    if tec_slaid == 1:
        slaid1()
        if 350 <= mouse[0] <= 550 and 200 <= mouse[1] <= 300:
            slaid1(color_dark_white)

    elif tec_slaid == 2:
        slaid2()
        if 350 <= mouse[0] <= 550 and 330 <= mouse[1] <= 380:
            slaid2(color_dark_white)
    elif tec_slaid == 3:
        slaid3()
        if (350 <= mouse[0] <= 550 and 150 <= mouse[1] <= 240):
            slaid3(color_dark_white, 1)
        elif (350 <= mouse[0] <= 550 and 280 <= mouse[1] <= 360):
            slaid3(color_dark_white, 2)
    elif tec_slaid == 4:
        slaid4()
    elif tec_slaid == 5:
        slaid5()
        if (350 <= mouse[0] <= 550 and 170 <= mouse[1] <= 260):
            slaid5(color_dark_white, 1)
        elif (350 <= mouse[0] <= 590 and 300 <= mouse[1] <= 390):
            slaid5(color_dark_white, 2)
    elif tec_slaid == 6:
        run = False
        slaid6()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 350 <= mouse[0] <= 550 and 200 <= mouse[1] <= 300 and tec_slaid == 1:
                tec_slaid = 2
            elif 350 <= mouse[0] <= 550 and 330 <= mouse[1] <= 380 and tec_slaid == 2:
                tec_slaid = 3
            elif (350 <= mouse[0] <= 550 and 150 <= mouse[1] <= 240) and tec_slaid == 3: #Если да
                tec_slaid = 4
            elif (350 <= mouse[0] <= 550 and 280 <= mouse[1] <= 360) and tec_slaid == 3: #Если нет
                tec_slaid = 5
            elif (350 <= mouse[0] <= 590 and 300 <= mouse[1] <= 390) and tec_slaid == 5:
                tec_slaid = 4
            elif (350 <= mouse[0] <= 550 and 170 <= mouse[1] <= 260) and tec_slaid == 5:
                tec_slaid = 6
                

  