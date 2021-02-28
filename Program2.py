import pygame, random, time
import pylab as plt
from model1 import People
from module2 import People1

k = 1


def main():
    list=animate()
    l23=animate2()
    if len(list)==20 and len(l23)==20:
        graphing(list,l23)



def graphing(list,l23):


    t = [i for i in range(1, 21)]
    plt.figure('Graph 1')
    plt.xlabel('Time')
    plt.ylabel('Active Cases')
    plt.title('Spread of the Virus')
    plt.plot(t, list, 'r-', label='No precautions taken')
    plt.plot(t, l23, 'b-', label='With precautions')
    plt.legend(loc='upper right')
    plt.interactive(False)
    plt.show()

def animate():
    t0=time.process_time()
    t = 0
    l = []
    global k
    pygame.init()
    WIDTH = HEIGHT = 800
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Virus Simulation without precautions (grey is susceptible, red infected, green is recovered, black is dead)")
    screen.fill(pygame.Color("white"))
    p0 = People(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "infected", False)
    no_p = 350 - 1
    peoples = [p0]

    for i in range(no_p):
        if i < no_p / 4:
            peoples.append(People(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "susceptible", False))
        else:
            peoples.append(People(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "susceptible", False))

    clock = pygame.time.Clock()
    fps = 30
    runtime = True
    while runtime:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtime = False
            if len(l)==19:
                runtime=False

        for i in range(no_p):
            k = peoples[i].updation(screen, peoples)
        screen.fill(pygame.Color("white"))
        for i in range(no_p):
            peoples[i].draw(screen)
        # t1 = time.clock()
        # p0.draw(screen)
        pygame.display.flip()

        clock.tick(fps)


        t1=time.process_time()
        if round(t1 - t0) % 3 == 0 and t != round(t1 - t0) and len(l)<=19:
            l.append(k)
            t = round(t1 - t0)
    pygame.quit()


    return l

def animate2():
    t0=time.process_time()
    t = 0
    l = []
    global k
    pygame.init()
    WIDTH = HEIGHT = 800
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Virus Simulation with precautions  (grey is susceptible, red infected, green is recovered, black is dead)")
    screen.fill(pygame.Color("white"))
    p0 = People1(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "infected", False)
    no_p = 350 - 1
    peoples = [p0]

    for i in range(no_p):
        if i < no_p / 20:
            peoples.append(People1(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "susceptible", False))
        else:
            peoples.append(People1(random.randint(5, WIDTH - 5), random.randint(5, HEIGHT - 5, ), "susceptible", True))

    clock = pygame.time.Clock()
    fps = 30
    runtime = True
    while runtime:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtime = False

        for i in range(no_p):
            k = peoples[i].updation1(screen, peoples)
        screen.fill(pygame.Color("white"))
        for i in range(no_p):
            peoples[i].draw1(screen)
        # t1 = time.clock()
        # p0.draw(screen)
        pygame.display.flip()

        clock.tick(fps)

        t1 = time.process_time()
        if round(t1 - t0) % 3 == 0 and t != round(t1 - t0) and len(l)<=19:
            l.append(k)
            t = round(t1 - t0)
    pygame.quit()


    return l

main()

