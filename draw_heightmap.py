import noise_gen as ng
import apply_filters as af
from translations import get_loc, get_size
import random
from PIL import Image
import pathfinder as pf


def drawThis(phrases, fileName):
    
    featuresList = [0, 0, 0, 0, 0] #road, river, lake, forest, mountain

    #make the background and get its size
    world, world_size = ng.make_heightmap()

    roads = []
    rivers = []

    for phrase in phrases:

        #Draw a #size# #color# #object# in the #location#
        cutUpPhrase = phrase.split(" ")
        
        sizeTT = cutUpPhrase[0]
        default_size = 0.01 #smaller numbers result in larger objects
        size = get_size(sizeTT, world_size)

        # color = cutUpPhrase[1] # no color here yet
        objTT = cutUpPhrase[1]
        
        #get the location
        locTT = " ".join(cutUpPhrase[2:])
        location_ranges = get_loc(locTT, world_size)
        (x_range,y_range) = location_ranges
        (ax, bx), (ay, by) = x_range, y_range

        x = random.randint(ax, bx)
        y = random.randint(ay, by)

        location = (x,y)

        #'object': ['lake', 'river', 'forest', 'road', 'mountain'],
        forest = []
        
        if (objTT == 'lake'):
            af.make_lake(world, x, y, size)
            featuresList[2] = 1
            
        elif (objTT == 'river'):
            rivers.append(location)
            
            featuresList[1] = 1
            
        elif(objTT == 'forest'):
            forest = [location, default_size]
            featuresList[3] = 1

        elif (objTT=='road'):
            roads.append(location)
            
            featuresList[0] = 1
        
        elif (objTT == 'mountain'):
            af.make_mountain(world, x, y, size)
            featuresList[4] = 1

    #now draw all the rivers
    if rivers:
        for river in rivers:
            path = pf.make_river(world, river, (random.randint(0, 1023), random.randint(0, 1023)), -1000, 0.60, 0)

            if not path:
                #this deals with the case where no path was found - then we just try a different one
                path = pf.make_river(world, location, (random.randint(0, 1023), random.randint(0, 1023)), -1000, 0.60, 0)
  
            pf.color_path(world, path, -3)

    #now draw all the roads
    if roads:
        for road in roads:
            path = pf.bfs(world, location, (random.randint(0, 1023), random.randint(0, 1023)), -0.50, 3000)

            if not path:
                #this deals with the case where no path was found - then we just try a different one
                path = pf.bfs(world, location, (random.randint(0, 1023), random.randint(0, 1023)), -0.50, 3000)

            pf.color_path(world, path, 1000)


    imgDetails = {"File Name": fileName, "Phrase": phrases, "Road": featuresList[0], "River": featuresList[1], "Lake": featuresList[2], "Forest": featuresList[3], "Mountain": featuresList[4]}
    colored_world = ng.add_color(world, world_size)
    
    return colored_world, imgDetails, forest

def fillWithTrees(img_name, loc, size):
    #it's going to draw several trees inside the "forest" square at random

    numTrees = random.randint(80, 100)

    size = size * 10000

    x, y = loc
    
    foreground = Image.open('tree.png').resize((50,50))
    background = Image.open(img_name)


    # # Then get raw PNG data and encode DIRECTLY into the SVG file.
    # image_data = foreground.make_blob(format='png')
    # encoded = base64.b64encode(image_data).decode()
    # pngdata = 'data:image/png;base64,{}'.format(encoded)

    for i in range(0, numTrees):
        #draws that many # of trees randomly in the square
        treeX = random.randint(x, min(x + size, 1023))
        treeY = random.randint(y, min(y + size, 1023))

        background.paste(foreground, (treeX, treeY), foreground.convert('RGBA'))
        # Image.alpha_composite(background, foreground).save(img_name)
        
    # background.show()

    return background




        