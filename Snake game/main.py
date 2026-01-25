import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.color = GREEN
        self.head_color = DARK_GREEN
        self.score = 0
        
    def get_head_position(self):
        return self.positions[0]
    
    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + x) % GRID_WIDTH), ((cur[1] + y) % GRID_HEIGHT))
        
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.score = 0
    
    def render(self, surface):
        for i, p in enumerate(self.positions):
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            if i == 0:
                pygame.draw.rect(surface, self.head_color, r)
                pygame.draw.rect(surface, WHITE, r, 1)
            else:
                pygame.draw.rect(surface, self.color, r)
                pygame.draw.rect(surface, WHITE, r, 1)
    
    def handle_keys(self, keys):
        if keys[pygame.K_UP] and self.direction != DOWN:
            self.direction = UP
        elif keys[pygame.K_DOWN] and self.direction != UP:
            self.direction = DOWN
        elif keys[pygame.K_LEFT] and self.direction != RIGHT:
            self.direction = LEFT
        elif keys[pygame.K_RIGHT] and self.direction != LEFT:
            self.direction = RIGHT

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    def render(self, surface):
        r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

def draw_grid(surface):
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            r = pygame.Rect((x, y), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, GRAY, r, 1)

def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    
    snake = Snake()
    food = Food()
    
    # Game state
    game_over = False
    paused = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r and game_over:
                    snake.reset()
                    food.randomize_position()
                    game_over = False
        
        if not game_over and not paused:
            keys = pygame.key.get_pressed()
            snake.handle_keys(keys)
            snake.update()
            
            # Check if snake ate food
            if snake.get_head_position() == food.position:
                snake.length += 1
                snake.score += 10
                food.randomize_position()
                # Make sure food doesn't spawn on snake
                while food.position in snake.positions:
                    food.randomize_position()
        
        # Draw everything
        screen.fill(BLACK)
        draw_grid(screen)
        
        if not game_over:
            snake.render(screen)
            food.render(screen)
        else:
            draw_text(screen, "GAME OVER", 72, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50, RED)
            draw_text(screen, f"Final Score: {snake.score}", 36, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20)
            draw_text(screen, "Press R to Restart", 24, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60)
        
        if paused:
            draw_text(screen, "PAUSED", 72, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50, BLUE)
            draw_text(screen, "Press SPACE to Continue", 24, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20)
        
        # Display score
        draw_text(screen, f"Score: {snake.score}", 24, WINDOW_WIDTH - 100, 10)
        
        # Display instructions
        draw_text(screen, "Use Arrow Keys to Move", 18, 100, 10, GRAY)
        draw_text(screen, "SPACE: Pause | ESC: Quit", 18, 100, 30, GRAY)
        
        pygame.display.update()
        clock.tick(10)  # Game speed (frames per second)

if __name__ == "__main__":
    main()
