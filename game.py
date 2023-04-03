import pygame

DEFAULT_SCREEN_SIZE = (800, 600)

def main():
    game = Game()
    game.run()

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock() # For fps
        self.show_fps = True
        self.is_fullscreen = False # TODO: make it fullscreen
        self.screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE) # Screen size
        self.screen_w = self.screen.get_width()
        self.screen_h = self.screen.get_height()
        self.running = False # For checking if the game is running or not
        # TODO: self.font = ?
        self.init_graphics()
        self.init_objects()

    def init_graphics(self):
        """This is for..initializing..the graphics-stuff
        """
        bat_images = [
            pygame.image.load(f"images\Bat\Move\Frames\Bat Move{num}.png")
            for num in [15]            
        ]
        self.bat_images = [
            pygame.transform.rotozoom(img, 0, self.screen_h / 1).convert_alpha()
            for img in bat_images
        ]

    def init_objects(self):
        """Initializing some objects..
        """
        self.bird_frame = 0
        self.bird_pos = (self.screen_w / 3, self.screen_h / 4)

    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            # TODO: self.handle_logic()
            # TODO: self.update_screen()
            self.clock.tick(60) # Set fps to 60

        pygame.quit()
    
    def handle_events(self):
        """Handles events.
        Like pressing a button -> what will it do?
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_screen(self):
        self.screen.fill("purple")

        # TODO: if self.show_fps:
            # fps_text = f"{self.clock.get_fps()} fps"
            # self.screen.blit(fps_text, (0,0))
        bat_images_i = self.bat_images[(self.bird_frame // 1) % 4]
        bat_images = pygame.transform.rotozoom(bat_images_i, 0, 1)
        self.screen.blit(bat_images, self.bird_pos)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()