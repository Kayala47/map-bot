import random

#this section lays out conversion rules for text to code
sizes = {

    'tiny': 2,
    'small': 5,
    'medium': 10,
    'large': 15,
    'huge': 25
}

LEFT_SIDE = 0
RIGHT_SIDE = 100
TOP = 0
BOTTOM = 100


locations = {
    'top left corner': (LEFT_SIDE, TOP),
    'top right corner': (RIGHT_SIDE, TOP),
    'bottom left corner': (LEFT_SIDE, BOTTOM),
    'bottom right corner': (RIGHT_SIDE, BOTTOM), 
    'center': (RIGHT_SIDE/2, BOTTOM/2)

}

possibleLocs = ['top left corner', 'top right corner', 'bottom left corner', 'bottom right corner', 'center']

def chooseEndpt(startPt):
    end = random.choice(possibleLocs)

    if end == startPt:
        chooseEndpt(startPt)
    else:
         return locations[end]
