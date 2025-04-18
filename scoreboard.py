import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """Una clase para dar información de la puntuación"""

    def __init__(self, ai_game):
        """Inicializa los atributos de la puntuación"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Configuración de fuente para la información de la puntuación
        
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara las imágenes de puntuaciones iniciales
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def  prep_score(self):
        """Convierte la puntuación en una imagen renderizada"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"        
        self.score_image = self.font.render(score_str, True, 
                                            self.text_color, self.settings.bg_color)
        
        # Muestra la puntuación en la parte superior derecha de la patalla
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Dibuja la puntuaciones, nivel y naves en la pantalla"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def prep_high_score(self):
        """Convierte la puntuación más alta en una imagen renderizada"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)

        # Centra la puntuación más alta en la parte superior de la pantalla
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def check_high_score(self):
        """Comprueba si hay una puntuación más alta"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        """Convierte el nivel en una imagen renderizada"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, 
                self.text_color, self.settings.bg_color)
    
        # Coloca el nivel bajo la puntuación
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Muestra cuentas naves queda"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    

