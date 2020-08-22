import pygame
import random
import os
import numpy as np
import math


# Setting display variables
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 500

win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("HANGMAN!")

# defining button variables
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400
A = 65


for i in range(26):
    x =  start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y =  start_y + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


# creating of fonts
LETTER_FONT = pygame.font.SysFont('yumin', 20)
WORD_FONT = pygame.font.SysFont('yumin', 45)
TITLE_FONT = pygame.font.SysFont('yumin', 65)

# loading hangman image files
images = []

# indexing between 1-7 because list is 1-6 length and 7 isn't inclusive 
for i in range(7):
    image = pygame.image.load(os.path.join("hangman", "hangman" + str(i) + ".png"))
    images.append(image)

# setting up game variables
hangman_status = 0
word = str(input("please select a word to be guessed: ").upper()) #note: This Word Needs To Be in Caps
guessed = []



# Colors variables
WHITE = (255,255,255)
BLACK = (0,0,0)


# setting up gameplay loop
FPS = 60

clock = pygame.time.Clock()

run = True

def draw():
    win.fill(BLACK)

    # code for drawing title
    text = TITLE_FONT.render("HANGMAN", 1, WHITE)
    win.blit(text, (WIDTH/2, 50))

    # code for drawing words
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text =  WORD_FONT.render(display_word, 1, WHITE)
    win.blit(text, (400, 200))

    

    # code for drawing buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, WHITE, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, WHITE)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))


    win.blit(images[hangman_status], (150,100))
    pygame.display.update()


# end screen message display function
def display_endscreen(message):
    pygame.time.delay(1000)
    win.fill(BLACK)
    text = WORD_FONT.render(message, 1, WHITE)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 - 100))
    pygame.display.update()

def display_endimage(num):
    image = pygame.image.load(os.path.join("hangman", "hangman" + str(num) + ".png"))
    win.blit(image, (WIDTH/2 - 55, 200))
    pygame.display.update()
    pygame.time.delay(2000)






# While GameLoop is Running 
while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1


    won = True                        
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_endscreen("You Won!!!")
        display_endimage("0")

        break
 
    if hangman_status == 6:
        display_endscreen("You Lost!!!")
        display_endimage("6")
        break


pygame.quit()






