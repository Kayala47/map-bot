from PIL import Image
import numpy as np


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
    img_array[x][y] = img_array[x][y] + delta

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
            img_array[current_x][current_y] += delta
            
        
        #right 
        for i in range(1, length):
            current_y += 1
            img_array[current_x][current_y] += delta
            
        #bottom
        for i in range(1, length):
            current_x -= 1
            img_array[current_x][current_y] += delta

        #left
        for i in range(1, length):
            current_y -= 1
            img_array[current_x][current_y] += delta


        delta -= difference

        lt_x -= 1
        rt_x += 1
        y -= 1

def make_mountain(img_aray, x, y, size):
    print("made mountain")
    apply_stationary(img_aray, x, y, 1.00, size)

def make_lake(img_array, x, y, size):
    #apply filters to make sure a lake pops up where the user wants

    delta = -1.00
    difference = 0.01

    #first change the exact point
    img_array[x][y] = img_array[x][y] + delta

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
            img_array[current_x][current_y] += delta
            
        
        #right 
        for i in range(1, length):
            current_y += 1
            img_array[current_x][current_y] += delta
            
        #bottom
        for i in range(1, length):
            current_x -= 1
            img_array[current_x][current_y] += delta

        #left
        for i in range(1, length):
            current_y -= 1
            img_array[current_x][current_y] += delta
        
        print("stationary")

        delta += difference

        lt_x -= 1
        rt_x += 1
        y -= 1