import pygame
import tkinter as tk
from tkinter import *
import threading
import sys
import math



class object_elem:
    def __init__(self, name, color, weight = 500, status = 'dinamik', position = [0, 0], speed = [0.1, 1.5], boost = [0.0, 0.0]):
        self.__name = str(name)
        self.__color = color
        self.__weight = int(weight)
        self.__status = status
        self.__position = position
        self.__speed = speed
        self.__boost = boost

    def __getName(self):
        return self.__name
    def __getColor(self):
        return self.__color
    def __getWeight(self):
        return self.__weight
    def __getStatus(self):
        return self.__status
    def __getPosition(self):
        return self.__position
    def __getSpeed(self):
        return self.__speed
    def __getBoost(self):
        return self.__boost
    def __newName(self, new):
        self.__name = new
    def __newColor(self, new): 
        self.__color = new
    def __newWeight(self, new):
        self.__weight = new
    def __newStatus(self, new):
        self.__status = new
    def __newPosition(self, new):
        self.__position = new
    def __newSpeed(self, new):
        self.__speed = new
    def __newBoost(self, new):
        self.__boost = new

    def update_position(self): #Временная функция для первой попытки с одой звездой и планетой
        if len(listElem) > 1:
            for obj in listElem:
                if obj.name == self.__name:
                    continue
                X0 = obj.position[0]
                Y0 = obj.position[1]
                M0 = obj.weight

                r = math.sqrt((self.__position[0] - X0)**2 + (self.__position[1] - Y0)**2)
                self.__boost[0] = M0 * (X0 - self.__position[0]) / r**3
                self.__boost[1] = M0 * (Y0 - self.__position[1]) / r**3
                self.__speed[0] += self.__boost[0]
                self.__speed[1] += self.__boost[1]
                self.__position[0] += self.__speed[0]
                self.__position[1] += self.__speed[1]


        
    
    name = property (__getName, __newName)
    color = property (__getColor, __newColor)
    weight = property (__getWeight, __newWeight)
    status = property (__getStatus, __newStatus)
    position = property (__getPosition, __newPosition)
    speed = property (__getSpeed, __newSpeed)
    boost = property (__getBoost, __newBoost)

listElem = []

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Гравитация")

img_reset = pygame.image.load('Photo_reset.png')
img_reset = pygame.transform.scale(img_reset, (60, 60))
img_create = pygame.image.load('Photo_create.png')
img_create = pygame.transform.scale(img_create, (120, 120))

img_checkbox_off = pygame.image.load('checkbox_off.png')
img_checkbox_on = pygame.image.load('checkbox_on.png')
img_checkbox_off = pygame.transform.scale(img_checkbox_off, (60, 60))
img_checkbox_on = pygame.transform.scale(img_checkbox_on, (60, 60))
checkbox = True



RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colorsRGB = [RED, GREEN, BLUE]
colorForText = {
    RED: "Red",
    GREEN: "Green",
    BLUE: "Blue",
    WHITE: "White",
    BLACK: "Black"
}

process = False
se = True
G = 1
T = 1
#Две константы, нужны для точности

