
# ======   TinyLand 弹丸之地 SUGT06a3   ======

# 本游戏由 MoYuStudio 摸魚社® 100%原创开发
# MoYuStudio 摸魚社® 隶属于 C-Prismera Tech Corp 淩创科技®
# 禁止篡改以及非法用作商业用途

# 制作人：WilsonVinson
# MoYuStudio 摸魚社® & C-Prismera Tech Corp 淩创科技® reserves the right of final explanation

# === mod input 模块导入 ===

import pygame,sys

from pygame.locals import *

# === mod init 模块初始化 ===

pygame.init()
pygame.mixer.init()

# === ManinWindow 主视窗 ===

MainWindow = pygame.display.set_mode((800, 500))

pygame.display.set_caption('TinyLand 弹丸之地', 'SUGT06a3')

icon = pygame.image.load('assets/image/testbuilding.png').convert_alpha()
pygame.display.set_icon(icon)

pygame.display.flip()

# === 1 ===

Tile_Size = 64*2

Tilemap = ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],)

Buildable = True

PretileGreen = pygame.image.load('assets/image/PretileGreen.png').convert_alpha()
PretileGreenFin = pygame.transform.scale(PretileGreen, (64*2,32*2))
PretileRed = pygame.image.load('assets/image/PretileRed.png').convert_alpha()
PretileRedFin = pygame.transform.scale(PretileRed, (64*2,32*2))

image1 = pygame.image.load('assets/image/tile1.png').convert_alpha()
image1Fin = pygame.transform.scale(image1, (64*2,32*2))
image2 = pygame.image.load('assets/image/tile2.png').convert_alpha()
image2Fin = pygame.transform.scale(image2, (64*2,32*2))
image3 = pygame.image.load('assets/image/testbuilding.png').convert_alpha()
image3Fin = pygame.transform.scale(image3, (64*2,64*2))
image4 = pygame.image.load('assets/image/tilewater.png').convert_alpha()
image4Fin = pygame.transform.scale(image4, (64*2,32*2))

Background = pygame.image.load('assets/image/testmap.png').convert_alpha()
BackgroundFin = pygame.transform.scale(Background, (1024*2,512*2))

Tile_X,Tile_Y = 6,1

Tile_Type = 0

pygame.mixer.music.set_volume(0.1)
move_sound = pygame.mixer.Sound('assets/sound/click5.ogg')
build_sound = pygame.mixer.Sound('assets/sound/rollover6.ogg')

# === Window Upload 视窗更新 ===

def Window():
    global  Buildable

    MainWindow.blit(BackgroundFin,(-64*2,-32*2))

    Tilemap_Window()

    Tilemap_YData = Tilemap[Tile_Y]
    Tile_Type_Data = Tilemap_YData[Tile_X]

    if Tile_Type == 0:
        MainWindow.blit(PretileGreenFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))

    if Tile_Type == 1:
        if Tile_Type_Data == 0:
            Buildable = True
            MainWindow.blit(PretileGreenFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))
        if Tile_Type_Data == 1:
            Buildable = False
            MainWindow.blit(PretileRedFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))
        pygame.draw.rect(MainWindow,(255,255,255),(0,0,64,64), width=0)
        MainWindow.blit(image1,(0,32))

    if Tile_Type == 2:
        if Tile_Type_Data == 0:
            Buildable = False
            MainWindow.blit(PretileRedFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))
        if Tile_Type_Data == 1:
            Buildable = True
            MainWindow.blit(PretileGreenFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))
        pygame.draw.rect(MainWindow,(255,255,255),(0,0,64,64), width=0)
        MainWindow.blit(image2,(0,32))

    if Tile_Type == 3:
        if Tile_Type_Data == 0:
            Buildable = True
            MainWindow.blit(PretileGreenFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))
        if Tile_Type_Data == 1 or Tile_Type_Data == 2:
            Buildable = False
            MainWindow.blit(PretileRedFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))
        pygame.draw.rect(MainWindow,(255,255,255),(0,0,64,64), width=0)
        MainWindow.blit(image3,(0,0))

    if Tile_Type == 4:
        if Tile_Type_Data == 0:
            Buildable = True
            MainWindow.blit(PretileGreenFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))
        if Tile_Type_Data == 1 or Tile_Type_Data == 2 or Tile_Type_Data == 3:
            Buildable = False
            MainWindow.blit(PretileRedFin,((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4))))
        pygame.draw.rect(MainWindow,(255,255,255),(0,0,64,64), width=0)
        MainWindow.blit(image4,(0,32))

    pygame.display.update()

    print(Tile_X,Tile_Y)
    print((Tile_X*(Tile_Size/2)-Tile_Y*(Tile_Size/2)),(Tile_X*(Tile_Size/4)+Tile_Y*(Tile_Size/4)))

    return Buildable

