import pygame
class reset:
  def __init__(self, x, y, width, height, screen, window):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.screen = screen
    self.window = window
    self.color = (255, 255, 255)
    self.text = "reset"
    self.font = pygame.font.SysFont(None, 24)
    self.text_surface = self.font.render(self.text, True, (0, 0, 0))
    self.text_rect = self.text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
    self.draw()
    pygame.display.update()
    
  def draw(self):
    pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    self.screen.blit(self.text_surface, self.text_rect)
  def reset(self, mouse_x, mouse_y):
    if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
      self.window.reset()
      print("reset")