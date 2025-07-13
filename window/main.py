import pygame
import platform
import os
from window import Window
from buttons.reset import reset
from buttons.getdata import getdata



def main():
  if platform.system() == "linux":
    os.environ['SDL_VIDEODRIVER'] = 'x11'
  pygame.init()
  pygame.display.set_caption("drawing area")
  screen = pygame.display.set_mode((640, 480))
  screen.fill((93, 102, 88))
  running = True
  windows = Window(280, 280, screen)
  reset_button = reset(500, 20, 100, 50, screen, windows)
  getdata_button = getdata(500, 100, 100, 50, screen, windows)
  
  
  while running:
    reset_button.draw()
    getdata_button.draw()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEMOTION and event.buttons[0]:
        mouse_x, mouse_y = event.pos
        windows.run(mouse_x, mouse_y)
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        if reset_button.clicked(mouse_x, mouse_y):
          reset_button.reset()
        if getdata_button.clicked(mouse_x, mouse_y):
          getdata_button.getdata()
      

if __name__ == "__main__":
  main()