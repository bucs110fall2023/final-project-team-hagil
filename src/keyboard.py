import pygame

OG_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key.png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key.png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key.png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key.png",
    "space_key":"final-project-team-hagil/assets/keyboard/space key.png"
}
Al_KEY={
    "w_key":"final-project-team-hagil/assets/keyboard/w key(after).png",
    "s_key":"final-project-team-hagil/assets/keyboard/s key(after).png",
    "a_key":"final-project-team-hagil/assets/keyboard/a key(after).png",
    "d_key":"final-project-team-hagil/assets/keyboard/d key(after).png",
    "space_key":"final-project-team-hagil/assets/keyboard/space key(after).png"
    
}
class Keyboard(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y ):
        super().__init__()
        self.image=pygame.Surface([50,50])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
    
    