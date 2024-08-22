import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una clase para gestionarr las balas disparadas desde la nave"""

    def __init__(self, ai_game):
        """Crea un objeto para la bala en la posición actual de la nave"""
        super().__init__() 
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color

        # Crea un rectángulo para la bala en la posición (0, 0) y luego establece
        # la posición correcta

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Guarda la posición como flotante
        self.y = float(self.rect.y)

    def update(selft):
        """Mueve la bala hacia arriba por la pantalla"""
        # Actualiza la posición exacta de la bala.
        selft.y -= selft.settings.bullet_speed
        # Actualiza la pisición del rectángulo.
        selft.rect.y = selft.y
    
    def draw_bullet(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)
 