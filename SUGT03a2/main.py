# ======   游戏公司模拟器 SUGT03a2   ======

# 本游戏由 MoYu.Co 摸魚社® 100%原创开发
# MoYu.Co 摸魚社® 隶属于 C-Prismera Tech Corp 淩创科技®
# 禁止篡改以及非法用作商业用途

# 制作人：WilsonVinson
# MoYu.Co 摸魚社® & C-Prismera Tech Corp 淩创科技® reserves the right of final explanation

import pygame
import moviepy
import random
import time
#import mutagen

from pygame.locals import *
from moviepy.editor import *
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# from display import speed_button_display
# import display

# === Init 进入 ===

pygame.init()

# === Screen 屏幕 ===

screen_level = 3
screen_width = 320 * screen_level
screen_height = 180 * screen_level
MainWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('游戏公司模拟器 Game.Co Simulator', 'SUGT03a2')

icon = pygame.image.load('assets/image/game_icon.png').convert_alpha()
pygame.display.set_icon(icon)

pygame.display.flip()

clock = pygame.time.Clock()
clock.tick(120)

# === Font 字体 ===

font1 = pygame.font.Font('assets/font/LockClock.ttf', 11 * screen_level)
font2 = pygame.font.Font('assets/font/LockClock.ttf', 6 * screen_level)
font3 = pygame.font.Font('assets/font/方正像素16.TTF', 10 * screen_level)
font4 = pygame.font.Font('assets/font/LockClock.ttf', 5 * screen_level)

# === Screen Init 屏幕 进入 ===

video = r'assets/video/initVideo2.mp4'
clip = VideoFileClip(video, audio=True).resize([(1920 / 6) * screen_level, (1080 / 6) * screen_level])

logo = pygame.image.load('assets/image/icon_x100.png').convert_alpha()
logoFin = pygame.transform.scale(logo, (64 * screen_level, 64 * screen_level))
logotext = pygame.image.load('assets/image/icontext_x100.png').convert_alpha()
logotextFin = pygame.transform.scale(logotext, (128 * screen_level, 32 * screen_level))

# === Screen FirstTime Init 屏幕 初次游戏 ===

firsttimeinit_text1 = font3.render('给你的游戏公司取个名吧！', True, (255, 255, 255))

firsttimeinit_text_inputtext = ''

# === Screen Init Main 屏幕 进入 主界面 ===

initmain_initmain = pygame.image.load('assets/image/initmain.png').convert_alpha()
initmain_initmainFin = pygame.transform.scale(initmain_initmain, (320 * screen_level, 180 * screen_level))

initmain_gamelogo = pygame.image.load('assets/image/gamelogo.png').convert_alpha()
initmain_gamelogoFin = pygame.transform.scale(initmain_gamelogo, (128 * screen_level, 64 * screen_level))

initmain_text6 = font4.render('Game.Co Simulator SUGT03a2 Dv2021053101', True, (255, 255, 255))

initmain_text1 = font3.render('新游戏', True, (255, 255, 255))
initmain_button01 = pygame.image.load('assets/image/button.png').convert_alpha()
initmain_button01Fin = pygame.transform.scale(initmain_button01, (64 * screen_level, 16 * screen_level))
initmain_text2 = font3.render('旧游戏', True, (255, 255, 255))
initmain_button02 = pygame.image.load('assets/image/button.png').convert_alpha()
initmain_button02Fin = pygame.transform.scale(initmain_button02, (64 * screen_level, 16 * screen_level))
initmain_text3 = font3.render('设置', True, (255, 255, 255))
initmain_button03 = pygame.image.load('assets/image/button.png').convert_alpha()
initmain_button03Fin = pygame.transform.scale(initmain_button03, (64 * screen_level, 16 * screen_level))
initmain_text4 = font3.render('关于1', True, (255, 255, 255))
initmain_button04 = pygame.image.load('assets/image/button.png').convert_alpha()
initmain_button04Fin = pygame.transform.scale(initmain_button04, (64 * screen_level, 16 * screen_level))
initmain_text5 = font3.render('关于2', True, (255, 255, 255))
initmain_button05 = pygame.image.load('assets/image/button.png').convert_alpha()
initmain_button05Fin = pygame.transform.scale(initmain_button05, (64 * screen_level, 16 * screen_level))

