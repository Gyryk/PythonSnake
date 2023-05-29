# Python Snake
> Name seems kind of redundant but this is my rendition of Snake programmed in Python

- If you go through my repositories you might find that this is essentially just my AI driven snake game but the AI has been stripped out and replaced by you, the player. And of course it's been slowed down SIGNIFICANTLY, since we don't run at thousands of ticks per second like the computer
- It's quite a simple, and classic, game which you shouldn't have much problem getting the hang of and then playing in your downtime. Controls are arrow keys
- There isn't anything too complex about the coding of this, it's just a simple program made with PyGame, just like [Space Invaders](https://www.github.com/Gyryk/SpaceInvaders)

`scores = []

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
            game = snakeGame()`
