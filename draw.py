import svgwrite
from matplotlib import colors

dwg = svgwrite.Drawing('images/test.svg', profile='tiny')
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
dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()

def drawThis(phrase):

    fixedPhrase = phrase.replace(" ", "-")
    fileName = "images/" + fixedPhrase

    dwg = svgwrite.Drawing(fileName, profile='tiny')

    #Draw a #size# #color# #object# in the #location#
    cutUpPhrase = phrase.split(" ")

    sizeTT = cutUpPhrase[2]
    colorTT = cutUpPhrase[3]
    objTT = cutUpPhrase[4]
    locTT = cutUpPhrase[7]

    
    color = colors.to_rgb(colorTT)






    return dwg

