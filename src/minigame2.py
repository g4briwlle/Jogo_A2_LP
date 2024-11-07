""" Module with the minigame 'MAZEAMAZE'
"""

import pygame
import pyamaze

class MazeAmaze:
    def __init__(self, maze_file) -> None:
        """
        Initializes the game

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
        self.rows = 8
        self.cols = 16
        self.start_position = (4, 1) 
        self.end_position = (8, 16)
        self.cell_size = 40
        self.maze_file = maze_file
        self.mazeamaze = pyamaze.maze(self.rows, self.cols)

    def setup_maze(self, screen):
        """
        Place settings of the maze from pyamaze in pygame, creating 
        """
        # Size of maze
        self.mazeamaze = pyamaze.maze(self.rows, self.cols)

        # Create maze with destination using pyamaze and saving mazes into files
        # self.mazeamaze.CreateMaze(self.end_position[0], self.end_position[1], loopPercent=20, saveMaze=True) 

        # Creating the maze with the file
        self.mazeamaze.CreateMaze(self.end_position[0], self.end_position[1], loadMaze=self.maze_file) # interrogaçao

    def draw_maze(self, screen):
        """
        Draw the maze from pyamaze in pygame
        """
        # Draw walls with the maze in pygame according to maze of pyamaze
        for x in range(1, self.rows + 1):
            for y in range(1, self.cols + 1):
                cell_x = (y - 1) * self.cell_size
                cell_y = (x - 1) * self.cell_size

                if not self.mazeamaze.maze_map[(x, y)]['S']:
                    pygame.draw.line(screen, (0, 0, 0), (cell_x, cell_y + self.cell_size), (cell_x + self.cell_size, cell_y + self.cell_size), 2)
                if not self.mazeamaze.maze_map[(x, y)]['N']:
                    pygame.draw.line(screen, (0, 0, 0), (cell_x, cell_y), (cell_x + self.cell_size, cell_y), 2)
                if not self.mazeamaze.maze_map[(x, y)]['E']:
                    pygame.draw.line(screen, (0, 0, 0), (cell_x + self.cell_size, cell_y), (cell_x + self.cell_size, cell_y + self.cell_size), 2)
                if not self.mazeamaze.maze_map[(x, y)]['W']:
                    pygame.draw.line(screen, (0, 0, 0), (cell_x, cell_y), (cell_x, cell_y + self.cell_size), 2)


class Agent():
    def __init__(self):
        self.cell_size = 40
        self.start_position = (4, 1)
        self.mazeamaze = pyamaze.maze(self.rows, self.cols)

    def draw_agent(self, screen):
        """
        Creat agent in pygame
        """
        self.agent_position = self.start_position
        x, y = self.agent_position
        # Positions the agent
        agent_x = (y-1) * self.cell_size 
        agent_y = (x-1) * self.cell_size  
        # Draws
        pygame.draw.rect(screen, (255, 0, 255), (agent_x, agent_y, self.cell_size, self.cell_size))

    def move_agent(self, direction):
        """
        Move the agent in the specified direction if possible.
        """
        # Indicate agent in this function
        self.agent_position = self.start_position
        x, y = self.agent_position
        
        # Change the coordinates in the direction if possible
        if direction == 'DOWN' and self.mazeamaze.maze_map[(x, y)]['S']:
            self.agent_position = (x + 1, y)
        elif direction == 'UP' and self.mazeamaze.maze_map[(x, y)]['N']:
            self.agent_position = (x - 1, y)
        elif direction == 'RIGHT' and self.mazeamaze.maze_map[(x, y)]['E']:
            self.agent_position = (x, y + 1)
        elif direction == 'LEFT' and self.mazeamaze.maze_map[(x, y)]['W']:
            self.agent_position = (x, y - 1)


class Timer:
    def __init__(self, countdown_time):
        """
        Inicializes the class
        """
        self.font = pygame.font.SysFont(None, 36)
        self.start_time = pygame.time.get_ticks()
        self.countdown_time = countdown_time  # Time in seconds

    def get_time_remaining(self) -> int:
        """
        Gets the time remaining and returns it
        """
        elapsed_time = pygame.time.get_ticks() - self.start_time
        remaining_time = self.countdown_time - elapsed_time // 1000
        if remaining_time < 0:
            remaining_time = 0
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        return f"Time: {minutes:02}:{seconds:02}"
    
    def draw_timer(self, screen) -> None:
        """
        Draws timer on screen
        """
        time_text = self.font.render(self.get_time_remaining(), True, (0, 0, 0))
        screen.blit(time_text, (10, 600))

    def is_time_up(self) -> bool:
        """
        Says if the time is over or not with a bool return
        """
        elapsed_time = pygame.time.get_ticks() - self.start_time
        remaining_time = self.countdown_time - elapsed_time // 1000
        return remaining_time <= 0



def start():
    """
    Starts MAZEAMAZE
    """

    # Inicializes pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('MAZEAMAZE')
    # Inicializes and draws maze
    running = True
    maze = MazeAmaze('Jogo_A2_LP\docs\maze--2024-11-07--12-47-38.csv')
    timer = Timer(1000)
    player = Agent()

    # Main loop for pygame
    while running:
        screen.fill((255, 255, 255))  # Cleans screen
        maze.draw_maze(screen)  # Draws maze
        player.draw_agent(screen) #Draws agent
        timer.draw_timer(screen) 
        pygame.display.flip()  # Update screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exiting the game
                running = False
            elif event.type == pygame.KEYDOWN:   # Moving agent
                if event.key == pygame.K_DOWN:
                    player.move_agent('DOWN')
                elif event.key == pygame.K_UP:
                    player.move_agent('UP')
                elif event.key == pygame.K_RIGHT:
                    player.move_agent('RIGHT')
                elif event.key == pygame.K_LEFT:
                    player.move_agent('LEFT')

    pygame.quit()

        

start()
# labirinto2 = MazeAmaze(maze_file='Jogo_A2_LP/docs/maze--2024-11-07--12-47-41.csv')
# labirinto2.start()