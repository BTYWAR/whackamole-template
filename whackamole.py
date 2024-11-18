import pygame
import random

def main():
    try:
        pygame.init()
        screen_width, screen_height = 640, 512
        grid_size = 32
        rows, cols = screen_height // grid_size, screen_width // grid_size

        mole_image = pygame.image.load("mole.png")
        mole_position = [0,0]

        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_x, mole_y = mole_position[0] * grid_size, mole_position[1] * grid_size
                    if mole_x <= mouse_x < mole_x + grid_size and mole_y <= mouse_y < mole_y + grid_size:
                        mole_position[0] = random.randrange(0, cols)
                        mole_position[1] = random.randrange(0, rows)

            screen.fill("light green")

            for x in range(0, screen_width, grid_size):
                pygame.draw.line(screen, "dark blue", (x, 0), (x, screen_height))
            for y in range(0, screen_height, grid_size):
                pygame.draw.line(screen, "dark blue", (0, y), (screen_width, y))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_position[0] * grid_size, mole_position[1] * grid_size)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