#                                                               button_number v       button_number v
initmain_button01_x, initmain_button01_y = 240 * screen_level, 15 * screen_level + 1 * 3 * screen_level + 0 * 16 * screen_level
initmain_button01_w, initmain_button01_h = 64 * screen_level, 16 * screen_level
initmain_button02_x, initmain_button02_y = 240 * screen_level, 15 * screen_level + 2 * 3 * screen_level + 1 * 16 * screen_level
initmain_button02_w, initmain_button02_h = 64 * screen_level, 16 * screen_level
initmain_button03_x, initmain_button03_y = 240 * screen_level, 15 * screen_level + 3 * 3 * screen_level + 2 * 16 * screen_level
initmain_button03_w, initmain_button03_h = 64 * screen_level, 16 * screen_level
initmain_button04_x, initmain_button04_y = 240 * screen_level, 15 * screen_level + 4 * 3 * screen_level + 3 * 16 * screen_level
initmain_button04_w, initmain_button04_h = 64 * screen_level, 16 * screen_level
initmain_button05_x, initmain_button05_y = 240 * screen_level, 15 * screen_level + 5 * 3 * screen_level + 4 * 16 * screen_level
initmain_button05_w, initmain_button05_h = 64 * screen_level, 16 * screen_level

# === Screen Main 屏幕 主界面 ===

#                   button_number v       button_number v
main_button01_x, main_button01_y = 1 * 3 * screen_level + 0 * 32 * screen_level, 3 * screen_level
main_button01_w, main_button01_h = 32 * screen_level, 32 * screen_level
main_button02_x, main_button02_y = 2 * 3 * screen_level + 1 * 32 * screen_level, 3 * screen_level
main_button02_w, main_button02_h = 32 * screen_level, 32 * screen_level
main_button03_x, main_button03_y = 3 * 3 * screen_level + 2 * 32 * screen_level, 3 * screen_level
main_button03_w, main_button03_h = 32 * screen_level, 32 * screen_level
main_button04_x, main_button04_y = 4 * 3 * screen_level + 3 * 32 * screen_level, 3 * screen_level
main_button04_w, main_button04_h = 32 * screen_level, 32 * screen_level
main_button05_x, main_button05_y = 5 * 3 * screen_level + 4 * 32 * screen_level, 3 * screen_level
main_button05_w, main_button05_h = 32 * screen_level, 32 * screen_level

main_button06_x, main_button06_y = screen_width - 32 * screen_level - 3 * screen_level, 3 * screen_level
main_button06_w, main_button06_h = 32 * screen_level, 32 * screen_level

main_button01 = pygame.image.load('assets/image/button01.png').convert_alpha()
main_button01Fin = pygame.transform.scale(main_button01, (32 * screen_level, 32 * screen_level))
main_button02 = pygame.image.load('assets/image/button02.png').convert_alpha()
main_button02Fin = pygame.transform.scale(main_button02, (32 * screen_level, 32 * screen_level))
main_button03 = pygame.image.load('assets/image/button03.png').convert_alpha()
main_button03Fin = pygame.transform.scale(main_button03, (32 * screen_level, 32 * screen_level))
main_button04 = pygame.image.load('assets/image/button04.png').convert_alpha()
main_button04Fin = pygame.transform.scale(main_button04, (32 * screen_level, 32 * screen_level))
main_button05 = pygame.image.load('assets/image/button05.png').convert_alpha()
main_button05Fin = pygame.transform.scale(main_button05, (32 * screen_level, 32 * screen_level))

main_info_bar = pygame.image.load('assets/image/info_bar.png').convert_alpha()
main_info_barFin = pygame.transform.scale(main_info_bar, (104 * screen_level, 32 * screen_level))

main_button06 = pygame.image.load('assets/image/setting_button.png').convert_alpha()
main_button06Fin = pygame.transform.scale(main_button06, (32 * screen_level, 32 * screen_level))

main_leaderboard = pygame.image.load('assets/image/leaderboard.png').convert_alpha()
main_leaderboardFin = pygame.transform.scale(main_leaderboard, (102 * screen_level, 129 * screen_level))

main_news_board = pygame.image.load('assets/image/news_board.png').convert_alpha()
main_news_boardFin = pygame.transform.scale(main_news_board, (209 * screen_level, 129 * screen_level))

# === Screen Assets 屏幕 资产 ===

