import tkinter, pygame, PIL

# Define Variables and functions as well as their values
class Man:
    x = 0
    y = 0

    def __init__(self,image,startx,starty):
        self.x = startx
        self.y = starty
        self.image = pygame.image.load(image)

    def move(self,movex,movey):
        self.x = self.x + movex
        self.y = self.y + movey

    # def draw(self):
        # gameDisplay.blit(self.image, self.x, self.y)

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Manhunt')
clock = pygame.time.Clock()

man = Man('man.png', display_width * 0.45, display_height * 0.8)

end = False

# mainloop
while not end:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    gameDisplay.fill(white)

    man.move(0,-1)
    gameDisplay.blit(man.image, (man.x, man.y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
