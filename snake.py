#pylint: disable-all

import pygame
import time
import math
import random

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (196,247,160)
RED = (209, 20, 20)

random.seed()

class Board():
    def __init__(self, snake, color, width, height, surface):
        self.snake = snake
        self.color = color
        self.width = width
        self.height = height
        self.offset = 50
        self.surface = surface
        self.gridX = 20
        self.gridY = 20
        self.grid = [[0 for _ in range(self.gridY)] for _ in range(self.gridX)]
        self.tileSize = ((self.width - 2 * self.offset) // self.gridX, (self.height - 2 * self.offset) // self.gridY)
        self.food = None
        self.score = -1
        self.speed = 1

    def drawBoard(self):
        pygame.draw.rect(self.surface, BLACK, [self.offset - 2, self.offset - 2, self.width - 2 * (self.offset - 2),
                                                 self.height - 2 * (self.offset - 2)])
        pygame.draw.rect(self.surface, self.color, [self.offset, self.offset, self.width - 2 * (self.offset),
                                                 self.height - 2 * (self.offset)])
        self.newFood(self.snake)

    def drawSnake(self):
        self.snake.drawSnake(self.offset, self.tileSize[0], self.tileSize[1], self)

    def newFood(self, snake):
        food = (random.randint(1,19), random.randint(1,19))
        while food in snake.bodyGrid:
            food = (random.randint(1,19), random.randint(1,19))
        self.food = food
        self.score += 1
        self.speed += 1
        self.drawFood()

    def drawFood(self):
        text = "SCORE: " + str(self.score)
        putText(text, 30, BOARD_HEIGHT - TEXT_SIZE - 10, GREEN, TEXT_SIZE, surface)
        newCoord = (self.offset + self.food[0] * self.tileSize[0], self.offset + self.food[1] * self.tileSize[1])
        pygame.draw.rect(surface, RED, [newCoord[0] + 2, newCoord[1] + 2, self.tileSize[0] - 4, self.tileSize[1] - 4])

class Snake():
    def __init__(self):
        self.initiated = 0
        self.color = BLACK
        self.length = 3
        self.head = (10,10)
        self.direction = (1,0)
        self.bodyGrid = [self.head]

    def drawSnake(self, offset, width, height, board):
        if self.initiated == 0:
            for newX, newY in self.bodyGrid:
                newCoord = (offset + newX * width, offset + newY * height)
                pygame.draw.rect(surface, BLACK, [newCoord[0] + 2, newCoord[1] + 2, width - 4, height-4])
            self.initiated = 1 

        self.nextSnake()
        if self.head in self.bodyGrid[1:]:
            pygame.quit()
            quit()
        elif not self.head == board.food:
            oldX, oldY = self.bodyGrid.pop()
            oldCoord = (offset + oldX * width, offset + oldY * height)
            pygame.draw.rect(surface, GREEN, [oldCoord[0] + 2, oldCoord[1] + 2, width-4, height-4])
        else:
            board.newFood(self)

        newCoord = (offset + self.head[0] * width, offset + self.head[1] * height)
        pygame.draw.rect(surface, BLACK, [newCoord[0] + 2, newCoord[1] + 2, width - 4, height-4]) 

    def nextSnake(self):
        self.head = ((self.head[0] + self.direction[0]) % 20, (self.head[1] + self.direction[1]) % 20)
        self.bodyGrid.insert(0, self.head)     

def putText(text, x, y, bg, size, surface):
    font = pygame.font.Font('freesansbold.ttf', size)
    textSurface = font.render(text, True, BLACK, bg)
    textRect = textSurface.get_rect()
    textRect.x = x
    textRect.y = y
    surface.blit(textSurface, textRect)

BOARD_WIDTH = 600
BOARD_HEIGHT = 600
TEXT_SIZE = 20

DIRECTIONS = {'right':(1,0), 'down':(0,1), 'left':(-1,0), 'up':(0,-1)}

pygame.init()
clock = pygame.time.Clock()

surface = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
surface.fill(GREEN)
pygame.display.set_caption('Snake')

snake = Snake()
board = Board(snake, GREEN, BOARD_WIDTH, BOARD_HEIGHT, surface)

board.drawBoard()
# putText("SCORE: ", 30, BOARD_HEIGHT - TEXT_SIZE - 10, GREEN, TEXT_SIZE, surface)


while True:
    for event in pygame.event.get():
        # if page is closed, quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # check if key down is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake.direction is not DIRECTIONS['right']:
                    snake.direction = DIRECTIONS['left']
            if event.key == pygame.K_RIGHT:
                if snake.direction is not DIRECTIONS['left']:
                    snake.direction = DIRECTIONS['right']
            if event.key == pygame.K_UP:
                if snake.direction is not DIRECTIONS['down']:
                    snake.direction = DIRECTIONS['up']
            if event.key == pygame.K_DOWN:
                if snake.direction is not DIRECTIONS['up']:
                    snake.direction = DIRECTIONS['down']
        
    board.drawSnake()
    pygame.display.update()
    clock.tick(board.speed)


