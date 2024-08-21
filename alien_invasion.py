import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inializa el juego y crea recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(selft):
        """Inici el bucle principal para el juego"""
        while True:
            #Busca eventos de teclado y ratón.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                selft.screen.fill(selft.settings.bg_color)
        
            #Hace visible la última pantalla dibujada
            pygame.display.flip() 
            selft.clock.tick(60)


if __name__ == '__main__':
    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
    