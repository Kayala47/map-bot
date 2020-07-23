import random

#9 quadrants, each taking up 1/9 the space of the world map

def get_loc(string_pos, world_size):
    #returns a range of positions based on the string position value passed in

    length, width = world_size

    #by default, the range spans the whole map
    horizontal = (0, length -  1)
    vertical = (0, width - 1)

    #for the string location, we're expecting 1-3 words tha describe the position of the object

    separate_words = string_pos.split(" ")

    first_third = int(length/3)
    second_third = int(2 * length/3)

    
    if len(separate_words) == 1:
        #if it's only one word, we know it is in the true center
        horizontal = (first_third, second_third) #the middle third of the map
        vertical = (first_third, second_third) 

    elif len(separate_words) == 2:
        #in this case, we actually have two separate values for horizontal and vertical positions

        #vertical
        if (separate_words[0] == 'bottom'):
            vertical = (second_third, length - 1)
        elif (separate_words[0] == 'center'):
            vertical = (first_third, second_third)
        elif (separate_words[0] == 'top'):
            vertical = (0, first_third)

        #horizontal
        if (separate_words[1] == 'right'):
            horizontal = (second_third, width - 1)
        elif (separate_words[1] == 'center'):
            horizontal = (first_third, second_third)
        elif (separate_words[1] == 'left'):
            vertical = (0, first_third)

    return (horizontal, vertical)

        
def get_size(string_size, world_size):

    size = 0.01 # by default

    if string_size == 'tiny':
        return 0.06
    elif string_size == 'small':
        return 0.03
    elif string_size == 'medium':
        return 0.01
    elif string_size == 'large':
        return 0.004
    elif string_size == 'huge':
        return 0.002
    else:
        return size







    