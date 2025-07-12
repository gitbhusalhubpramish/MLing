import pygame

class Pixel:
  def __init__(self, x, y, size, screen):
    self.x = x
    self.y = y
    self.size = size
    self.screen = screen
    self.val = 0
    self.color = (0, 0, 0)

  def update(self, mouse_x, mouse_y):
    if self.x <= mouse_x <= self.x + self.size and self.y <= mouse_y <= self.y + self.size:
      center_x = self.x + self.size / 2
      center_y = self.y + self.size / 2

      dx = mouse_x - center_x
      dy = mouse_y - center_y
      dist = (dx**2 + dy**2) ** 0.5  # Euclidean distance

      max_dist = (2 * (self.size / 2) ** 2) ** 0.5  # max distance: corner to center
      closeness = 1 - min(dist / max_dist, 1)       # 1 = center, 0 = edge

      self.val = closeness
      shade = int(255 * self.val)
      self.color = (shade, shade, 200)
    else:
      self.color = (0, 0, 200)

  def draw(self):
    pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))
