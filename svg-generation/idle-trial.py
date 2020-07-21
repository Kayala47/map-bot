import svgwrite
from matplotlib import colors
from dictionaries import sizes, locations, chooseEndpt
import emoji

width = 50
height= 100

dwg = svgwrite.Drawing('images/test.svg', height=height, width=width, profile='tiny')
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
dwg.add(dwg.text('Test', (300, 300), fill='red'))

#The follwoing worked but didn't load the image:
dwg.add(dwg.image('https://picsum.photos/200/300', (100, 100), (100, 100)))


#print(dwg.image(href='https://picsum.photos/200/300'))
dwg.save()