assets_text1 = font1.render('Assets', True, (255, 255, 255))

# === Screen Policy 屏幕 政策 ===

policy_text1 = font1.render('Policy', True, (255, 255, 255))

# === Screen Personnel 屏幕 人员 ===

personnel_text1 = font1.render('Personnel', True, (255, 255, 255))

# === Screen Project 屏幕 项目 ===

project_text1 = font1.render('Project', True, (255, 255, 255))

# === Screen Stock 屏幕 股市 ===

stock_stock_window = False

stock_stock_draw = (159 * screen_level) / 3

stock_stock_w = 8 * screen_level

stock_stock_h = 90 * screen_level

stock_stock_wOld = 8 * screen_level

stock_stock_hOld = 90 * screen_level

stock_stock_base = 0.5

stock_text1 = font1.render('Stock', True, (255, 255, 255))

stock_board = pygame.image.load('assets/image/stock_board.png').convert_alpha()
stock_boardFin = pygame.transform.scale(stock_board, (170 * screen_level, 152 * screen_level))

# === Screen Setting 屏幕 设置 ===

setting_text1 = font1.render('Setting', True, (255, 255, 255))

setting_info_bar = pygame.image.load('assets/image/info_bar.png').convert_alpha()
setting_info_barFin = pygame.transform.scale(main_info_bar, (104 * screen_level, 32 * screen_level))
setting_info_bar2 = pygame.image.load('assets/image/info_bar2.png').convert_alpha()
setting_info_bar2Fin = pygame.transform.scale(setting_info_bar2, (104 * screen_level, 127 * screen_level))
setting_setting_bar = pygame.image.load('assets/image/setting_bar.png').convert_alpha()
setting_setting_barFin = pygame.transform.scale(setting_setting_bar, (207 * screen_level, 162 * screen_level))

setting_text1 = font3.render('新游戏', True, (255, 255, 255))
setting_button01 = pygame.image.load('assets/image/button.png').convert_alpha()
setting_button01Fin = pygame.transform.scale(setting_button01, (64 * screen_level, 16 * screen_level))

setting_button01_x, setting_button01_y = 240 * screen_level, 15 * screen_level + 1 * 3 * screen_level + 0 * 16 * screen_level
setting_button01_w, setting_button01_h = 64 * screen_level, 16 * screen_level

# === Screen Total 屏幕 全局 ===


# === Screen Total Display Variable 屏幕 全局 显示 变量 ===

money_icon = pygame.image.load('assets/image/money_icon.png').convert_alpha()
money_iconFin = pygame.transform.scale(money_icon, (5 * screen_level, 5 * screen_level))

home_button = pygame.image.load('assets/image/home_button.png').convert_alpha()
home_buttonFin = pygame.transform.scale(home_button, (9 * screen_level, 9 * screen_level))

speed_button01 = pygame.image.load('assets/image/speed_button01.png').convert_alpha()
speed_button01Fin = pygame.transform.scale(speed_button01, (14 * screen_level, 7 * screen_level))
speed_button02 = pygame.image.load('assets/image/speed_button02.png').convert_alpha()
speed_button02Fin = pygame.transform.scale(speed_button02, (14 * screen_level, 7 * screen_level))
speed_button03 = pygame.image.load('assets/image/speed_button03.png').convert_alpha()
speed_button03Fin = pygame.transform.scale(speed_button03, (14 * screen_level, 7 * screen_level))
speed_button04 = pygame.image.load('assets/image/speed_button04.png').convert_alpha()
speed_button04Fin = pygame.transform.scale(speed_button04, (14 * screen_level, 7 * screen_level))
speed_button05 = pygame.image.load('assets/image/speed_button05.png').convert_alpha()
speed_button05Fin = pygame.transform.scale(speed_button05, (14 * screen_level, 7 * screen_level))

save_button = pygame.image.load('assets/image/save_button.png').convert_alpha()
save_buttonFin = pygame.transform.scale(save_button, (9 * screen_level, 9 * screen_level))


# === Screen Total Display 屏幕 全局 显示 ===

