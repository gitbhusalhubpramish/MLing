import pygame
import os
import json
class feed:
  def __init__(self, x, y, width, height, screen, window):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.screen = screen
    self.window = window
    self.color = (255, 255, 255)
    self.data = {'data': []}
    with open("data.json", "r") as f:
      self.data = json.load(f)
    self.text = "feed"
    self.font = pygame.font.SysFont(None, 24)
    self.text_surface = self.font.render(self.text, True, (0, 0, 0))
    self.text_rect = self.text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
    self.notic = "enter output in terminal"
    self.notic_surface = self.font.render(self.notic, True, (200, 200, 200))
    self.notic_rect = self.notic_surface.get_rect(center=(200 / 2, 200))
  def draw(self):
    pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    self.screen.blit(self.text_surface, self.text_rect)
  def clicked(self, mouse_x, mouse_y, clicked):
    if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height and clicked:
      return True
  def feed(self):
    self.screen.blit(self.notic_surface, self.notic_rect)
    pygame.display.update()
    self.window.getdata()
    self.root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    out = input("enter output: ")
    if out != "nan":
      out = int(out)
      
      while out < 0 or out > 9:
        out = int(input("invalid input enter output: "))
        if out == "nan":
          break
      if out != "nan":
        self.data["data"].append({'input':self.window.data,'output': out})
        file = os.path.join(self.root, "data.json")
        with open(file, "w") as f:
          data = json.dumps(self.data)
          f.write(data)
        print("saved")
    self.window.reset()