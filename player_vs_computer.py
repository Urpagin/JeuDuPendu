import pygame
import pygame.freetype

def main(dimensions: tuple[int, int]):
    pygame.init()

    # Set up the display
    screen_width, screen_height = dimensions
    screen = pygame.display.set_mode(dimensions)

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    weird_color = (255, 0, 255)

    # Set the font and size
    font_size = 250
    font = pygame.font.SysFont(None, font_size)

    # Word to guess and current state
    word_to_guess = "PYTHON"
    current_state = ["_" for _ in word_to_guess]

    # Counter for incorrect guesses
    mistake_counter = 0

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Check if the pressed key is a letter
                if not event.unicode.isalpha():
                    continue

                if mistake_counter == 5:
                    print('RETURING')
                    running = False


                guess = event.unicode.upper()
                if guess in word_to_guess:
                    for index, letter in enumerate(word_to_guess):
                        if letter == guess:
                            current_state[index] = guess
                else:
                    mistake_counter += 1
                    # handle failure
                    if mistake_counter > 5:
                        mistake_counter = 5

        # Load and display the background image based on the mistake counter
        bg_image_path = f'../resources/gallows/gallows{mistake_counter}.png'
        bg_image = pygame.image.load(bg_image_path)
        bg_image = pygame.transform.scale(bg_image, dimensions)
        screen.blit(bg_image, (0, 0))
        if mistake_counter != 5:
            # Display the current state of the guessed word
            text_surface = font.render(' '.join(current_state), True, weird_color)
            text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text_surface, text_rect)

        if mistake_counter == 5:
            text_surface = font.render('VOUS AVEZ PERDU!', True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()

        # Update the display
        pygame.display.flip()

    pygame.quit()

