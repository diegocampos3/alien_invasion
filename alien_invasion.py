import sys

import pygame

from settings import Settings
from ship import Ship

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

        self.ship = Ship(self)
    
    def run_game(self):
        """Inici el bucle principal para el juego"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
             
            self.clock.tick(60)
    
    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #Mueve la nave a la derecha
                        self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
    
    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva"""
        #Redibuja la pantalla en cada paso del bucle
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

         #Hace visible la última pantalla dibujada
        pygame.display.flip() 


if __name__ == '__main__':
    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
    