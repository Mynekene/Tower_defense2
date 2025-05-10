from data import *

class Mob:
    def __init__(self, path, speed=1):
        self.path = path
        self.current_point = 0
        self.x, self.y = path[0]
        self.speed = speed
        self.image = mob_image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        if self.current_point + 1 < len(self.path):
            target_x, target_y = self.path[self.current_point + 1]
            dx, dy = target_x - self.x, target_y - self.y
            dist = (dx**2 + dy**2)**0.5
            if dist < self.speed:
                self.x, self.y = target_x, target_y
                self.current_point += 1
            else:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist
            self.rect.center = (round(self.x), round(self.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
mobs = [Mob(path)]