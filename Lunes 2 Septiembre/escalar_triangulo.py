import pygame

NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO = [255,255,255]
ANCHO = 600
ALTO = 400
x = -20
y = -80
tx = 300
ty = 200
origen = [tx,ty]

def plano(p):
    ox = origen[0]
    oy = origen[1]
    pygame.draw.line(pantalla,BLANCO,[ox,0],[ox,ALTO])
    pygame.draw.line(pantalla,BLANCO,[0,oy],[ANCHO,oy])
    pygame.display.flip()

def Cart_plano(pto):
    x = pto[0]
    y = pto[1]
    xp = x + origen[0]
    yp = -y + origen[1]
    return [xp,yp]

def aPant(origen, pto):
    xp=origen[0]+pto[0]
    yp=origen[1]-pto[1]
    return [xp, yp]

def Triangulo(pantalla,VERDE,puntos):
    pygame.draw.polygon(pantalla,VERDE,puntos, 1)
    pygame.display.flip()

def escala(pto,scalar):
    sx=pto[0]*scalar[0]
    sy=pto[1]*scalar[1]
    return [sx, sy]


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    plano(pantalla)
    pygame.display.flip()
    flag = 0
    ls=[]
    ls_a=[]
    ls_p=[]
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag < 3:
                    ls_p=[]
                    pygame.draw.circle(pantalla,VERDE,event.pos,2)
                    pygame.draw.circle(pantalla,VERDE,Cart_plano(event.pos),2)
                    flag+=1
                    ls.append(event.pos)

                if flag == 3:
                    for i in ls:
                        ls_p.append(Cart_plano(i))

                    Triangulo(pantalla,VERDE,ls_p)
                    flag = 0
                    ls=[]
                pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == 'space':
                    for i in ls_p:
                        print(i)
                        i = [(200+(i[0]*0.5)),(100+(i[1]*0.5))]
                        print(i)
                        ls_a.append(i)
                    Triangulo(pantalla,VERDE,ls_a)
                    ls_a=[]
                    pygame.display.flip()
