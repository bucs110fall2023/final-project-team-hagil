import pygame
class Keyboard(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y):
        super().__init__()
        self.image=pygame.Surface([700,50])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
                         