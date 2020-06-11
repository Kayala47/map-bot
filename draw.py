import svgwrite
from matplotlib import colors
from dictionaries import sizes, locations, chooseEndpt

width = 50
height= 100

dwg = svgwrite.Drawing('images/test.svg', height=height, width=width)
dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.circle(center=(400,25),
    r=10, 
    stroke=svgwrite.rgb(15, 15, 15, '%'),
    fill='#eeeeee')
)

dwg.add(dwg.circle(center=(520,220),
    r=90, 
    stroke=svgwrite.rgb(10, 10, 16, '%'),
    fill='yellow')
)
dwg.add(dwg.line(start=(100,100), end=(700,700), stroke='purple', stroke_width='5px'))
dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()


def drawThis(phrase, dwg):

    #Draw a #size# #color# #object# in the #location#
    cutUpPhrase = phrase.split(" ")

    sizeTT = cutUpPhrase[2]
    color = cutUpPhrase[3]
    objTT = cutUpPhrase[4]
    locTT = phrase[phrase.index('the') + 4:-1]
    
    

    size = sizes[sizeTT]
    location = locations[str(locTT)]

    (x,y) = location
    x = x + size if x == 0 else x - size
    y = y + size if y == 0 else y - size
    location = (x,y)

    #'object': ['lake', 'river', 'forest', 'road'],
    
    if (objTT == 'lake'):
        drawCircle(dwg, color, size, location)
    elif (objTT == 'river'):
        drawStraightLine(dwg, color, size, location, chooseEndpt(location))
    elif(objTT == 'forest'):
        drawSquare(dwg, color, size, location)
    elif (objTT=='road'):
        drawStraightLine(dwg, color, size, location, chooseEndpt(location))


    dwg.add(dwg.text(phrase, (100, 400)))
    return dwg

def drawCircle(drawing, color, size, location):
    #a lake is just a circle. It can be filled in with any color, but has a black rim
    x,y = location
    #stroke=svgwrite.rgb(15,15,15,'%'),

   
    drawing.add(drawing.circle(center=(x, y), r=size,  fill=color))

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

    drawing.add(drawing.rect((x, y), (size,size), fill=color))

def drawStraightLine(drawing, color, size, loc1, loc2):
    #a road is a straight, but thick line that goes from one point to the other
    x1, y1 = loc1
    x2, y2 = loc2

    size = size/10

    #(r,g,b) = color

    drawing.add(drawing.line(start=(x1,y1), end=(x2,y2), stroke=color, stroke_width=size))




