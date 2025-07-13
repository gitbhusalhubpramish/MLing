import pygame
from .feed import feed
class train:
  def __init__(self, x, y, width, height, screen, window):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.screen = screen
    self.window = window
    self.color = (255, 255, 255)
    self.text = "train"
    self.font = pygame.font.SysFont(None, 24)
    self.text_surface = self.font.render(self.text, True, (0, 0, 0))
    self.text_rect = self.text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
    self.train = False
    self.feed = None
    self.draw()
  def draw(self):
    if not self.train:
      self.color = (255, 255, 255)
    else:
      self.color = (200, 200, 200)
    pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    self.screen.blit(self.text_surface, self.text_rect)
  def clicked(self, mouse_x, mouse_y):
    if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
      self.train = not self.train
      print(f"clicked train {self.train}")
      if self.train:
        self.feed = feed(500, 250, 100, 50, self.screen, self.window)
      else:
        self.feed = None  # Remove reference
        print("feed deleted")
      return True
  def training(self, clicked):
    if self.train and self.feed:
      self.feed.draw()
      if self.feed.clicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], clicked):
        self.feed.feed()