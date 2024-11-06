""" Organizational module
"""
import pygame

class Game:
    """
    The main class representing the game.

    Attributes
    ----------
    bg_music : pygame.mixer.Sound
        The background music for the game.

    screen : pygame.Surface
        The main game window.

    clock : pygame.time.Clock
        A clock to control the game's frame rate.

    x : int
        An example attribute for demonstration purposes.

    running : bool
        Flag indicating whether the game is currently running.

    Methods
    -------
    __init__()
        Initializes the game, including pygame and the game window.

    new()
        Initializes a new game, creating a new level and menu.

    run()
        Runs the main game loop, handling events and updating the game state.
    """
    def __init__(self) -> None:
        """
        Initializes the game

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
        # Initialize pygame and create window
        pygame.init()
        pygame.mixer.init()

        # Audio
        self.bg_music = pygame.mixer.Sound('src/audio/bg_music.wav')
        self.bg_music.set_volume(0.3)
        self.bg_music.play(loops = -1)

        # Screen
        self.screen = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()

        # Game loop
        self.running = True

    def run(self):
        """
        Runs the main game loop
        
        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Pause the game:
                """ 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # ESC to pause"""
                
            # Update the game state and render the screen
            """ 
            if self.menu.current_screen == "main_menu":
                self.menu.main_menu(r"src\graphics\backgrounds\menu_bg.png")
            elif self.level.game_over:
                self.menu.game_over()
            elif self.menu.current_screen == "play":
                self.level.run()
                pygame.display.flip()
                self.clock.tick(60)
            elif self.menu.current_screen == "credits":
                self.menu.credits()"""
            
        # Handling erros
        """except pygame.error as e:
            print(f"An error has occured in the running of the game: {e}")
        except Exception as e:
            print(f"An error has occured in the running of the game: {e}")
         finally:"""
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()






