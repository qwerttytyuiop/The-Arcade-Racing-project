import pygame
import sys
import os
import random

pygame.init()
pygame.display.set_caption('')
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
podg = '0.png'
x_1c = 862
x_2c = 1058
xvs = 410
x_1o1 = 0
x_2o1 = 0
G = 0
sbr = 0
FPS = 60
cab = 0
menu1z = True
pause = False
menude = False
pause = False
run = False
Keyd = False
Keya = False
Keyw = False
Keys = False
obj = False
pp = True
per = True
s1 = True
inwul = False
broke = False
rot = 100
speed = 5
sh = 0
sp = 0
hp = 1
an1 = 0
sch = 0
S_G = 0
y_1o1 = 1000
spr1 = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png']
spr2 = ['obb1.png', 'obb2.png', 'obb3.png']
spr3 = ['obr1.png', 'obr2.png', 'obr3.png']
spr4 = ['5hp.png', '4hp.png', '3hp.png', '2hp.png', '1hp.png', '0hp.png']
k1 = [(860, 895), (875, 897), (865, 895), (865, 895), (865, 895), (865, 895)]
k2 = [(886, 895), (895, 897), (885, 895), (885, 895), (885, 895),
      (885, 895), (885, 895), (885, 895), (885, 895), (885, 895)]
k3 = [(908, 895), (915, 897), (907, 895), (907, 895), (907, 895),
      (907, 895), (907, 895), (907, 895), (907, 895), (907, 895)]


class Back:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('back.png').convert()
        self.rect = self.image.get_rect(center=(960, 930))
        self.bimage = pygame.transform.scale(self.image, (1920, 541))
        screen.blit(self.bimage, [0, 0])


back = Back()


class Road:

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('road.png')
        self.rect = self.image.get_rect(center=(960, 600))


road = Road()


class Panelm:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('panelm.png')
        self.rect = self.image.get_rect(center=(960, 930))


panelm = Panelm()


class Car:

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('car.png')
        self.rect = self.image.get_rect(center=(960, 800))


car = Car()

