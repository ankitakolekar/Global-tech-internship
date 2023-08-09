import pygame
import random


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
SNAKE_START_LENGTH = 3
SNAKE_START_POSITION = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
INITIAL_SPEED = 10


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


class Snake:
    def __init__(self):
        self.body = [SNAKE_START_POSITION]
        self.direction = (1, 0)

    def grow(self):
        tail_x, tail_y = self.body[-1]
        dx, dy = self.direction
        new_tail = ((tail_x - dx) % GRID_WIDTH, (tail_y - dy) % GRID_HEIGHT)
        self.body.append(new_tail)

    def check_collision(self):
        return len(set(self.body)) != len(self.body)

    def change_direction(self, dx, dy):
        self.direction = (dx, dy)

    def move(self, grow=False):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()


class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

def draw_snake(snake):
    for segment in snake.body:
        x, y = segment
        pygame.draw.rect(screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    x, y = food.position
    pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def update_score(score):
    font = pygame.font.Font(None, 36)
    score_display = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_display, (10, 10))

def main():
    snake = Snake()
    food = Food()
    score = 0
    speed = INITIAL_SPEED
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.change_direction(1, 0)

        snake.move()

        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.random_position()
            score += 10
            speed += 1

        if snake.check_collision():
            pygame.quit()
            quit()

        screen.fill((0, 0, 0))
        draw_snake(snake)
        draw_food(food)
        update_score(score)
        pygame.display.update()
        clock.tick(speed)

if __name__ == "__main__":
    main()
