import svgwrite
from matplotlib import colors
from dictionaries import sizes, locations, chooseEndpt
import emoji
import base64
from wand.image import Image
import random
import svgutils.transform as st
import math


# Distance function
def distance(xi,xii,yi,yii):
    sq1 = (xi-xii)*(xi-xii)
    sq2 = (yi-yii)*(yi-yii)
    return math.sqrt(sq1 + sq2)

def drawThis(phrases, dwg, fileName):

    
    featuresList = [0, 0, 0, 0] #road, river, lake, forest

    for phrase in phrases:

        #Draw a #size# #color# #object# in the #location#
        cutUpPhrase = phrase.split(" ")
        
        sizeTT = cutUpPhrase[0]
        color = cutUpPhrase[1]
        objTT = cutUpPhrase[2]
        locTT = " ".join(cutUpPhrase[3:])
        
        size = sizes[sizeTT]
        location = locations[str(locTT)]

        (x,y) = location
        x = x + size if x == 0 else x - size
        y = y + size if y == 0 else y - size
        location = (x,y)

        #draw background
        dwg.add(dwg.rect((0, 0), (450,450), fill='grey', opacity="0.6"))


        #'object': ['lake', 'river', 'forest', 'road'],
        
        if (objTT == 'lake'):
            featuresList[2] = 1
            circle = drawCircle(dwg, color, size, location)
            prettifyWater(dwg, circle)
        elif (objTT == 'river'):
            featuresList[1] = 1
            drawStraightLine(dwg, color, size, location, chooseEndpt(location))
        elif(objTT == 'forest'):
            featuresList[3] = 1
            background = drawSquare(dwg, color, size, location)
            fillWithTrees(dwg, background)
        elif (objTT=='road'):
            featuresList[0] = 1
            drawStraightLine(dwg, color, size, location, chooseEndpt(location))

    
    imgDetails = {"File Name": fileName, "Phrase": phrases, "Road": featuresList[0], "River": featuresList[1], "Lake": featuresList[2], "Forest": featuresList[3]}

    #dwg.add(dwg.text(phrase, (100, 400))) #we're not adding the text directly to the picture
    return dwg, imgDetails

def drawCircle(drawing, color, size, location):
    #a lake is just a circle. It can be filled in with any color, but has a black rim
    x,y = location
    #stroke=svgwrite.rgb(15,15,15,'%'),

    drawing.add(drawing.circle(center=(x, y), r=size,  fill=color, opacity="0.8"))

    return (location, size)

def drawCurvedLine(drawing, color, size, loc1, loc2):
    #a river is a path that goes from one location to the other, filled with a color. The distance between banks is the size

    #this is code to add curves later
    # x1, y1 = loc1
    # x2, y2 = loc2
    # pathString = "M " + x1 + " " + y1 + " " #start pos
    
    # dist = sqrt(pow(x2 - x1, 2) +  pow(y2 - y1, 2) * 1.0); #find distance b/n two points

    #for now, it'll just draw a straight line there
    x1, y1 = loc1
    x2, y2 = loc2

    pathString = "M " + str(x1) + " " + str(y1) + " " #start point
    pathString += "L " + str(x2) + " " + str(y2) #end point

    drawing.add(drawing.path( d=pathString, stroke='#000', fill=color, stroke_width=size))

    
def drawSquare(drawing, color, size, loc):
    #a forest is a small rectangle centered on a specific loc and color filled as specified

    x,y = loc

    square = drawing.rect((x, y), (size,size), fill=color, opacity="0.8")

    #fillWithTrees(dwg, square, size)

    drawing.add(square)

    return [loc, size] #returns dimensions of the square for later use

def drawStraightLine(drawing, color, size, loc1, loc2):
    #a road is a straight, but thick line that goes from one point to the other
    x1, y1 = loc1
    x2, y2 = loc2

    size = size/10

    #(r,g,b) = color

    drawing.add(drawing.line(start=(x1,y1), end=(x2,y2), stroke=color, stroke_width=size))


def fillWithTrees(dwg, background):
    #it's going to draw several trees inside the "forest" square at random

    numTrees = random.randint(80, 100)

    loc, size = background
    x, y = loc

    img = Image(filename="tree1.png")

    # Then get raw PNG data and encode DIRECTLY into the SVG file.
    image_data = img.make_blob(format='png')
    encoded = base64.b64encode(image_data).decode()
    pngdata = 'data:image/png;base64,{}'.format(encoded)

    for i in range(0 ,numTrees):
        #draws that many # of trees randomly in the square
        treeX = random.randint(x, x + size)
        treeY = random.randint(y, y + size)


        dwg.add(dwg.image(href=(pngdata), insert=(treeX,treeY), size=(size/5, size/5)))


def prettifyWater(dwg, background):
    #I'll add some squiggles to anything that has water

    numSquiggles = random.randint(10, 20)

    img = Image(filename="src-images\water-squiggle.png")

    image_data = img.make_blob(format='png')
    encoded = base64.b64encode(image_data).decode()
    pngdata = 'data:image/png;base64,{}'.format(encoded)

    loc, rad = background
    x, y = loc

    for i in range(numSquiggles):
        sqX = random.randint(x - rad, x + rad)
        sqY = random.randint(y - rad, y + rad)

        if distance(x, y, sqX, sqY) > rad:
            #outside the circle
            numSquiggles += 1
            continue
        else:
            dwg.add(dwg.image(href=(pngdata), insert=(sqX, sqY), size=(rad/5, rad/5)))







width = 50
height= 100

dwg = svgwrite.Drawing('images/test.svg', height=height, width=width, profile='tiny')
#dwg2 = svgwrite.Drawing('images/test2.svg', height=height, width=width, profile='tiny')

dwg.add(dwg.circle(center=(0,0),
    r=10, 
    stroke=svgwrite.rgb(15, 15, 15, '%'),
    fill='#eeeeee')
)


circle = drawCircle(dwg, "blue", 200, (300,400))
prettifyWater(dwg, circle)


dwg.add(dwg.circle(center=(520,220),
    r=90, 
    stroke=svgwrite.rgb(10, 10, 16, '%'),
    fill='yellow')
)
dwg.add(dwg.line(start=(100,100), end=(700,700), stroke='purple', stroke_width='5px'))
dwg.add(dwg.text('Test', (300, 300), fill='red'))

square = drawSquare(dwg, 'green', 100, (100,100))

fillWithTrees(dwg, square)

img = Image(filename="src-images\water-squiggle.png")

# Then get raw PNG data and encode DIRECTLY into the SVG file.
image_data = img.make_blob(format='png')
encoded = base64.b64encode(image_data).decode()
pngdata = 'data:image/png;base64,{}'.format(encoded)

image = dwg.add(dwg.image(href=(pngdata), insert=(100,500), size=(100,100)))

dwg.save()
