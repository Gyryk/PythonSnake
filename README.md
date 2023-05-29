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
An array of past scores is created and every time you collide with something, causing the game to end, the score from the game is added to the array and a new total is calculated to be output in the terminal. A new game is then started immediately after. This code is run immediately after you run the command `python main.py` in your terminal

```
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
```
The direction that the snake is moving in is stored as an enumerated class, where there is a fixed set of constants that said direction can be a part of. This is an efficient way to set the direction without having to worry about case sensitive variables

```
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
```
Every integer within the range of 0 and window width that is a multiple of the constant block size is chosen. After that, a square the size of a normal block is drawn from the first integer to the last; this is done at the top (0) as well as bottom (960-block size). To add some detail, dirt (brown pixels) is added to the grass blocks with randomly generated numbers within the bounds of the block.
These blocks serve as the visible boundary at the end of the window.
```
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
```
The same calculations etc. are done, only vertically so as to create the other walls.

```

```
