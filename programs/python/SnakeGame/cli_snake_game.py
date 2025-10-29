import random
import curses

def create_food(window, snake):
    sh, sw = window.getmaxyx()
    while True:
        food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
        if food not in snake:
            return food

def main(window):
    curses.curs_set(0)
    window.nodelay(True)
    window.timeout(100)

    sh, sw = window.getmaxyx()
    snake_y, snake_x = sh // 2, sw // 4
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    direction = curses.KEY_RIGHT
    food = create_food(window, snake)
    score = 0

    while True:
        window.clear()
        window.border(0)
        window.addstr(0, 2, f'Score: {score} ')
        window.addch(food[0], food[1], '🍎')

        for y, x in snake:
            window.addch(y, x, '🟩')

        new_direction = window.getch()
        if new_direction in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            # Prevent going backwards directly
            opposite = {curses.KEY_RIGHT: curses.KEY_LEFT, curses.KEY_LEFT: curses.KEY_RIGHT,
                        curses.KEY_UP: curses.KEY_DOWN, curses.KEY_DOWN: curses.KEY_UP}
            if direction != opposite.get(new_direction):
                direction = new_direction

        head = snake[0].copy()
        if direction == curses.KEY_RIGHT:
            head[1] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1

        snake.insert(0, head)

        # Collision with border or itself
        if (head[0] in [0, sh - 1] or head[1] in [0, sw - 1] or head in snake[1:]):
            msg = f'Game Over! Final Score: {score}'
            window.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            window.nodelay(False)
            window.getch()
            break

        if head == food:
            score += 1
            food = create_food(window, snake)
        else:
            snake.pop()

if __name__ == "__main__":
    curses.wrapper(main)
