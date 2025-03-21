import pygame
import math

class Soldier:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level
        self.target = None
        
        # Set properties based on level
        if level == 1:  # Basic soldier
            self.health = 50
            self.max_health = 50
            self.damage = 10
            self.speed = 2
            self.attack_range = 50
            self.attack_speed = 1.0
            self.color = (0, 0, 255)  # Blue
            self.radius = 15
            
        elif level == 2:  # Archer
            self.health = 40
            self.max_health = 40
            self.damage = 15
            self.speed = 1.5
            self.attack_range = 150
            self.attack_speed = 0.8
            self.color = (0, 255, 0)  # Green
            self.radius = 12
            
        elif level == 3:  # Cavalry
            self.health = 80
            self.max_health = 80
            self.damage = 25
            self.speed = 3
            self.attack_range = 40
            self.attack_speed = 1.2
            self.color = (255, 255, 0)  # Yellow
            self.radius = 20
            
        else:  # Wizard
            self.health = 30
            self.max_health = 30
            self.damage = 20
            self.speed = 1
            self.attack_range = 200
            self.attack_speed = 1.5
            self.color = (255, 0, 255)  # Purple
            self.radius = 18
            
        self.last_attack_time = 0
        
    def move(self, target_x, target_y):
        # Calculate direction
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
            
    def can_attack(self, current_time):
        return current_time - self.last_attack_time >= 1.0 / self.attack_speed
        
    def attack(self, target, current_time):
        if self.can_attack(current_time):
            target.take_damage(self.damage)
            self.last_attack_time = current_time
            return True
        return False
        
    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0
        
    def draw(self, screen):
        # Draw soldier
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw health bar
        health_width = (self.health / self.max_health) * (self.radius * 2)
        pygame.draw.rect(screen, (0, 255, 0),
                        (self.x - self.radius, self.y - self.radius - 10,
                         health_width, 5))
        
        # Draw level indicator
        font = pygame.font.Font(None, 20)
        level_text = font.render(str(self.level), True, (255, 255, 255))
        text_rect = level_text.get_rect(center=(self.x, self.y))
        screen.blit(level_text, text_rect) 