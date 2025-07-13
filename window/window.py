import pygame
from pixel import Pixel
class Window:
  def __init__(self, width, height, screen):
    self.width = width
    self.height = height
    self.screen = screen
    self.pixels = [[Pixel(x, y, 10, screen) for x in range(0, self.width, 10)] for y in range(0, self.height, 10)]
    self.run(0,0)
    self.data = []
    self.reset()
    pygame.display.update()
    
  def getdata(self):
    data = []
    for row in self.pixels:
      for pixel in row:
        data.append(pixel.val)
    self.data = data
  def run(self, mouse_x, mouse_y):
    for row in self.pixels:
      for pixel in row:
        pixel.update(mouse_x, mouse_y)
        pixel.draw()
        pygame.display.update()
    self.getdata()
  def reset(self):
    for row in self.pixels:
      for pixel in row:
        self.data = []
        pixel.val = 0
        pixel.draw()
        pygame.display.update()
    print(f"rst {self.data}")