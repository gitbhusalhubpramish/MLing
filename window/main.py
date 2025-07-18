import pygame
import platform
import os
from .window import Window
from .buttons.reset import reset
from .buttons.getdata import getdata
from .buttons.train import train
from .buttons.run import Run



def main():
  os.environ["SDL_VIDEODRIVER"] = "dummy"
  if platform.system() == "Linux":
    # Only set DISPLAY if not already set (for headless servers)
    if "DISPLAY" not in os.environ:
        os.environ["DISPLAY"] = ":0"

  pygame.init()
  pygame.display.set_caption("drawing area")
  screen = pygame.display.set_mode((640, 480))
  pygame.display.flip()  # Ensure the display is updated
  screen.fill((93, 102, 88))
  windows = Window(280, 280, screen)
  reset_button = reset(500, 20, 100, 50, screen, windows)
  getdata_button = getdata(500, 100, 100, 50, screen, windows)
  train_button = train(500, 180, 100, 50, screen, windows)
  run_button = Run(500, 250, 100, 50, screen, windows)
  running = True
  clicked = False
  while running:
    screen.fill((93, 102, 88))
    windows.run(0,0)
    reset_button.draw()
    getdata_button.draw()
    train_button.draw()
    run_button.draw()
    train_button.training(clicked)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEMOTION and event.buttons[0]:
        mouse_x, mouse_y = event.pos
        windows.run(mouse_x, mouse_y)
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        clicked = True
        if reset_button.clicked(mouse_x, mouse_y):
          reset_button.reset()
        if getdata_button.clicked(mouse_x, mouse_y):
          getdata_button.getdata()
        if train_button.clicked(mouse_x, mouse_y):
          train_button.draw()
        if run_button.clicked(mouse_x, mouse_y):
          run_button.runModel()
      else:
        clicked = False
         
    pygame.display.update()
  pygame.quit()
  print("done")

if __name__ == "__main__":
  main()