while running:
    if menu1z is True:
        class Menu1:
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('qwe.png').convert()
                self.rect = self.image.get_rect(center=(960, 930))
                self.bimage = pygame.transform.scale(self.image, (1920, 1080))
                screen.blit(self.bimage, [0, 0])


        menu1 = Menu1()
        ch_s = pygame.image.load('vib.png')
        ch_r = ch_s.get_rect(center=(250, xvs))
        screen.blit(ch_s, ch_r)

        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu1z = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if xvs == 956:
                        xvs = 750
                    if xvs > 410:
                        xvs -= 68
                    else:
                        xvs = 956
                if event.key == pygame.K_s:
                    if xvs == 956:
                        xvs = 342
                    if xvs < 682:
                        xvs += 68
                    else:
                        xvs = 956
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if xvs == 410:
                        xvs = 750
                        menu2z = True
                        menu1z = False
                    if xvs == 956:
                        running = False

    else:
        if menude is True:
            ch_s = pygame.image.load('ded.png')
            ch_r = ch_s.get_rect(center=(960, 540))
            screen.blit(ch_s, ch_r)
            ch_s = pygame.image.load('vib2.png')
            ch_r = ch_s.get_rect(center=(xvs, 707))
            screen.blit(ch_s, ch_r)
            clock.tick(FPS)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        if xvs == 750:
                            xvs = 1168
                        else:
                            xvs = 750
                    if event.key == pygame.K_a:
                        if xvs == 750:
                            xvs = 1168
                        else:
                            xvs = 750
                    if event.key == pygame.K_f:
                        if xvs == 1168:
                            car.rect.x = 862
                            inwul = False
                            hp = 5
                            speed = 5
                            G = 0
                            S_G = 0
                            menu1z = True
                            menude = False
                        if xvs == 750:
                            inwul = False
                            car.rect.x = 862
                            hp = 5
                            speed = 5
                            G = 0
                            S_G = 0
                            menude = False
        else:
            if pause is True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            pause = False
            else:
                class Object:
                    def __init__(self):
                        pygame.sprite.Sprite.__init__(self)
                        self.image = pygame.image.load(podg)
                        self.rect = self.image.get_rect(center=(x_1o1, y_1o1))


                object = Object()

                screen.blit(back.image, back.rect)
                back.rect.x = 0
                back.rect.y = 0
                po = random.randint(0, 1000)
                if pp is True:
                    x_1o1 = po
                if 100 < po < 300 and pp is True:
                    sp = random.randint(0, 2)
                    rot = random.randint(0, 1)
                    cord = random.randint(700, 1200)
                    pp = False
                    screen.blit(object.image, object.rect)
                    x_1o1 = cord
                    x_2o1 = cord + 98
                    if rot == 0:
                        podg = spr2[sp]
                    else:
                        podg = spr3[sp]
                if rot == 0 and s1 is True:
                    if y_1o1 > 400:
                        y_1o1 -= speed
                    else:
                        s1 = False
                    screen.blit(object.image, object.rect)
                if rot == 1 and s1 is True:
                    if y_1o1 > 400:
                        y_1o1 -= speed * 2
                    else:
                        s1 = False
                    screen.blit(object.image, object.rect)
                sch += 1
                if sch == 180:
                    inwul = False
                    sch = 0
                if 250 <= car.rect.x + G <= 1430:
                    car.rect.x += G
                    x_1c = car.rect.x
                    x_2c = car.rect.x + 196
                else:
                    G = 0
                screen.blit(road.image, road.rect)
                sh += 1 + speed * 0.01
                if sh <= 10:
                    ch_s = pygame.image.load('pol1.png')
                    ch_r = ch_s.get_rect(center=(960, 825))
                    screen.blit(ch_s, ch_r)
                    ch_s = pygame.image.load('light1.png')
                    ch_r = ch_s.get_rect(center=(1800, 825))
                    screen.blit(ch_s, ch_r)
                    ch_s = pygame.image.load('light2.png')
                    ch_r = ch_s.get_rect(center=(120, 825))
                    screen.blit(ch_s, ch_r)
                    ch_s = pygame.image.load('light1.png')
                    ch_r = ch_s.get_rect(center=(1400, 425))
                    screen.blit(ch_s, ch_r)
                    ch_s = pygame.image.load('light2.png')
                    ch_r = ch_s.get_rect(center=(520, 425))
                    screen.blit(ch_s, ch_r)
                else:
                    if sh <= 20:
                        ch_s = pygame.image.load('pol2.png')
                        ch_r = ch_s.get_rect(center=(960, 810))
                        screen.blit(ch_s, ch_r)
                        ch_s = pygame.image.load('light1.png')
                        ch_r = ch_s.get_rect(center=(1600, 625))
                        screen.blit(ch_s, ch_r)
                        ch_s = pygame.image.load('light2.png')
                        ch_r = ch_s.get_rect(center=(320, 625))
                        screen.blit(ch_s, ch_r)
                    else:
                        ch_s = pygame.image.load('pol1.png')
                        ch_r = ch_s.get_rect(center=(960, 825))
                        screen.blit(ch_s, ch_r)
                        sh = sh * 0
                if rot == 0 and s1 is False:
                    if cord >= 960:
                        y_1o1 += speed
                        x_1o1 += speed
                        x_2o1 += speed
                        screen.blit(object.image, object.rect)
                    else:
                        y_1o1 += speed
                        x_1o1 -= speed
                        x_2o1 -= speed
                        screen.blit(object.image, object.rect)
                    if y_1o1 > 1200:
                        y_1o1 = 1100
                        s1 = True
                        pp = True
                if rot == 1 and s1 is False:
                    if cord >= 960:
                        y_1o1 += speed * 2
                        x_1o1 += speed * 2
                        x_2o1 += speed * 2
                        screen.blit(object.image, object.rect)
                    else:
                        y_1o1 += speed * 2
                        x_1o1 -= speed * 2
                        x_2o1 -= speed * 2
                        screen.blit(object.image, object.rect)
                    if y_1o1 > 1200:
                        y_1o1 = 1100
                        s1 = True
                        pp = True
                if 780 < object.rect.y < 820 and s1 is False and (
                        x_1o1 - 98 <= x_1c <= x_2o1 or x_1o1 - 98 <= x_2c <= x_2o1) and inwul is False:
                    S_G = 0
                    if speed - 10 > 0:
                        speed -= 10
                    if inwul is False:
                        hp -= 1
                    inwul = True
                if hp == 0:
                    menude = True

                if inwul is False:
                    screen.blit(car.image, car.rect)
                if inwul is True and an1 <= 10:
                    screen.blit(car.image, car.rect)
                    an1 += 1
                if inwul is True and an1 > 10:
                    an1 += 1
                if an1 == 21:
                    an1 = 0
                screen.blit(panelm.image, panelm.rect)
                kmph = speed * 10
                kmph = round(kmph)
                if kmph < 100:
                    kmph = '0' + str(kmph)
                kmph = list(str(kmph))
                ci1 = int(kmph[0])
                ci2 = int(kmph[1])
                ci3 = int(kmph[2])
                ch_s = pygame.image.load(spr1[ci1])
                ch_r = ch_s.get_rect(center=k1[ci1])
                screen.blit(ch_s, ch_r)
                ch_s = pygame.image.load(spr1[ci2])
                ch_r = ch_s.get_rect(center=k2[ci2])
                screen.blit(ch_s, ch_r)
                ch_s = pygame.image.load(spr1[ci3])
                ch_r = ch_s.get_rect(center=k3[ci3])
                screen.blit(ch_s, ch_r)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            Keyd = True
                        if event.key == pygame.K_a:
                            Keya = True
                        if event.key == pygame.K_w:
                            Keyw = True
                        if event.key == pygame.K_p:
                            if pause is False:
                                pause = True
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                            Keyd = False
                        if event.key == pygame.K_a:
                            Keya = False
                        if event.key == pygame.K_w:
                            Keyw = False
                if Keyd is True:
                    if G < 10:
                        G += 0.5
                if Keya is True:
                    if G > -10:
                        G -= 0.5
                if Keyw is True and S_G + 0.01 < 0.08:
                    S_G += 0.0005
                if S_G - 0.0003 > 0:
                    S_G -= 0.0003
                speed += S_G
                if broke is False:
                    ch_s = pygame.image.load('tah_p.png')
                    ch_r = ch_s.get_rect(center=(875, 1030))
                    screen.blit(ch_s, ch_r)
                if S_G > 0.01:
                    ch_s = pygame.image.load('tah1.png')
                    ch_r = ch_s.get_rect(center=(930, 1028))
                    screen.blit(ch_s, ch_r)
                if S_G > 0.02:
                    ch_s = pygame.image.load('tah2.png')
                    ch_r = ch_s.get_rect(center=(947, 1022))
                    screen.blit(ch_s, ch_r)
                if S_G > 0.03:
                    ch_s = pygame.image.load('tah3.png')
                    ch_r = ch_s.get_rect(center=(991, 1018))
                    screen.blit(ch_s, ch_r)
                if S_G > 0.05:
                    ch_s = pygame.image.load('tah4.png')
                    ch_r = ch_s.get_rect(center=(1010, 1000))
                    screen.blit(ch_s, ch_r)
                if S_G > 0.06:
                    ch_s = pygame.image.load('tah5.png')
                    ch_r = ch_s.get_rect(center=(1040, 1000))
                    screen.blit(ch_s, ch_r)
                    cab += 1
                else:
                    if broke is False:
                        cab = 0
                if cab == 180:
                    broke = True
                    S_G = -0.001
                    cab = 0
                if broke is True:
                    cab += 1
                    if cab == 120:
                        broke = False
                        cab = 0
                if hp == 5:
                    ch_s = pygame.image.load('full.png')
                    ch_r = ch_s.get_rect(center=(1750, 10))
                    screen.blit(ch_s, ch_r)
                else:
                    if 2 < hp < 5:
                        ch_s = pygame.image.load('litt.png')
                        ch_r = ch_s.get_rect(center=(1750, 10))
                        screen.blit(ch_s, ch_r)
                    else:
                        ch_s = pygame.image.load('fuc.png')
                        ch_r = ch_s.get_rect(center=(1750, 10))
                        screen.blit(ch_s, ch_r)
                ch_s = pygame.image.load('pereg.png')
                if 1030 - cab > 990 and broke is False and cab != 0:
                    ch_r = ch_s.get_rect(center=(1138, 1030 - cab))
                    sbr = 0
                if 1030 - cab < 990 and broke is False and cab != 0:
                    ch_r = ch_s.get_rect(center=(1138, 990))
                    sbr = 0
                if broke is True or cab == 0:
                    sbr += 1
                    if 990 + sbr < 1030:
                        ch_r = ch_s.get_rect(center=(1138, 990 + sbr))
                    else:
                        ch_r = ch_s.get_rect(center=(1138, 1030))

                screen.blit(ch_s, ch_r)
                ch_s = pygame.image.load(spr4[5 - hp])
                ch_r = ch_s.get_rect(center=(1770, 180))
                screen.blit(ch_s, ch_r)
                clock.tick(FPS)
                pygame.display.update()
