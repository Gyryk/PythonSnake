# Import Libraries
import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

font = pygame.font.Font('DejaVuSerif.ttf', 32)

# Store Direction as set of preset values
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


# Constants
point = namedtuple('point', ['x', 'y'])
BLOCK_SIZE = 16
# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
LIME = (200, 255, 0)
CYAN = (0, 155, 200)
CRIMSON = (155, 0, 50)
DARK_GREEN = (5, 100, 60)
BROWN = (150, 75, 0)

global speed
speed = 10

class snakeGame:
    def __init__(self, w=1280, h=960):
        self.w = w
        self.h = h

        # Initialise Display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Basic Game of Snake :)")
        self.clock = pygame.time.Clock()

        self.reset()

    # Restart game instead of closing window
    def reset(self):
        global speed

        # Draw Horizontal Walls
        for block in range(0, 1280, BLOCK_SIZE):
            pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(block, 0, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BROWN, pygame.Rect(block + random.randint(0, 4), random.randint(0, 8),
                                                              random.randint(1, 4), random.randint(1, 6)))
            pygame.draw.rect(self.display, BROWN, pygame.Rect(block + random.randint(8, 12), random.randint(0, 8),
                                                              random.randint(1, 4), random.randint(1, 6)))

            pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(block, 960 - BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BROWN, pygame.Rect(block + random.randint(0, 4), 960 - random.randint(6, 14),
                                                              random.randint(1, 4), random.randint(1, 6)))
            pygame.draw.rect(self.display, BROWN,
                             pygame.Rect(block + random.randint(8, 12), 960 - random.randint(6, 14),
                                         random.randint(1, 4), random.randint(1, 6)))

        # Draw Vertical Walls
        for block in range(0, 960, BLOCK_SIZE):
            pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(0, block, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BROWN, pygame.Rect(random.randint(0, 4), block + random.randint(0, 8),
                                                              random.randint(1, 4), random.randint(1, 6)))
            pygame.draw.rect(self.display, BROWN, pygame.Rect(random.randint(8, 12), block + random.randint(0, 8),
                                                              random.randint(1, 4), random.randint(1, 6)))

            pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(1280 - BLOCK_SIZE, block, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BROWN,
                             pygame.Rect(1280 - random.randint(10, 14), block + random.randint(0, 8),
                                         random.randint(1, 4), random.randint(1, 6)))
            pygame.draw.rect(self.display, BROWN,
                             pygame.Rect(1280 - random.randint(10, 14), block + random.randint(0, 8),
                                         random.randint(1, 4), random.randint(1, 6)))

        # Initialise Game with starting variables
        self.direction = Direction.RIGHT
        self.head = point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      point(self.head.x - BLOCK_SIZE, self.head.y),
                      point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()

        speed = 10

    # Place food in valid pixels
    def _place_food(self):
        x = random.randint(BLOCK_SIZE, (self.w-BLOCK_SIZE*2)//BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(BLOCK_SIZE, (self.h-BLOCK_SIZE*2)//BLOCK_SIZE) * BLOCK_SIZE
        self.food = point(x, y)
        if self.food in self.snake:
            self._place_food()

    # Frame Executes
    def play_step(self):
        global speed

        # Get User Input
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    if self.direction != Direction.RIGHT:
                        self.direction = Direction.LEFT
                elif e.key == pygame.K_RIGHT:
                    if self.direction != Direction.LEFT:
                        self.direction = Direction.RIGHT
                elif e.key == pygame.K_UP:
                    if self.direction != Direction.DOWN:
                        self.direction = Direction.UP
                elif e.key == pygame.K_DOWN:
                    if self.direction != Direction.UP:
                        self.direction = Direction.DOWN
                elif e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                break

        # Move Snake
        self._move(self.direction)
        self.snake.insert(0, self.head)

        # Game Over Check
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # Food Logic
        if self.head == self.food:
            self.score += 1
            speed += 0.5
            self._place_food()
        else:
            self.snake.pop()

        # Update UI and Clock
        self._update_ui()
        self.clock.tick(speed)

        # Return Game State
        return game_over, self.score

    def _is_collision(self):
        # Snake hits horizontal boundary
        if self.head.x > self.w - (BLOCK_SIZE*2) or self.head.x < BLOCK_SIZE:
            return True
        # Snake hits vertical boundary
        if self.head.y > self.h - (BLOCK_SIZE*2) or self.head.y < BLOCK_SIZE:
            return True
        # Snake hits body
        if self.head in self.snake[1:]:
            return True

        return False

    # Interface Updates
    def _update_ui(self):
        # Background
        for blockX in range(BLOCK_SIZE, 1280 - BLOCK_SIZE, BLOCK_SIZE):
            for blockY in range(BLOCK_SIZE, 960 - BLOCK_SIZE, BLOCK_SIZE):
                pygame.draw.rect(self.display, LIME, pygame.Rect(blockX, blockY, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.display, WHITE, pygame.Rect(blockX + 6, blockY + 6, 4, 4))

        # Snake
        for p in self.snake:
            pygame.draw.rect(self.display, BLUE, pygame.Rect(p.x, p.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, CYAN, pygame.Rect(p.x+2, p.y+2, BLOCK_SIZE-4, BLOCK_SIZE-4))
            pygame.draw.rect(self.display, BLUE, pygame.Rect(p.x+4, p.y+4, BLOCK_SIZE-8, BLOCK_SIZE-8))

        # Apple
        pygame.draw.rect(self.display, CRIMSON, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x+2, self.food.y+2, BLOCK_SIZE-4, BLOCK_SIZE-4))
        pygame.draw.rect(self.display, GREEN, pygame.Rect(self.food.x+1, self.food.y+1, 3, 6))

        # Send Updates
        text = font.render("Score: " + str(self.score), True, BLACK)
        self.display.blit(text, [32, 32])
        pygame.display.flip()

    # Move the snake around
    def _move(self, direction):
        x = self.head.x
        y = self.head.y

        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE

        self.head = point(x, y)


scores = []

# Start Executes
if __name__ == '__main__':
    game = snakeGame()

    # Update Loop
    while True:
        game_over, score = game.play_step()

        if game_over:
            scores.append(score)
            total = 0
            for n in scores:
                total += n
            print('Total Score:', str(total))
            game = snakeGame()

    # Game Over
    pygame.quit()
    quit()

# Future Changes: Turn boundaries into teleports instead of death barriers
