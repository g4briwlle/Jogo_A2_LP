import pygame

class Player:
    def __init__(self, x: int, y: int, width: int = 50, height:int = 50):
        self.rect = pygame.Rect(x, y, width, height)
        self.vel_y = 0 # velocidade vertical
        self.gravity = 0.5 # força da gravidade
        self.is_jumping = False # estado do pulo
        
    def __jump(self):
        if not self.is_jumping:
            self.vel_y = -10
            self.is_jumping = True

    def __apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

    def __on_out_of_bounds(self):
        if self.rect.right > SCREEN_WIDTH: # Borda direita
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0: # Borda esquerda
            self.rect.left = 0
        if self.rect.top < 0:
             self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.is_jumping = False

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.__jump

    def update(self):
        self.__apply_gravity()
        self.__on_out_of_bounds()

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.on_event(event)

    player.update

    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()



