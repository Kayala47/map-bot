
import noise
import numpy as np
from scipy.misc import toimage, imsave
from matplotlib import pyplot as plt
from PIL import Image
from apply_filters import make_mountain


blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]

#a good resource = https://medium.com/@yvanscher/playing-with-perlin-noise-generating-realistic-archipelagos-b59f004d8401

def make_heightmap():
    shape = (1024,1024)
    scale = 100.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i/30, 
                                        j/30, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        repeatx=1024, 
                                        repeaty=1024, 
                                        base=0)

    return world, shape

#< -0.20 = blue, -0.20 - -0.10 = beach, -0.10 - 0.60 = green, 0.60 - 0.75 mountain, 0.75 - 1.0 snow 

def add_color(world, shape):
    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.20:
                color_world[i][j] = blue
            elif world[i][j] < -0.10:
                color_world[i][j] = beach
            elif world[i][j] < .60:
                color_world[i][j] = green
            elif world[i][j] < 0.75:
                color_world[i][j] = mountain
            elif world[i][j] < 1.0:
                color_world[i][j] = snow

    return color_world

world, shape = make_heightmap()

print(world[800][200])

make_mountain(world, 800, 200)

print(world[800][200])
        
color_world = add_color(world, shape)

color_world[600][600] = [255, 0, 0]

# print(color_world)

#print the array into an image
array = np.array(color_world, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save('new1.png')