# === Window Log Upload 视窗更新 ===

def Tilemap_Window():
    
    Tilemap_Line = 0

    Tilemap_Num = 0
    
    while Tilemap_Line < 10:

        Tilemap_Line_data = Tilemap[Tilemap_Line]

        Tilemap_Num = 0
        
        while Tilemap_Num < 16:

            if Tilemap_Line_data [Tilemap_Num] == 0:
                pass

            if Tilemap_Line_data [Tilemap_Num] == 1:
                MainWindow.blit(image1Fin,((Tilemap_Num*(Tile_Size/2)-Tilemap_Line*(Tile_Size/2)),(Tilemap_Num*(Tile_Size/4)+Tilemap_Line*(Tile_Size/4))))

            if Tilemap_Line_data [Tilemap_Num] == 2:
                MainWindow.blit(image2Fin,((Tilemap_Num*(Tile_Size/2)-Tilemap_Line*(Tile_Size/2)),(Tilemap_Num*(Tile_Size/4)+Tilemap_Line*(Tile_Size/4))))
            
            if Tilemap_Line_data [Tilemap_Num] == 3:
                MainWindow.blit(image3Fin,((Tilemap_Num*(Tile_Size/2)-Tilemap_Line*(Tile_Size/2)),(Tilemap_Num*(Tile_Size/4)+Tilemap_Line*(Tile_Size/4)-32*2)))
            
            if Tilemap_Line_data [Tilemap_Num] == 4:
                MainWindow.blit(image4Fin,((Tilemap_Num*(Tile_Size/2)-Tilemap_Line*(Tile_Size/2)),(Tilemap_Num*(Tile_Size/4)+Tilemap_Line*(Tile_Size/4))))

            Tilemap_Num += 1

        Tilemap_Line += 1

# === Main Loop 主循环 ===

while True:

    Window()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #if event.type == pygame.MOUSEMOTION:

            mouse_pos = event.pos

            mouse_pos_x,mouse_pos_y = mouse_pos
            
            mouse_pos_x_Fin,mouse_pos_y_Fin = int((mouse_pos_x/50)/1),int((mouse_pos_y/100)/1)

            print(mouse_pos_x,mouse_pos_y)
            print(mouse_pos_x_Fin,mouse_pos_y_Fin)

            Window()

        if event.type == pygame.KEYDOWN:

            if event.key == K_UP:

                Tile_Y -= 1
                move_sound.play()

                Window()

            if event.key == K_DOWN:

                Tile_Y += 1
                move_sound.play()

                Window()

            if event.key == K_RIGHT:

                Tile_X += 1
                move_sound.play()

                Window()

            if event.key == K_LEFT:

                Tile_X -= 1
                move_sound.play()

                Window()

            if event.key == K_0:
                Tile_Type = 0

            if event.key == K_1:
                Tile_Type = 1

            if event.key == K_2:
                Tile_Type = 2

            if event.key == K_3:
                Tile_Type = 3

            if event.key == K_4:
                Tile_Type = 4

            if event.key == K_q:

                if Buildable == True:

                    Tilemap_YData = Tilemap[Tile_Y]
                    Tilemap_YData[Tile_X] = Tile_Type

                    build_sound.play()