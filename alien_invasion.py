import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
  
class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inicializa el juego y crea recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Crea una instancia para guardar las estadísticas del juego.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Inicia Alien Invasion en estado activo
        self.game_active = True
    
    def run_game(self):
        """Inicia el bucle principal para el juego"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()
                self.clock.tick(60)
    
    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a pulsaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            #Mueve la nave a la derecha
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Mueve la nave a la izquierda
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Responde a liberaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de las balas"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas."""
        # Actualiza las posiciones de las balas
        self.bullets.update()
        # Se deshace de las balas que han desaparecido
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            #print(len(self.bullets))
        
        self._check_bullet_alien_collisions()
        

    
    def _check_bullet_alien_collisions(self):
        """Responde a las colisiones bala-alien"""
        # Retira todas las balas y aliens que han chocado
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destruye las balas existentes y crea una flota nueva.
            self.bullets.empty()
            self._create_fleet()
    
    def _check_aliens_bottom(self):
        """Comprueba si algún alien a llegado al fondo de la pantalla"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Trata esto como si la nave hubiese sido alcanzada
                self._ship_hit()
                break
    
    def _create_fleet(self):
        """Crea la flota de alienígenas"""
        # Crea un alienígena y va añadiendo alienígenas hasta que no haya espacio
        # El espacio entre alienígenas es de un alien de ancho y otro de alto
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_y = alien_height
        while current_y < (self.screen.get_height() - 3 * alien_height):
            current_x = alien_width
            while current_x < (self.screen.get_width() - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
        
            # Fila terminada; incrementar valor de y
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        """Crea un alienígena y lo coloca en la fila"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Comprueba si la flota está en un orde, despues actualiza lasposiciones"""
        self._check_fleet_edges()
        self.aliens.update()
        # Busca colisiones alien-nave
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Busca aliens llegando al fondo de la pantalla
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        """Responde al impacto de un alien en la nave"""

        if self.stats.ships_left > 0:
            # Disminuye ships_left.
            self.stats.ships_left -= 1

            # Se deshace de los aliens y balas restantes
            self.aliens.empty()
            self.bullets.empty()

            # Crea una flota nueva y centra la nave
            self._create_fleet()
            self.ship.center_ship()

            # Pausa.
            sleep(0.5)
        else:
            self.game_active = False
    
    def _check_fleet_edges(self):
        """Responde adecuadamente si algún alien ha legado a un borde"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su dirección"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    
    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva"""
        #Redibuja la pantalla en cada paso del bucle
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

         #Hace visible la última pantalla dibujada
        pygame.display.flip() 
    
    


if __name__ == '__main__':
    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
    