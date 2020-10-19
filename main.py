import pygame as pg
import numpy as np

# Define Classes**************************************************************************************************************************
class Object:

    def __init__(self, image, x, y):
        self.image = pg.image.load(image)
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        gameDisplay.blit(self.image, (self.x, self.y))

class Spritesheet:
    def __init__(self, filename):
        try:
            self.sheet = pg.image.load(filename).convert()

        except pg.error as e:
            print(f"Unable to load sprite sheet image: {filename}")
            raise SystemExit(e)

    def image_at(self, rectangle, colorkey = None):
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        if colorkey == None:
            if colorkey == -1:
                color = image.get_at((0,0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        return [self.image_at(rect,colorkey) for rect in rangerects]

    def load_strip(self, rect, image_count, colorkey = None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[3])
            for x in range(image_count)]
        return self.image_at(tups, colorkey)

class Tile:

    def __init__(self, type, image, x, y, z, width, height):
        self.type = type
        self.image = image
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height

class Terrain:

    def __init__(self, spritesheet, tile_width, tile_height, world_width, world_height):
        self.spritesheet = spritesheet
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.world_width = world_width
        self.world_height = world_height
        self.z_offset = tile_height / 2

    def draw():
        for x in self.width:
            for y in self.height:
                # tile.
                return 0


def generate_tiles(terrain):
    for x in range(terrain.world_width):
        for y in range(terrain.world_height):
            tiles[x][y] = 0

# define global variables**********************************************************************************************************
display_width = 800
display_height = 600

player_movex = 0
player_movey = 0

tiles[0][0] = None

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

end = False

# create instances***********************************************************************************************************
pg.init()
gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('Manhunt')
clock = pg.time.Clock()

# create objects****************************************************************************************************************
man = Object('man.png', display_width / 2, display_height / 2)
terrain = Terrain(Spritesheet("tilesheet.png"), 64, 64, 10, 10)

# mainloop***********************************************************************************************************************
while not end:

    # event handler*********************************************************************************************************
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_movex = -1
            elif event.key == pg.K_RIGHT:
                player_movex = 1

            if event.key == pg.K_UP:
                player_movey = -1
            elif event.key == pg.K_DOWN:
                player_movey = 1

        if event.type == pg.KEYUP:
            if event.key == pg.K_UP or pg.K_DOWN:
                player_movey = 0
            if event.key == pg.K_LEFT or pg.K_RIGHT:
                player_movex = 0

    # update game*****************************************************************************************************************
    gameDisplay.fill(white)
    man.move(player_movex,player_movey)
    generate_tiles(terrain)
    man.draw()
    pg.display.update()
    clock.tick(60)

pg.quit()
quit()
