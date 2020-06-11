import random

#this section lays out conversion rules for text to code
sizes = {

    'tiny': 50,
    'small': 60,
    'medium': 70,
    'large': 80,
    'huge': 90
}

size = 450

LEFT_SIDE = 0
RIGHT_SIDE = size
TOP = 0
BOTTOM = size


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


def getSize():
    return size