def create_new_elem():
    def save_conf():
        global sett
        try:
            entrySpeed=[float(entrySpeedX.get()), float(entrySpeedY.get())]
            entryBoost=[float(entryBoostX.get()), float(entryBoostY.get())]
        except:
            entrySpeed=[0.1, 1.5]
            entryBoost=[0.0, 0.0]
        sett = [e1.get(), colorsRGB[v.get()-1], e2.get(), v2.get(), entrySpeed, entryBoost]
        print(e1.get(), colorsRGB[v.get()-1], e2.get(), v2.get(), entrySpeed, entryBoost, sep='\n')
        root.destroy()
    root = tk.Tk()
    root.geometry("150x400")
    root.attributes("-topmost", True)
    Label(root, text='Имя').grid(row=0, column=1)
    e1 = Entry(root)
    e1.grid(row=1, column=1)

    Label(root, text="Выбери цвет").grid(row=2, column=1)
    v = IntVar(root, 1)
    rb1=Radiobutton(root, text='Красный', variable=v, value=1)
    rb1.grid(row=3, column=1)
    rb2=Radiobutton(root, text='Зелений', variable=v, value=2)
    rb2.grid(row=4, column=1)
    rb3=Radiobutton(root, text='Синий', variable=v, value=3)
    rb3.grid(row=5, column=1)
    Label(root, text="Впишите массу").grid(row=6, column=1)
    e2 = Entry(root)
    e2.grid(row=7, column=1)
    Label(root, text="Выберите тип объекта").grid(row=8, column=1)
    v2 = StringVar(root, 1)
    rb4=Radiobutton(root, text='Статический', variable=v2, value='statik')
    rb4.grid(row=9, column=1)
    rb4=Radiobutton(root, text='Динамический', variable=v2, value='dinamik')
    rb4.grid(row=10, column=1)
    Label(root, text='Задайте скорость').grid(row=11, column=1)
    entrySpeedX = Entry(root)
    entrySpeedX.grid(row=12, column=1)
    entrySpeedY = Entry(root)
    entrySpeedY.grid(row=12, column=2)

    Label(root, text='Задайте ускорение').grid(row=13, column=1)
    entryBoostX = Entry(root)
    entryBoostX.grid(row=14, column=1)
    entryBoostY = Entry(root)
    entryBoostY.grid(row=14, column=2)


    button = tk.Button(root, text='Создать', width=15, command=lambda :save_conf())
    button.grid(row=15, column=1)
    root.mainloop()

def start_end():
    def update():
        if se == False:
            root1.destroy()
        def fun(a):
            global process
            process = a
        if process == False:
            label.config(text="Остановлена")
            button.config(text='Запустить', command=lambda :fun(True))
        if process == True:
            label.config(text="Запущена")
            button.config(text='Остановить', command=lambda :fun(False))
        root1.after(100, update)

    root1 = tk.Tk()
    root1.geometry("200x200")
    root1.attributes("-topmost", True)
    label = Label(root1, text="Остановлена")
    label.pack(fill=BOTH, expand=True)
    button = tk.Button(root1, text='Запустить', width=15, command=lambda :fun(True))
    button.pack(expand=True)
    update()
    root1.mainloop()

def create_n_e():
    process = False
    text = pygame.font.Font(None, 40)
    text1 = text.render('Выберите место для вашего объекта', False, 'White')
    check = True
    thread1 = threading.Thread(target=create_new_elem)
    while check:
        screen.blit(text1, (140, 740))
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                check = False
                break
    pygame.draw.circle(screen, WHITE, (mouse[0], mouse[1]), 10)
    pygame.display.update()
    thread1.start()
    thread1.join()
    elem = object_elem(sett[0], sett[1], sett[2], sett[3], [mouse[0],mouse[1]], sett[4], sett[5])
    listElem.append(elem)
    process = True
    



run = True
while run:
    screen.fill(BLACK)
    mouse = pygame.mouse.get_pos()

    screen.blit(img_create, (50, 0))
    screen.blit(img_reset, (80, 200))
    for obj in listElem:
        pygame.draw.circle(screen, obj.color, obj.position, 10)
        if obj.status == 'dinamik':
            obj.update_position()
        if checkbox == True:
            text = pygame.font.Font(None, 20)
            text1 = text.render(obj.name, False, colorForText[obj.color])
            text2 = text.render(str(obj.weight), False, colorForText[obj.color])
            screen.blit(text1, (obj.position[0]-10, obj.position[1]+18))
            screen.blit(text2, (obj.position[0]-10, obj.position[1]-24))    
            
    if checkbox:
        screen.blit(img_checkbox_on, (80, 280))
    if checkbox == False:
        screen.blit(img_checkbox_off, (80, 280))
    text = pygame.font.Font(None, 35)
    text_oi = text.render("Имя Вес", False, 'White')
    screen.blit(text_oi, (60, 350))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            se = False
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 50 <= mouse[0] <= 170 and 40 <= mouse[1] <= 80:
                create_n_e()
            if 80 <= mouse[0] <= 140 and 280 <= mouse[1] <= 340:
                if checkbox == True:
                    checkbox = False
                else:
                    checkbox = True
            if 80 <= mouse[0] <= 140 and 200 <= mouse[1] <= 260:
                listElem=[]


    
    if run == False:
        break
    pygame.display.update()



