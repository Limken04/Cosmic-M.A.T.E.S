import sys
import random
import pygame
import pygame.mixer
from classes.constants import WIDTH, HEIGHT, BLACK, WHITE, RED


def animate_screen():
    """Shake animation for the screen."""
    for i in range(0, 20):
        screen.blit(mainmenu_img, (0, 0))
        pygame.display.flip()
        pygame.time.wait(10)
        screen.blit(mainmenu_img, (random.randint(-5, 5), random.randint(-5, 5)))
        pygame.display.flip()
        pygame.time.wait(10)


# Initialize Pygame and mixer
pygame.mixer.init()
pygame.init()

# Set up music and sound
pygame.mixer.music.load('game_sounds/menu.mp3')
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

explosion_sound = pygame.mixer.Sound('game_sounds/explosions/explosion1.wav')
explosion_sound.set_volume(0.25)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")
clock = pygame.time.Clock()

# Load images
mainmenu_img = pygame.image.load('images/mainmenu.jpg').convert()
mainmenu_img = pygame.transform.scale(mainmenu_img, (WIDTH, HEIGHT))

logo_img = pygame.image.load('images/ch.jpg').convert_alpha()
logo_x = (WIDTH - logo_img.get_width()) // 2
logo_y = 50

# Define buttons
play_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 205, 50)
quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 205, 50)

selected_button = 0
show_menu = True

# Initialize joystick if available
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

# Main loop
while show_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if play_button_rect.collidepoint(x, y):
                explosion_sound.play()
                animate_screen()
                show_menu = False
                # Assuming main.main() is the game's main loop
                import main
                main.main()
                break
            elif quit_button_rect.collidepoint(x, y):
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_button = 0
            elif event.key == pygame.K_DOWN:
                selected_button = 1
            elif event.key == pygame.K_RETURN:
                if selected_button == 0:
                    explosion_sound.play()
                    animate_screen()
                    show_menu = False
                    import main
                    main.main()
                    break
                elif selected_button == 1:
                    pygame.quit()
                    sys.exit()

        if joystick:
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    if selected_button == 0:
                        explosion_sound.play()
                        animate_screen()
                        show_menu = False
                        import main
                        main.main()
                        break
                    elif selected_button == 1:
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.JOYHATMOTION:
                if event.value[1] == 1:
                    selected_button = 0
                elif event.value[1] == -1:
                    selected_button = 1

    # Draw the menu screen
    screen.blit(mainmenu_img, (0, 0))
    screen.blit(logo_img, (logo_x, logo_y))

    # Draw Play button
    font = pygame.font.SysFont('Comic Sans MS', 40)
    text = font.render("Play", True, WHITE)
    pygame.draw.rect(screen, BLACK, play_button_rect, border_radius=10)
    if selected_button == 0:
        pygame.draw.rect(screen, RED, play_button_rect, border_radius=10, width=4)
    text_rect = text.get_rect(center=play_button_rect.center)
    screen.blit(text, text_rect)

    # Draw Exit button
    text = font.render("Exit", True, WHITE)
    pygame.draw.rect(screen, BLACK, quit_button_rect, border_radius=10)
    if selected_button == 1:
        pygame.draw.rect(screen, RED, quit_button_rect, border_radius=10, width=4)
    text_rect = text.get_rect(center=quit_button_rect.center)
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()