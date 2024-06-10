import pygame
import pygame
import sys

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Screen Example")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Main menu screen
def main_menu():
    screen.fill(WHITE)
    # Draw main menu elements
    pygame.draw.rect(screen, RED, (100, 500, 200, 100))
    pygame.display.flip()

# Game screen
def game_screen():
    screen.fill(BLACK)
    # Draw game elements
    pygame.draw.rect(screen, GREEN, (300, 200, 200, 100))
    pygame.display.flip()

# Main loop
def main():
    current_screen = main_menu  # Start with the main menu screen

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Switch to game screen when space key is pressed
                    current_screen = game_screen
        
        # Call the current screen function
        current_screen()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