def speed_button_display():
    #                         button_number v
    MainWindow.blit(speed_button01Fin,
                    ((0 * (14 + 3)) * screen_level + 3 * screen_level, screen_height - 10 * screen_level))
    MainWindow.blit(speed_button02Fin,
                    ((1 * (14 + 3)) * screen_level + 3 * screen_level, screen_height - 10 * screen_level))
    MainWindow.blit(speed_button03Fin,
                    ((2 * (14 + 3)) * screen_level + 3 * screen_level, screen_height - 10 * screen_level))
    MainWindow.blit(speed_button04Fin,
                    ((3 * (14 + 3)) * screen_level + 3 * screen_level, screen_height - 10 * screen_level))
    MainWindow.blit(speed_button05Fin,
                    ((4 * (14 + 3)) * screen_level + 3 * screen_level, screen_height - 10 * screen_level))


# === Screen Total Click Variable 屏幕 全局 点击 变量 ===

home_button_x, home_button_y = 3 * screen_level, 3 * screen_level
home_button_w, home_button_h = 9 * screen_level, 9 * screen_level

#                      button_number v
speed_button01_x, speed_button01_y = 0 * (14 + 3) * screen_level + 3 * screen_level, screen_height - 10 * screen_level
speed_button01_w, speed_button01_h = 14 * screen_level, 7 * screen_level
speed_button02_x, speed_button02_y = 1 * (14 + 3) * screen_level + 3 * screen_level, screen_height - 10 * screen_level
speed_button02_w, speed_button02_h = 14 * screen_level, 7 * screen_level
speed_button03_x, speed_button03_y = 2 * (14 + 3) * screen_level + 3 * screen_level, screen_height - 10 * screen_level
speed_button03_w, speed_button03_h = 14 * screen_level, 7 * screen_level
speed_button04_x, speed_button04_y = 3 * (14 + 3) * screen_level + 3 * screen_level, screen_height - 10 * screen_level
speed_button04_w, speed_button04_h = 14 * screen_level, 7 * screen_level
speed_button05_x, speed_button05_y = 4 * (14 + 3) * screen_level + 3 * screen_level, screen_height - 10 * screen_level
speed_button05_w, speed_button05_h = 14 * screen_level, 7 * screen_level

save_button_x, save_button_y = screen_width - 9 * screen_level - 3 * screen_level, 3 * screen_level
save_button_w, save_button_h = 9 * screen_level, 9 * screen_level


# === Screen Total Click 屏幕 全局 点击 ===

def speed_button_click():
    if speed_button01_x <= mouse_x <= speed_button01_x + speed_button01_w and speed_button01_y <= mouse_y <= speed_button01_y + speed_button01_h:
        print('speed_button01 be clicked')
        button_click_sound.play()
    if speed_button02_x <= mouse_x <= speed_button02_x + speed_button02_w and speed_button02_y <= mouse_y <= speed_button02_y + speed_button02_h:
        print('speed_button02 be clicked')
        button_click_sound.play()
    if speed_button03_x <= mouse_x <= speed_button03_x + speed_button03_w and speed_button03_y <= mouse_y <= speed_button03_y + speed_button03_h:
        print('speed_button03 be clicked')
        button_click_sound.play()
    if speed_button04_x <= mouse_x <= speed_button04_x + speed_button04_w and speed_button04_y <= mouse_y <= speed_button04_y + speed_button04_h:
        print('speed_button04 be clicked')
        button_click_sound.play()
    if speed_button05_x <= mouse_x <= speed_button05_x + speed_button05_w and speed_button05_y <= mouse_y <= speed_button05_y + speed_button05_h:
        print('speed_button05 be clicked')
        button_click_sound.play()


def save_button_click():
    if save_button_x <= mouse_x <= save_button_x + save_button_w and save_button_y <= mouse_y <= save_button_y + save_button_h:
        print('save_button be clicked')
        button_click_sound.play()

        saveslot_save('save/player_name', str(player_name))
        saveslot_save('save/money', str(money))
        saveslot_save('save/prestige', str(prestige))

        print('save complete')


# === Screen Total Time 屏幕 全局 时间 ===

time_year = time.strftime('%Y', time.gmtime())

time_month = time.strftime('%m', time.gmtime())

time_day = time.strftime('%d', time.gmtime())

time_year_text = font2.render(str(time_year), True, (255, 255, 255))
time_month_text = font2.render(str(time_month), True, (255, 255, 255))
time_day_text = font2.render(str(time_day), True, (255, 255, 255))

# === Sound 音乐 ===

pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
logo_sound = pygame.mixer.Sound('assets/sound/Pause.wav')

