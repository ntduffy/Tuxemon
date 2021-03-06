
import pygame
from core.components.menu import Menu

class DialogMenu(Menu):

    def __init__(self, screen, resolution, game, name="Dialog Menu"):

        # Initialize the parent menu class's default shit
        Menu.__init__(self, screen, resolution, game, name)
        self.delay = 0.5
        self.elapsed_time = self.delay

    def get_event(self, event):

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

            # Hide the menu
            self.visible = False

            # Reset our elapsed time this menu is closed to zero
            self.elapsed_time = 0.0

