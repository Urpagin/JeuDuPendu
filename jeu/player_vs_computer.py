import json
import random
import time

import nltk  # Natural Language Toolkit
import pygame
import pygame.freetype
from nltk.corpus import cmudict

from qt_guis.new_game_settings import widget

# Ensure you have the necessary NLTK data
nltk.download('cmudict')

# Prepare a dictionary for syllable count lookup
d = cmudict.dict()


def syllable_count(word):
    """Return the number of syllables in a word."""
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]


def categorize_word(word: str) -> int:
    """Categorize a word based on length and syllable count."""
    try:
        syllables = syllable_count(word)
    except KeyError:
        # If the word is not found in the cmudict, approximate by word length
        syllables = len(word) // 3

    length = len(word)

    if length <= 4 or syllables == 1:
        return 0
    elif 4 < length <= 7:
        return 1
    elif 7 < length <= 10 or 1 < syllables <= 3:
        return 2
    else:
        return 3


def main(dimensions: tuple[int, int]):
    widget.run_ui()

    # Set up the display
    screen_width, screen_height = dimensions
    screen = pygame.display.set_mode(dimensions)

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    weird_color = (255, 0, 255)

    # Set the font and size
    font_size = 100
    font = pygame.font.SysFont(None, font_size)

    # Word to guess and current state
    # word_to_guess = "PYTHON"
    flag = True

    with open('info.json', 'r', encoding='utf-8') as f:
        data: json = json.load(f)
        player_name: str = data['player_name']
        difficulty: int = data['difficulty']
        language: str = data['language']

    print(player_name, difficulty, language)

    word_to_guess: str = get_random_word_v2(language=language, difficulty=difficulty).upper().strip().replace(' ', '')
    print(word_to_guess)

    #if language == 'Anglais':
    #    words_file: str = ''

    #with open('language.txt', 'r', encoding='utf-8') as f:
    #    for i in f:
    #        if language == 'Anglais':
    #            word_to_guess: str = get_random_word(1).upper().strip().replace(' ', '')
    #        else:
    #            word_to_guess: str = get_random_word().upper().strip().replace(' ', '')

    # TODO DELETE !!!!!!!
    #word_to_guess = "ABC"

    current_state = ["_" for _ in word_to_guess]
    print(word_to_guess)

    # Counter for incorrect guesses
    mistake_counter = 0

    # Main loop
    running = True
    player_win = False
    flag2 = False
    while running:
        # If player won
        if '_' not in current_state:
            bg_image_path = f'../resources/win.jpeg'
            bg_image = pygame.image.load(bg_image_path)
            bg_image = pygame.transform.scale(bg_image, dimensions)
            screen.blit(bg_image, (0, 0))

            print('PLAYER WON')
            if player_name:
                text_surface = font.render(f'BRAVO, {player_name}, VOUS AVEZ GAGNEZ!', True, (255, 0, 0))
            else:
                text_surface = font.render(f'BRAVO VOUS AVEZ GAGNEZ!', True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            time.sleep(5)
            running = False

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
            text_surface = font.render(f'VOUS AVEZ PERDU! ({word_to_guess})', True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()

        # Update the display
        pygame.display.flip()


def get_random_word(e=0) -> str:
    if e == 0:
        with open('../resources/words.txt', 'r', encoding='utf-8') as f:
            words: list[str] = f.readlines()
            return random.choice(words)
    else:
        with open('../resources/english.txt', 'r', encoding='utf-8') as f:
            words: list[str] = f.readlines()
            return random.choice(words)


def get_random_word_v2(language: str, difficulty: int) -> str:
    words: list[str] = []
    if language == 'Anglais':
        with open('../resources/english.txt', 'r', encoding='utf-8') as f:
            for word in f:
                words.append(word)
            random.shuffle(words)
            for word in words:
                if categorize_word(word) == difficulty:
                    return word
    else:
        with open('../resources/words.txt', 'r', encoding='utf-8') as f:
            for word in f:
                words.append(word)
            random.shuffle(words)
            for word in words:
                if categorize_word(word) == difficulty:
                    return word


if __name__ == '__main__':
    print(categorize_word('parfait'))
