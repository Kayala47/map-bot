import svgwrite
from matplotlib import colors
from dictionaries import sizes, locations, chooseEndpt

width = 100
height= 100

# dwg = svgwrite.Drawing('images/test.svg', height=height, width=width)
# dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
# dwg.add(dwg.circle(center=(400,25),
#     r=10, 
#     stroke=svgwrite.rgb(15, 15, 15, '%'),
#     fill='#eeeeee')
# )

# dwg.add(dwg.circle(center=(520,220),
#     r=90, 
#     stroke=svgwrite.rgb(10, 10, 16, '%'),
#     fill='yellow')
# )
# dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
# dwg.save()


def drawThis(phrase, dwg):

    #Draw a #size# #color# #object# in the #location#
    cutUpPhrase = phrase.split(" ")

    sizeTT = cutUpPhrase[2]
    colorTT = cutUpPhrase[3]
    objTT = cutUpPhrase[4]
    locTT = phrase[phrase.index('the') + 4:-1]
    print(locTT)

    
    color = colors.to_rgb(colorTT)
    size = sizes[sizeTT]
    location = locations[str(locTT)]

    #'object': ['lake', 'river', 'forest', 'road'],
    
    if (objTT == 'lake'):
        drawLake(dwg, color, size, location)
    elif (objTT == 'river'):
        drawRiver(dwg, color, size, location, chooseEndpt(location))
    elif(objTT == 'forest'):
        drawForest(dwg, color, size, location)
    elif (objTT=='road'):
        drawRoad(dwg, color, size, location, chooseEndpt(location))


    return dwg

def drawLake(drawing, color, size, location):
    #a lake is just a circle. It can be filled in with any color, but has a black rim
    x,y = location
    #stroke=svgwrite.rgb(15,15,15,'%'),
    drawing.add(drawing.circle(center=location, r=size))#,  fill=color))

def drawRiver(drawing, color, size, loc1, loc2):
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

    drawing.add(drawing.path( d=pathString))#, stroke='#000', fill=color, stroke_width=size))

    
def drawForest(drawing, color, size, loc):
    #a forest is a small rectangle centered on a specific loc and color filled as specified
    drawing.add(drawing.rect(insert=loc, size=(size,size)))#, fill=color))

def drawRoad(drawing, color, size, loc1, loc2):
    #a road is a straight, but thick line that goes from one point to the other
    x1, y1 = loc1
    x2, y2 = loc2

    pathString = "M " + str(x1) + " " + str(y1) + " " #start point
    pathString += "L " + str(x2) + " " + str(y2) #end point

    drawing.add(drawing.path(d=pathString))#, stroke='#000', fill=color, stroke_width=size))




