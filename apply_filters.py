from PIL import Image
import numpy as np
import random



def random_img(output, width, height):
    
    array = np.random.random_integers(0,255, (height,width,3))  

    array = np.array(array, dtype=np.uint8)
    img = Image.fromarray(array)
    img.save(output)

    return img


rand_img = random_img('random.png', 1024, 1024)

print(rand_img)


#< -0.05 = blue, -0.5 - 0 = beach, 0 - 0.20 = green, 0.20 - 0.35 mountain, 0.35 - 1.0 snow 

#the following functions apply a filter to a noise map
def apply_stationary(img_array, x, y, delta, difference):
    #apply filters to make sure a mountain pops up where the user wants

    #first change the exact point
    img_array[y][x] = img_array[y][x] + delta

    lt_x = x - 1 #chooses a corner in the top left
    rt_x = x + 1 #chooses a corner in the top right

    #from then on change the height in increasing radius away from the point
    while delta > 0.0:

        length = rt_x - lt_x #this is the length of the square ringing the previous one

        top_left = lt_corner_x, lt_corner_y = lt_x, y -1
        top_right = rt_corner_x, rt_corner_y = rt_x, y - 1

        current_x = lt_corner_x
        current_y = lt_corner_y

        # img_array[current_x][current_y] += delta

        #top
        for i in range(1, length):
            current_x += 1
            img_array[current_y][current_x] += delta
            
        
        #right 
        for i in range(1, length):
            current_y += 1
            img_array[current_y][current_x] += delta
            
        #bottom
        for i in range(1, length):
            current_x -= 1
            img_array[current_y][current_x] += delta

        #left
        for i in range(1, length):
            current_y -= 1
            img_array[current_y][current_x] += delta


        delta -= difference

        lt_x -= 1
        rt_x += 1
        y -= 1

def make_mountain(img_aray, x, y, size):
    apply_stationary(img_aray, x, y, 1.00, size)

def make_lake(img_array, x, y, size):
    #apply filters to make sure a lake pops up where the user wants

    delta = -1.00
    difference = size

    #first change the exact point
    img_array[y][x] = img_array[y][x] + delta

    lt_x = x - 1 #chooses a corner in the top left
    rt_x = x + 1 #chooses a corner in the top right

    #from then on change the height in increasing radius away from the point
    while delta < 0.0:

        length = rt_x - lt_x #this is the length of the square ringing the previous one

        top_left = lt_corner_x, lt_corner_y = lt_x, y -1
        top_right = rt_corner_x, rt_corner_y = rt_x, y - 1

        current_x = lt_corner_x
        current_y = lt_corner_y

        # img_array[current_x][current_y] += delta

        #top
        for i in range(1, length):
            current_x += 1
            img_array[current_y][current_x] += delta
            
        
        #right 
        for i in range(1, length):
            current_y += 1
            img_array[current_y][current_x] += delta
            
        #bottom
        for i in range(1, length):
            current_x -= 1
            img_array[current_y][current_x] += delta

        #left
        for i in range(1, length):
            current_y -= 1
            img_array[current_y][current_x] += delta
        

        delta += difference

        lt_x -= 1
        rt_x += 1
        y -= 1

def make_river(img_array, x, y):
    #it will start at this point and follow a downward path until it can't anymore. 

    blue = -0.30 #that's the value at which it colors blue water
    beach = -0.11 #that's the value for a light tan color

    alreadyUsed = [(y, x)]

    img_array[y][x] = 1000 #for testing, delete once done

    delta = -1.00

    # make_lake(img_array, x, y, 0.1) #starts with a lake there, so water can begin flowing

    #from now on, it chooses a random direction to flow from possible moves (those that are in decreasing heights)
    nextPossible = get_adjacent_cells(img_array, x, y, img_array[y][x], alreadyUsed) #returns all adjacent squares that have less height

    riverLength = 0 #just to make sure it doesn't go on forever

    print("nextPossible before loop: {}".format(nextPossible))

    while nextPossible: 
        #while there are possible steps to take, it chooses one randomly and then begins to choose the next one

        print("already used: {}".format(alreadyUsed))

        print("nextPossible during loop: {}".format(nextPossible))

        next_y, next_x = nextBlock = random.choice(nextPossible)

        print("chosen: {},{}".format(next_y, next_x))

        currentHeight = img_array[next_y][next_x]
        
        img_array[next_y][next_x] += 2 * delta #this will turn that block blue
       

        alreadyUsed.append((next_y, next_x))

        #now, it'll generate the new list of possible steps to take based off the last block it selected
        nextPossible = get_adjacent_cells(img_array, next_x, next_y, currentHeight, alreadyUsed)

        riverLength += 1

        if (riverLength > 100):
            print("reached 100 blocks")
            make_lake(img_array, next_x, next_y, 0.1)
            break







def get_adjacent_cells(img_array, x_coord, y_coord, mainHeight, usedList):
    result = []
    for y, x in [(y_coord+j, x_coord+i) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if x < len(img_array[0]) and img_array[y][x] <= mainHeight and y < len(img_array) and ( x > -1  and y > -1 ) and (y, x) not in usedList and (abs(x_coord - x) <= 1 and abs(y_coord - y) <= 1):
        
            result.append((y, x))

    return result


#
#
#
#if :

    








