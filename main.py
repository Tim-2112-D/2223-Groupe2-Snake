import pygame

pygame.init()

dis_width = 600
dis_height = 600
green = "#32CD32"
size = 20

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()


def drawGrid():
    blockSize = 20  # Set the size of the grid block
    for x in range(0, dis_width, blockSize):
        for y in range(0, dis_height, blockSize):
            # rect = pygame.Rect(x, y, blockSize, blockSize)
            # pygame.draw.rect(dis, WHITE, rect, 1)
            pass


class Position:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

    def draw(self):
        pygame.draw.rect(dis, green, [self.x, self.y, self.width, self.width])


class Snake:
    def __init__(self, xpos, ypos):
        self.blocks = [
            Position(xpos, ypos, size),
            Position(xpos - size, ypos, size),
            Position(xpos - 2 * size, ypos, size),
        ]
        self.vel = [size, 0]
        self.length = 3

    def draw(self):
        for block in self.blocks:
            block.draw()

    def keys(self, event):
        if event.key == pygame.K_LEFT and self.vel[0] == 0:
            self.vel[0] = -20
            self.vel[1] = 0
        elif event.key == pygame.K_RIGHT and self.vel[0] == 0:
            self.vel[0] = 20
            self.vel[1] = 0
        elif event.key == pygame.K_UP and self.vel[1] == 0:
            self.vel[0] = 0
            self.vel[1] = -20
        elif event.key == pygame.K_DOWN and self.vel[1] == 0:
            self.vel[0] = 0
            self.vel[1] = 20
        elif event.key == pygame.K_SPACE:
            self.grow()

    def move(self):

        self.blocks = [
            Position(self.blocks[0].x, self.blocks[0].y, size)
        ] + self.blocks[0:-1]

        self.blocks[0].x += self.vel[0]
        self.blocks[0].y += self.vel[1]
        if self.blocks[0].x >= dis_width - 20 and self.vel[0] > 0:
            self.blocks[0].x = -20
        elif self.blocks[0].y >= dis_height - 20 and self.vel[1] > 0:
            self.blocks[0].y = -20
        elif self.blocks[0].x <= -20 and self.vel[0] < 0:
            self.blocks[0].x = dis_width - 20
        elif self.blocks[0].y <= -20 and self.vel[1] < 0:
            self.blocks[0].y = dis_height - 20

        clock.tick(5)

    def grow(self):
        self.length += 1
        self.blocks += [Position(self.blocks[-1].x, self.blocks[-1].x, size)]


def game_loop():
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            player.keys(event)
    player.move()

    dis.fill("#FFFFFF")
    player.draw()
    pygame.display.update()
    return False


game_over = False
player = Snake(40, 40)
while not game_over:
    game_over = game_loop()

pygame.quit()
quit()
