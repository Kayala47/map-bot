# Python3 program to find path between two 
# cell in matrix 
import collections
from noise_gen import make_heightmap, add_color
import numpy as np
from PIL import Image
import apply_filters as af
import random

def bfs(grid, start, end, min_height, max_height):
    queue = collections.deque([[start]])
    seen = set([start])

    count = 0

    height = len(grid)
    width = len(grid[0])

    while queue:
        
        path = queue.popleft()
        
        x, y = path[-1]
        if (x, y) == end:
            
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen and grid[y2][x2] < max_height and grid[y2][x2] > min_height:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
            count += 1
            
def make_river(grid, start, end, min_height, max_height, recursions):

    path = bfs(grid, start, end, min_height, max_height)

    times = 0

    if recursions > 15:
        return

    if path:
        color_path(grid, path, -2)
    else:
        make_river(grid, start, (random.randint(0, 1023), random.randint(0, 1023)), min_height, max_height, recursions + 1)



# and grid[y2][x2] < max_height  #taken out for now

def color_path(map, path, delta):
    if path:
        for cell in path:
            x, y = cell

            increase_depth((x, y), map, delta)


def increase_depth(loc, map, delta):

    x, y = loc

    map[y][x] += delta

    for i in range(1, 10):

        
        if (y + i < 1024):
            map[y + i][x] += delta/i
        if (y - i > 0):
            map[y - i][x] += delta/i
        if (x + i < 1024):
            map[y][x + i] += delta/i
        if (x - i > 0):
            map[y][x - i] += delta/i


#testing

delta = -3

world, shape = make_heightmap()

min_height = -1000
max_height = 0.60

af.make_lake(world, 300, 300, 0.01)


path = bfs(world, (100,100), (600, 800), min_height, max_height)
# print(path)

min_height = -0.49
max_height = 1000
road = bfs(world, (200, 300), (800, 100), min_height, max_height)

color_path(world, path, delta)

color_path(world, road, 2000)

colored_world = add_color(world, shape)

array = np.array(colored_world, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save('pf-test.png')

# new_image.show()