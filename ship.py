import pygame

class Ship:
    """Una clase para gestionar la nave"""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición actual"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Cargar la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la pate inferior de
        # la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda un valor decimal para la posición horizontal exacta de la nave
        self.x = float(self.rect.x)

        # Banderas de movimiento; comienza con una nave que no está en movimiento
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Actualiza la pisición de la nave en función de las banderas de movimiento"""
        #Actualiza el valor de x de la nave, no el rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        #Actualiza el objeto rect de self .x.
        #self.rect.x = self.x

    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centra la nave en la pantalla"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)