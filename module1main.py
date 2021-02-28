import pygame, random, time
from model1 import People

k = 1


def main():
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
        if round(t1 - t0) % 5 == 0 and t != round(t1 - t0):
            l.append(k)
            t = round(t1 - t0)
    pygame.quit()


    print(l)

main()