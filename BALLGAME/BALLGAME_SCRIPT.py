import pygame,random


# Define some colors
BACKGROUND_COLOR = (255, 255, 255)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.randomize()

    def randomize(self):
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-3, 3)

    def move(self):
        # 更新位置
        self.x += self.dx
        self.y += self.dy

        # 边界碰撞检测
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.dx = -self.dx  # 水平反弹
        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.dy = -self.dy  # 垂直反弹


# create class Player
class Player:
    def __init__(self):
        self.x = 350
        self.y = 250
        self.color = (0, 255, 0)
        self.height = 20
        self.width = 20
        self.distance = 5

    def move(self):
        # detect keys pressing
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.distance
            if self.x < 0:
                self.x = 0
        if keys[pygame.K_RIGHT]:
            self.x += self.distance
            if self.x + self.width > SCREEN_WIDTH:
                self.x = SCREEN_WIDTH - self.width
        if keys[pygame.K_UP]:
            self.y -= self.distance
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_DOWN]:
            self.y += self.distance
            if self.y + self.height > SCREEN_HEIGHT:
                self.y = SCREEN_HEIGHT - self.height



def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Balls")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = []
    for i in range(1, 5):
        r = random.randint(5, 50)
        balls.append(Ball(100*i, 100*i, r))
        # balls.append(Ball(100*i*random.randint(1,2), 100*i))

    player = Player()  # create an instance of class Player

    # Loop until the user clicks the close button or ESC.
    done = False
    while not done:
        # Limit number of frames per second
        clock.tick(60)

        # Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_r:
                    if balls:
                        random_index = random.randint(0, len(balls) - 1)
                        random_ball = balls[random_index]
                        random_ball.randomize()
                # 检测主键盘上的 '+' 键 (Shift + =)
                elif event.key == pygame.K_EQUALS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    new_ball = Ball(350, 250, random.randint(5, 50))
                    balls.append(new_ball)



        for ball in balls:
            ball.move()

        player.move()


        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color,
                               (ball.x, ball.y), ball.radius)

        pygame.draw.rect(screen, player.color, (player.x, player.y, player.height, player.width))

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()



if __name__ == "__main__":
    main()
