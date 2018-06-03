import os, sys, pygame


def main():
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Game')

    try:
        filename = os.path.join(
            os.path.dirname(__file__),
            'assets',
            'graphics',
            'background.png').replace('/', '\\')
        background = pygame.image.load(filename)
        background = background.convert()
    except pygame.error as e:
        print('Cannot load image: ', filename)
        raise SystemExit(str(e))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
