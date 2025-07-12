import pygame
import platform
import os
from window import Window



def main():
  if platform.system() == "linux":
    os.environ['SDL_VIDEODRIVER'] = 'x11'
  pygame.init()
  pygame.display.set_caption("drawing area")
  screen = pygame.display.set_mode((640, 480))
  running = True
  windows = Window(280, 280, screen)
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEMOTION:
        mouse_x, mouse_y = event.pos
        windows.run(mouse_x, mouse_y)

if __name__ == "__main__":
  main()