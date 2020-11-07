import pygame
import math

n=int(input('Enter the size of playing grid: '))

pygame.init()


prozor_sirina=900
prozor_visina=900
prozor=pygame.display.set_mode((prozor_sirina,prozor_visina))

BLACK =(100,100, 100)
RED=(255,0,0)

ikona=pygame.image.load('ikona.png')
pygame.display.set_icon(ikona)

pygame.display.set_caption('Krizic kruzic')

tabla=[[0 for _ in range(n)] for i in range(n)]



krizic_slika=pygame.image.load('krizic.png')
krizic_slika=pygame.transform.scale(krizic_slika,(int(prozor_sirina/n),int(prozor_visina/n)))

kruzic_slika=pygame.image.load('kruzic.png')
kruzic_slika=pygame.transform.scale(kruzic_slika,(int(prozor_sirina/n),int(prozor_visina/n)))

potez='x'

def isctaj_pozadinu():
    prozor.fill((75,125,255))

    for i in range(1,n):
        pygame.draw.line(prozor,(0,0,0),((prozor_sirina/n)*i,0),((prozor_sirina/n)*i,prozor_visina),int((prozor_sirina/n)/7.5))
        pygame.draw.line(prozor,(0,0,0),(0,(prozor_visina/n)*i),(prozor_sirina,(prozor_visina/n)*i),int((prozor_visina/n)/7.5))

    #pygame.display.update()

def iscrtaj_prozor():
    global tabla

    isctaj_pozadinu()

    for i in range(n):
        for j in range(n):
            if tabla[i][j]=='x':
                prozor.blit(krizic_slika, (i*(prozor_sirina/n), j*(prozor_visina/n)))
            elif tabla[i][j]=='o':
                prozor.blit(kruzic_slika, (i*(prozor_sirina/n), j*(prozor_visina/n)))

    pygame.display.update()

def indeksi_pobjede(n):

    for r in range(n):
        yield [(r, k) for k in range(n)]

    for k in range(n):
        yield [(r, k) for r in range(n)]

    yield [(i, i) for i in range(n)]

    yield [(i, n-1-i) for i in range(n)]

def provjeri_kraj(tabla,potez):
    global kord_linije
    tabla_dim=len(tabla)
    for indeksi in indeksi_pobjede(tabla_dim):
        if all(tabla[r][k]==potez  for r,k in indeksi):
            
            kord_linije=indeksi

            return True

    return False

def reset():
    global tabla
    global potez

    potez='x'

    tabla=[[0 for _ in range(n)] for i in range(n)]

def slobodno(x,y):
    x=math.floor(x/(prozor_sirina/n))
    y=math.floor(y/(prozor_visina/n))
    if tabla[x][y]==0:
        return True
    else:
        return False

def odigraj(x,y):
    global tabla
    x=math.floor(x/(prozor_sirina/n))
    y=math.floor(y/(prozor_visina/n))
    tabla[x][y]=potez

def kraj():
    iscrtaj_prozor()
    pygame.time.delay(1)
    pygame.display.update()

    pygame.draw.line(prozor,BLACK,linija(kord_linije)[0],linija(kord_linije)[1],int((prozor_sirina/n)/7.5))


    tekst2='Press any key'
    tekst3='to continue'

    font2=pygame.font.SysFont("monospace", 50)

    oznaka2=font2.render(tekst2,1,RED )
    oznaka3=font2.render(tekst3,1,RED)

    prozor.blit(oznaka2,(prozor_sirina / 2 - oznaka2.get_width() / 2, 350))
    prozor.blit(oznaka3,(prozor_sirina / 2 - oznaka3.get_width() / 2, 420))

    pygame.display.update()

    ponovno=True
    while ponovno:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                ponovno = False
    reset()    

def kraj_nerijeseno():
    iscrtaj_prozor()
    pygame.time.delay(1)
    pygame.display.update()


    tekst='Tie!'
    tekst2='Press any key'
    tekst3='to continue'

    font=pygame.font.SysFont("monospace", 50,True)
    font2=pygame.font.SysFont("monospace", 50)

    oznaka=font.render(tekst, 1, RED)
    oznaka2=font2.render(tekst2,1,RED)
    oznaka3=font2.render(tekst3,1,RED)

    prozor.blit(oznaka,(prozor_sirina / 2 - oznaka.get_width() / 2, 150))
    prozor.blit(oznaka2,(prozor_sirina / 2 - oznaka2.get_width() / 2, 350))
    prozor.blit(oznaka3,(prozor_sirina / 2 - oznaka3.get_width() / 2, 420))
    pygame.display.update()

    

    ponovno=True
    while ponovno:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                ponovno = False
    reset()


def linija(kord_linije):
    kordinate=[[None,None],[None,None]]
    kordinate[0][0]=kord_linije[0][0]*((prozor_sirina)/n)+((prozor_sirina)/(n*2))
    kordinate[0][1]=kord_linije[0][1]*((prozor_visina)/n)+((prozor_visina)/(n*2))
    kordinate[1][0]=kord_linije[-1][0]*((prozor_sirina)/n)+((prozor_sirina)/(n*2))
    kordinate[1][1]=kord_linije[-1][1]*((prozor_visina)/n)+((prozor_visina)/(n*2))
    if kord_linije[0][0]<kord_linije[-1][0]:
        kordinate[0][0]-=(prozor_sirina/n)*0.3
        kordinate[1][0]+=(prozor_sirina/n)*0.3
    if kord_linije[0][1]<kord_linije[-1][1]:
        kordinate[0][1]-=(prozor_visina/n)*0.3
        kordinate[1][1]+=(prozor_visina/n)*0.3
    elif kord_linije[0][1]>kord_linije[-1][1]:
        kordinate[0][1]+=(prozor_visina/n)*0.3
        kordinate[1][1]-=(prozor_visina/n)*0.3

    return kordinate


u_igri=True

while u_igri:
    iscrtaj_prozor()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            u_igri=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                u_igri=False
        if event.type==pygame.MOUSEBUTTONDOWN: 
            poz_klika=pygame.mouse.get_pos()
            if slobodno(poz_klika[0],poz_klika[1]):
                odigraj(poz_klika[0],poz_klika[1])
                if provjeri_kraj(tabla,potez):
                    kraj()
                elif sum(red.count(0) for red in tabla)==0:
                    kraj_nerijeseno()
                else:
                    if potez=='x': 
                        potez='o'
                    else: potez='x'


pygame.quit()

