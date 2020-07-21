import noise_gen as ng
import apply_filters as af
from translations import get_loc
import random


def drawThis(phrases, fileName):
    
    featuresList = [0, 0, 0, 0, 0] #road, river, lake, forest, mountain

    #make the background and get its size
    world, world_size = ng.make_heightmap()

    for phrase in phrases:

        #Draw a #size# #color# #object# in the #location#
        cutUpPhrase = phrase.split(" ")
        
        sizeTT = cutUpPhrase[0]
        default_size = 0.01 #smaller numbers result in larger objects

        # color = cutUpPhrase[1] # no color here yet
        objTT = cutUpPhrase[1]
        
        #get the location
        locTT = " ".join(cutUpPhrase[2:])
        location_ranges = get_loc(locTT, world_size)
        (x_range,y_range) = location_ranges
        x, y = random.randint(x_range), random.randint(y_range)

        location = (x,y)

        #'object': ['lake', 'river', 'forest', 'road', 'mountain'],
        
        if (objTT == 'lake'):
            af.make_lake(world, x, y, default_size)
            featuresList[0] = 1
            
        elif (objTT == 'river'):
            af.make_river(world, x, y)
            featuresList[1] = 1
            
        elif(objTT == 'forest'):
            print("Haven't coded a forest yet :/")
            featuresList[2] = 1

        elif (objTT=='road'):
            print("Haven't coded a road yet :/")
            featuresList[3] = 1
        
        elif (objTT == 'mountain'):
            af.make_mountain(world, x, y, default_size)
            featuresList[4] = 1

    imgDetails = {"File Name": fileName, "Phrase": phrases, "Road": featuresList[0], "River": featuresList[1], "Lake": featuresList[2], "Forest": featuresList[3]}
    colored_world = ng.add_color(world, world_size)

    #dwg.add(dwg.text(phrase, (100, 400))) #we're not adding the text directly to the picture
    return colored_world, imgDetails