bgm_sound = pygame.mixer.Sound('assets/sound/Ooyy - Sober Language_01.ogg')

button_click_sound = pygame.mixer.Sound('assets/sound/click5.ogg')

# === Player Assets 玩家 资产 ===

player_name = ''
player_nameFin = font2.render(player_name, True, (255, 255, 255))

money = 1000
moneyOld = money

prestige = 100


# === Save 保存系统 ===

def saveslot_save(filename, data):
    write_data = open(filename, 'w')
    write_data.write(data)


def saveslot_load(filename):
    read_data = open(filename, 'r')
    data = read_data.read()
    print(data)
    return data

# === Word Input 文字输入系统 ===



# === Main Loop 主循环 ===

init_window = True

firsttimeinit_window = False
firsttimeinit_window_init = True

initmain_window = False

main_window = False

assets_window = False

policy_window = False

personnel_window = False

project_window = False

stock_window = False

setting_window = False

while True:

    # === Screen Init 屏幕 进入 ===

    if init_window:

        clip.preview()

        pygame.display.update()

        init_window = False
        initmain_window = True

    # === Screen Init Main 屏幕 进入 主界面 ===

    elif initmain_window:

        #pygame.mixer.music.set_volume(0.5)
        #bgm_sound.play()

        MainWindow.blit(initmain_initmainFin, (0 * screen_level, 0 * screen_level))

        #                                                           button_number v       button_number v
        MainWindow.blit(initmain_button01Fin, (240 * screen_level, 15 * screen_level + 1 * 3 * screen_level + 0 * 16 * screen_level))
        MainWindow.blit(initmain_button02Fin, (240 * screen_level, 15 * screen_level + 2 * 3 * screen_level + 1 * 16 * screen_level))
        MainWindow.blit(initmain_button03Fin, (240 * screen_level, 15 * screen_level + 3 * 3 * screen_level + 2 * 16 * screen_level))
        MainWindow.blit(initmain_button04Fin, (240 * screen_level, 15 * screen_level + 4 * 3 * screen_level + 3 * 16 * screen_level))
        MainWindow.blit(initmain_button05Fin, (240 * screen_level, 15 * screen_level + 5 * 3 * screen_level + 4 * 16 * screen_level))

        MainWindow.blit(initmain_text1, (260 * screen_level, 18 * screen_level + 1 * 3 * screen_level + 0 * 16 * screen_level))
        MainWindow.blit(initmain_text2, (260 * screen_level, 18 * screen_level + 2 * 3 * screen_level + 1 * 16 * screen_level))
        MainWindow.blit(initmain_text3, (260 * screen_level, 18 * screen_level + 3 * 3 * screen_level + 2 * 16 * screen_level))
        MainWindow.blit(initmain_text4, (260 * screen_level, 18 * screen_level + 4 * 3 * screen_level + 3 * 16 * screen_level))
        MainWindow.blit(initmain_text5, (260 * screen_level, 18 * screen_level + 5 * 3 * screen_level + 4 * 16 * screen_level))

        MainWindow.blit(initmain_gamelogoFin, (100 * screen_level, 3 * screen_level))

        MainWindow.blit(initmain_text6, (3 * screen_level, 172 * screen_level))

        pygame.display.update()

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if initmain_button01_x <= mouse_x <= initmain_button01_x + initmain_button01_w and initmain_button01_y <= mouse_y <= initmain_button01_y + initmain_button01_h:
                    print('initmain_button01 be clicked')
                    button_click_sound.play()
                    firsttimeinit_window = True
                    initmain_window = False

                if initmain_button02_x <= mouse_x <= initmain_button02_x + initmain_button02_w and initmain_button02_y <= mouse_y <= initmain_button02_y + initmain_button02_h:
                    print('initmain_button02 be clicked')
                    button_click_sound.play()

                    player_name = saveslot_load('save/player_name')
                    money = saveslot_load('save/money')
                    prestige = saveslot_load('save/prestige')

                    print(money)
                    main_window = True
                    initmain_window = False

                if initmain_button03_x <= mouse_x <= initmain_button03_x + initmain_button03_w and initmain_button03_y <= mouse_y <= initmain_button03_y + initmain_button03_h:
                    print('initmain_button03 be clicked')
                    button_click_sound.play()
                    #setting_window = True
                    #initmain_window = False

                if initmain_button04_x <= mouse_x <= initmain_button04_x + initmain_button04_w and initmain_button04_y <= mouse_y <= initmain_button04_y + initmain_button04_h:
                    print('initmain_button04 be clicked')
                    button_click_sound.play()

                if initmain_button05_x <= mouse_x <= initmain_button05_x + initmain_button05_w and initmain_button05_y <= mouse_y <= initmain_button05_y + initmain_button05_h:
                    print('initmain_button05 be clicked')
                    button_click_sound.play()

    # === Screen FirstTime 屏幕 初次游戏 ===

    elif firsttimeinit_window:

        if firsttimeinit_window_init == True:

            MainWindow.fill((161, 136, 127))

            MainWindow.blit(firsttimeinit_text1, (screen_width / 2 - 55 * screen_level, screen_height / 2 - 60 * screen_level))

            pygame.draw.rect(MainWindow, (255, 255, 255), (350, 300, 250, 45), width=0)

            pygame.display.update()

        else:
            pass

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            elif event.type == pygame.KEYDOWN:

                if event.key == 13:
                    print('enter')
                    firsttimeinit_window_next = True
                    player_name = firsttimeinit_text_inputtext
                    player_nameFin = font1.render(player_name, True, (255, 255, 255))
                    main_window = True
                    firsttimeinit_window = False
                    firsttimeinit_window_init = False

                firsttimeinit_text_inputtext_input = chr(event.key)
                print(firsttimeinit_text_inputtext_input)
                firsttimeinit_text_inputtext = str(firsttimeinit_text_inputtext) + str(firsttimeinit_text_inputtext_input)
                print(firsttimeinit_text_inputtext)
                firsttimeinit_text_inputtextFin = font1.render(firsttimeinit_text_inputtext, True, (0, 0, 0))
                pygame.time.delay(33)

                firsttimeinit_window_init = False

                MainWindow.fill((161, 136, 127))

                MainWindow.blit(firsttimeinit_text1, (screen_width / 2 - 55 * screen_level, screen_height / 2 - 60 * screen_level))

                pygame.draw.rect(MainWindow, (255, 255, 255), (350, 300, 250, 45), width=0)

                MainWindow.blit(firsttimeinit_text_inputtextFin, (screen_width / 2 - 40 * screen_level, screen_height / 2 + 10 * screen_level))

                pygame.display.update()

    # === Screen Main 屏幕 主界面 ===

    elif main_window:

        MainWindow.fill((161, 136, 127))
        #                  button_number v       button_number v
        MainWindow.blit(main_button01Fin, (1 * 3 * screen_level + 0 * 32 * screen_level, 3 * screen_level))
        MainWindow.blit(main_button02Fin, (2 * 3 * screen_level + 1 * 32 * screen_level, 3 * screen_level))
        MainWindow.blit(main_button03Fin, (3 * 3 * screen_level + 2 * 32 * screen_level, 3 * screen_level))
        MainWindow.blit(main_button04Fin, (4 * 3 * screen_level + 3 * 32 * screen_level, 3 * screen_level))
        MainWindow.blit(main_button05Fin, (5 * 3 * screen_level + 4 * 32 * screen_level, 3 * screen_level))

        MainWindow.blit(main_info_barFin, (6 * 3 * screen_level + 5 * 32 * screen_level, 3 * screen_level))

        MainWindow.blit(main_button06Fin, (screen_width - 32 * screen_level - 3 * screen_level, 3 * screen_level))

        MainWindow.blit(main_leaderboardFin, (3 * screen_level, screen_height - 139 * screen_level - 3 * screen_level))
        player_nameFin = font2.render(player_name, True, (255, 255, 255))
        MainWindow.blit(player_nameFin, (25 * screen_level, 157 * screen_level))

        MainWindow.blit(main_news_boardFin, (screen_width - 209 * screen_level - 3 * screen_level, screen_height - 139 * screen_level - 3 * screen_level))

        speed_button_display()

        MainWindow.blit(time_year_text, (212 * screen_level, 3 * screen_level))
        MainWindow.blit(time_month_text, (240 * screen_level, 3 * screen_level))
        MainWindow.blit(time_day_text, (259 * screen_level, 3 * screen_level))

        money_text = font2.render(str(money), True, (255, 255, 255))
        MainWindow.blit(money_text, (218 * screen_level, 18 * screen_level))

        pygame.display.update()

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                speed_button_click()

                if main_button01_x <= mouse_x <= main_button01_x + main_button01_w and main_button01_y <= mouse_y <= main_button01_y + main_button01_h:
                    print('main_button01 be clicked')
                    button_click_sound.play()
                    assets_window = True
                    main_window = False

                if main_button02_x <= mouse_x <= main_button02_x + main_button02_w and main_button02_y <= mouse_y <= main_button02_y + main_button02_h:
                    print('main_button02 be clicked')
                    button_click_sound.play()
                    policy_window = True
                    main_window = False
                if main_button03_x <= mouse_x <= main_button03_x + main_button03_w and main_button03_y <= mouse_y <= main_button03_y + main_button03_h:
                    print('main_button03 be clicked')
                    button_click_sound.play()
                    personnel_window = True
                    main_window = False
                if main_button04_x <= mouse_x <= main_button04_x + main_button04_w and main_button04_y <= mouse_y <= main_button04_y + main_button04_h:
                    print('main_button04 be clicked')
                    button_click_sound.play()
                    project_window = True
                    main_window = False
                if main_button05_x <= mouse_x <= main_button05_x + main_button05_w and main_button05_y <= mouse_y <= main_button05_y + main_button05_h:
                    print('main_button05 be clicked')
                    button_click_sound.play()
                    stock_window = True
                    main_window = False

                if main_button06_x <= mouse_x <= main_button06_x + main_button06_w and main_button06_y <= mouse_y <= main_button06_y + main_button06_h:
                    print('main_button06 be clicked')
                    button_click_sound.play()
                    setting_window = True
                    main_window = False

    # === Screen Assets 屏幕 资产 ===

    elif assets_window:

        main_window = False

        MainWindow.fill((161, 136, 127))

        MainWindow.blit(assets_text1, (15 * screen_level, 1 * screen_level))
        MainWindow.blit(home_buttonFin, (3 * screen_level, 3 * screen_level))

        speed_button_display()

        pygame.display.update()

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                speed_button_click()

                if home_button_x <= mouse_x <= home_button_x + home_button_w and home_button_y <= mouse_y <= home_button_y + home_button_h:
                    print('home_button be clicked')
                    button_click_sound.play()
                    assets_window = False
                    main_window = True

    # === Screen Policy 屏幕 政策 ===

    elif policy_window:

        main_window = False

        MainWindow.fill((161, 136, 127))

        MainWindow.blit(policy_text1, (15 * screen_level, 1 * screen_level))
        MainWindow.blit(home_buttonFin, (3 * screen_level, 3 * screen_level))

        speed_button_display()

        pygame.display.update()

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                speed_button_click()

                if home_button_x <= mouse_x <= home_button_x + home_button_w and home_button_y <= mouse_y <= home_button_y + home_button_h:
                    print('home_button be clicked')
                    button_click_sound.play()
                    policy_window = False
                    main_window = True

    # === Screen Personnel 屏幕 人员 ===

    elif personnel_window:

        main_window = False

        MainWindow.fill((161, 136, 127))

        MainWindow.blit(personnel_text1, (15 * screen_level, 1 * screen_level))
        MainWindow.blit(home_buttonFin, (3 * screen_level, 3 * screen_level))

        speed_button_display()

        pygame.display.update()

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                speed_button_click()

                if home_button_x <= mouse_x <= home_button_x + home_button_w and home_button_y <= mouse_y <= home_button_y + home_button_h:
                    print('home_button be clicked')
                    button_click_sound.play()
                    personnel_window = False
                    main_window = True

    # === Screen Project 屏幕 项目 ===

    elif project_window:

        main_window = False

        MainWindow.fill((161, 136, 127))

        MainWindow.blit(project_text1, (15 * screen_level, 1 * screen_level))
        MainWindow.blit(home_buttonFin, (3 * screen_level, 3 * screen_level))

        speed_button_display()

        pygame.display.update()

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                speed_button_click()

                if home_button_x <= mouse_x <= home_button_x + home_button_w and home_button_y <= mouse_y <= home_button_y + home_button_h:
                    print('home_button be clicked')
                    button_click_sound.play()
                    project_window = False
                    main_window = True

    # === Screen Stock 屏幕 股市 ===

    elif stock_window:

        main_window = False

        if stock_stock_window == False:

            MainWindow.fill((161, 136, 127))

            MainWindow.blit(stock_text1, (15 * screen_level, 1 * screen_level))

            MainWindow.blit(home_buttonFin, (3 * screen_level, 3 * screen_level))

            MainWindow.blit(stock_boardFin, (3 * screen_level, 15 * screen_level))

            speed_button_display()

            MainWindow.blit(money_iconFin, (150 * screen_level, 5 * screen_level))
            money_text = font2.render(str(money), True, (255, 255, 255))
            MainWindow.blit(money_text, (160 * screen_level, 3 * screen_level))

            stock_stock_window = True

            pygame.display.update()

        elif stock_stock_window == True:
            if stock_stock_draw != 0:
                stock_stock_wOld = stock_stock_w
                stock_stock_w += 3

                stock_stock_hOld = stock_stock_h
                stock_stock_hd = random.randint(-15, 15)
                stock_stock_h += stock_stock_hd - stock_stock_base

                pygame.draw.line(MainWindow, (255, 255, 255), (stock_stock_wOld, stock_stock_hOld),
                                 (stock_stock_w, stock_stock_h), 1)

                pygame.display.update()

                stock_stock_draw -= 1

                time.sleep(0.1)

                pygame.display.update()

                print((-(stock_stock_h - 90 * screen_level) + 100) / 100)

                stock_variable = -(stock_stock_h - 90 * screen_level) + 100
                stock_variableFin = stock_variable / 100

                money = moneyOld * stock_variableFin
                money = int(money)
                money_text = font2.render(str(money), True, (255, 255, 255))

                pygame.draw.rect(MainWindow, (161, 136, 127),
                                 (160 * screen_level, 3 * screen_level, 50 * screen_level, 8 * screen_level), width=0)
                MainWindow.blit(money_text, (160 * screen_level, 3 * screen_level))

            else:
                print('Done')
                # stock_stock_draw = (159 * screen_level) / 3

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                speed_button_click()

                if home_button_x <= mouse_x <= home_button_x + home_button_w and home_button_y <= mouse_y <= home_button_y + home_button_h:
                    print('home_button be clicked')
                    button_click_sound.play()
                    stock_window = False
                    main_window = True
                    stock_stock_window = False


    # === Screen Setting 屏幕 设置 ===

    elif setting_window:

        main_window = False

        MainWindow.fill((161, 136, 127))

        MainWindow.blit(setting_text1, (15 * screen_level, 0 * screen_level))
        MainWindow.blit(home_buttonFin, (3 * screen_level, 3 * screen_level))

        MainWindow.blit(save_buttonFin, (screen_width - 9 * screen_level - 3 * screen_level, 3 * screen_level))

        MainWindow.blit(setting_info_barFin, (3 * screen_level, 15 * screen_level))
        MainWindow.blit(setting_info_bar2Fin, (3 * screen_level, 50 * screen_level))
        MainWindow.blit(setting_setting_barFin, (110 * screen_level, 15 * screen_level))

        #                                                           button_number v       button_number v
        MainWindow.blit(setting_button01Fin, (240 * screen_level, 15 * screen_level + 1 * 3 * screen_level + 0 * 16 * screen_level))

        pygame.display.update()

        # === 输入检测 ===

        for event in pygame.event.get():

            # === Quit 退出 ===

            if event.type == pygame.QUIT:
                exit()

            # === Button Click 按钮按下 ===

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                save_button_click()

                if home_button_x <= mouse_x <= home_button_x + home_button_w and home_button_y <= mouse_y <= home_button_y + home_button_h:
                    print('home_button be clicked')
                    button_click_sound.play()
                    setting_window = False
                    main_window = True

                if setting_button01_x <= mouse_x <= setting_button01_x + setting_button01_w and setting_button01_y <= mouse_y <= setting_button01_y + setting_button01_h:
                    print('setting_button01 be clicked')
                    button_click_sound.play()
                    #screen_level = 3
                    #screen_width = 320 * screen_level
                    #screen_height = 180 * screen_level
                    #MainWindow = pygame.display.set_mode((screen_width, screen_height))
                    MainWindow = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN | HWSURFACE )

    for event in pygame.event.get():

        # === Quit 退出 ===

        if event.type == pygame.QUIT:
            exit()
