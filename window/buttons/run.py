import pygame
import sys
import os

# Add root directory to sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_path)

import run

class Run:
  def __init__(self, x, y, width, height, screen, window):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.screen = screen
    self.window = window
    self.color = (255, 255, 255)
    self.text = "run"
    self.font = pygame.font.SysFont(None, 24)
    self.text_surface = self.font.render(self.text, True, (0, 0, 0))
    self.text_rect = self.text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
    self.draw()
  def draw(self):
    pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    self.screen.blit(self.text_surface, self.text_rect)
  def clicked(self, mouse_x, mouse_y):
    if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
      return True
  def runModel(self):
    self.window.getdata()
    run.main(self.window.data)
    pass