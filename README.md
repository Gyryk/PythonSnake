# Python Snake
> Name seems kind of redundant but this is my rendition of Snake programmed in Python

- If you go through my repositories you might find that this is essentially just my AI driven snake game but the AI has been stripped out and replaced by you, the player. And of course it's been slowed down SIGNIFICANTLY, since we don't run at thousands of ticks per second like the computer
- It's quite a simple, and classic, game which you shouldn't have much problem getting the hang of and then playing in your downtime. Controls are arrow keys
- There isn't anything too complex about the coding of this, it's just a simple program made with PyGame, just like [Space Invaders](https://www.github.com/Gyryk/SpaceInvaders)
<br>

## Documentation
```
scores = []

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
```
An array of past scores is created and every time you collide with something, causing the game to end, the score from the game is added to the array and a new total is calculated to be output in the terminal. A new game is then started immediately after. This code is run immediately after you run the command `python main.py` in your terminal.

```
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
```
The direction that the snake is moving in is stored as an enumerated class, where there is a fixed set of constants that said direction can be a part of. This is an efficient way to set the direction without having to worry about case sensitive variables.

```
for block in range(0, 1280, BLOCK_SIZE):
    pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(block, 0, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(self.display, BROWN, pygame.Rect(block + random.randint(0, 4), random.randint(0, 8), random.randint(1, 4), random.randint(1, 6)))
    pygame.draw.rect(self.display, BROWN, pygame.Rect(block + random.randint(8, 12), random.randint(0, 8), random.randint(1, 4), random.randint(1, 6)))

    pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(block, 960 - BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(self.display, BROWN, pygame.Rect(block + random.randint(0, 4), 960 - random.randint(6, 14), random.randint(1, 4), random.randint(1, 6)))
    pygame.draw.rect(self.display, BROWN, pygame.Rect(block + random.randint(8, 12), 960 - random.randint(6, 14), random.randint(1, 4), random.randint(1, 6)))
```
Every integer within the range of 0 and window width that is a multiple of the constant block size is chosen. After that, a square the size of a normal block is drawn from the first integer to the last; this is done at the top (0) as well as bottom (960-block size). To add some detail, dirt (brown pixels) is added to the grass blocks with randomly generated numbers within the bounds of the block.
These blocks serve as the visible boundary at the end of the window.
```
for block in range(0, 960, BLOCK_SIZE):
    pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(0, block, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(self.display, BROWN, pygame.Rect(random.randint(0, 4), block + random.randint(0, 8), random.randint(1, 4), random.randint(1, 6)))
    pygame.draw.rect(self.display, BROWN, pygame.Rect(random.randint(8, 12), block + random.randint(0, 8), random.randint(1, 4), random.randint(1, 6)))

    pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(1280 - BLOCK_SIZE, block, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(self.display, BROWN, pygame.Rect(1280 - random.randint(10, 14), block + random.randint(0, 8), random.randint(1, 4), random.randint(1, 6)))
    pygame.draw.rect(self.display, BROWN, pygame.Rect(1280 - random.randint(10, 14), block + random.randint(0, 8), random.randint(1, 4), random.randint(1, 6)))
```
The same calculations etc. are done, only vertically so as to create the other walls.

```
def _place_food(self):
    x = random.randint(BLOCK_SIZE, (self.w-BLOCK_SIZE*2)//BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(BLOCK_SIZE, (self.h-BLOCK_SIZE*2)//BLOCK_SIZE) * BLOCK_SIZE
    self.food = point(x, y)
    if self.food in self.snake:
        self._place_food()
```
Find a valid block coordinate in terms of x and y directions, between the first block and the last block. Subsequently, set the position of the food at the point with those coordinates. If the snake eats the food, the function is called again.

```
game_over = False
if self._is_collision():
    game_over = True
    return game_over, self.score
```
This small piece of code is responsible for checking whether there is a collision in each frame of the game, ending the game if there is one.

```
if self.head == self.food:
    self.score += 1
    speed += 0.5
    self._place_food()
else:
    self.snake.pop()
        
self.clock.tick(speed)
```
This is the logic for increasing the score, as well as the speed, whenever the snake eats the food. Otherwise the snake's last block is deleted to avoid drawing extra blocks, since a new one is created at the head. The speed is input in the clock's tickrate function to change how fast the game goes.

```
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
```
This boolean function checks whether the coordinates of the snake's head are the same as those of any of the boundary blocks, and if they are then it returns True.

```
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
```
The move function takes in the direction to move in as a parameter and depending on the direction specified, it changes the coordinates of the snake by 1 block at a time.

```
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
```
This function draws the entire dotted matrix pattern in the background behind the snake, draws the design for each block of the snake, draws a set of blocks that resembles an apple, and finally renders the score in the specified font. After doing all of this it sends these pixels to draw over to PyGame to update the window. This is called every frame.
