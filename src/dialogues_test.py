import pygame
import sys

# Player class 
class Player:
    def __init__(self, position, radius, speed):
        self.position = pygame.Vector2(position)
        self.radius = radius
        self.speed = speed

    def handle_movement(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.position.y += self.speed * dt
        if keys[pygame.K_a]:
            self.position.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.position.x += self.speed * dt

    def check_border_collision(self, screen_width, screen_height):
        if self.position.x - self.radius < 0:  # Left border
            self.position.x = self.radius
        if self.position.x + self.radius > screen_width:  # Right border
            self.position.x = screen_width - self.radius
        if self.position.y - self.radius < 0:  # Top border
            self.position.y = self.radius
        if self.position.y + self.radius > screen_height:  # Bottom border
            self.position.y = screen_height - self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (int(self.position.x), int(self.position.y)), self.radius)


class Dialogue:
    def __init__(self, font, lines, position, color=(255, 255, 255)):
        self.font = font
        self.lines = lines  # List of dialogue lines
        self.position = position
        self.color = color
        self.current_line = 0  
        self.finished = False

    def draw(self, screen):
        if not self.finished:
            text_surface = self.font.render(self.lines[self.current_line], True, self.color)
            screen.blit(text_surface, self.position)

    def next_line(self):
        if self.current_line < len(self.lines) - 1:
            self.current_line += 1
        else:
            self.finished = True


class NPC:
    def __init__(self, position, radius, dialogue_lines, font):
        self.position = pygame.Vector2(position)
        self.radius = radius
        self.dialogue = Dialogue(font, dialogue_lines, (50, 500))
        self.is_interacting = False

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (int(self.position.x), int(self.position.y)), self.radius)

    def check_proximity(self, player):
        distance = self.position.distance_to(player.position)
        return distance <= self.radius + player.radius  # Checks if player is in range

    def interact(self):
        self.is_interacting = True


# Game class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([700, 600])
        pygame.display.set_caption("Game Name")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)  
        self.player = Player(position=(self.screen.get_width() / 2, self.screen.get_height() / 2), radius=40, speed=300)
        self.npc = NPC(position=(100, 300), radius=30, dialogue_lines=["opa", "tranquilo?"], font=self.font)
        self.dt = 0

    def show_initial_dialogue(self):
        initial_dialogue = Dialogue(
            font=self.font,
            lines=["Aperte a barra de espaço para começãr"],
            position=(50, 500)
        )

        while not initial_dialogue.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        initial_dialogue.next_line()

            self.screen.fill("blue")
            initial_dialogue.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(75)

    def run(self):
        # Mostra o dialogo inicial
        self.show_initial_dialogue()

        # Main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Space key advances the dialogue
                        if self.npc.is_interacting:
                            self.npc.dialogue.next_line()

            # Update game objects
            self.screen.fill("blue")
            self.player.handle_movement(self.dt)
            self.player.check_border_collision(self.screen.get_width(), self.screen.get_height())
            self.player.draw(self.screen)
            self.npc.draw(self.screen)

            # Check for NPC interaction
            if self.npc.check_proximity(self.player):
                self.npc.interact()
                if not self.npc.dialogue.finished:
                    self.npc.dialogue.draw(self.screen)
                else:
                    self.npc.is_interacting = False

            # Refresh screen
            pygame.display.flip()
            self.dt = self.clock.tick(75) / 1000 # Limitei pra 75 fps??


if __name__ == "__main__":
    game = Game()
    game.run()