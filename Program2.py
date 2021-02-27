import pygame, random, time
import numpy as np
import pylab as plt
from model1 import People

k = 1


def main():
    list=animate()
    print (list)
    if len(list)==14:
        graphing(list)



def graphing(list):
    x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    y=[1,2,3,4,5,6,7]


    t = [i for i in range(1, 15)]
    plt.figure('Graph 1')
    plt.xlabel('Time')
    plt.ylabel('Active Cases')
    plt.title('Spread of the Virus')
    plt.plot(t, list, 'r-', label='No precautions taken')
    #plt.plot(t, cases2, 'b-', label='With precautions')
    plt.legend(loc='upper right')
    plt.interactive(False)
    plt.show()

def animate():
    t0 = time.clock()
    t = 0
    l = []
    global k
    pygame.init()
    WIDTH = HEIGHT = 800
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Virus Simulation")
    screen.fill(pygame.Color("white"))
    p0 = People(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "infected", False)
    no_p = 350 - 1
    peoples = [p0]

    for i in range(no_p):
        if i < no_p / 2:
            peoples.append(People(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "susceptible", False))
        else:
            peoples.append(People(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "susceptible", True))

    clock = pygame.time.Clock()
    fps = 30
    runtime = True
    while runtime:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtime = False

        for i in range(no_p):
            k = peoples[i].updation(screen, peoples)
        screen.fill(pygame.Color("white"))
        for i in range(no_p):
            peoples[i].draw(screen)
        # t1 = time.clock()
        # p0.draw(screen)
        pygame.display.flip()

        clock.tick(fps)

        t1 = time.clock()
        if round(t1 - t0) % 5 == 0 and t != round(t1 - t0) and len(l)<=13:
            l.append(k)
            t = round(t1 - t0)
    pygame.quit()


    return l

main()
