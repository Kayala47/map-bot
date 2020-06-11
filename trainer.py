from generate_text import generate 
from draw import drawThis
import svgwrite
from dictionaries import getSize

f = open('output.txt', 'w')

size = getSize()

for i in range(0,4):
    phrase = generate()

    fixedPhrase = phrase.replace(" ", "-")
    fixedPhrase = fixedPhrase.replace('Draw-a-', '')
    fixedPhrase = fixedPhrase.replace('in-the-', '')
    fixedPhrase = fixedPhrase[:-1]

    fileName = "images/" + fixedPhrase + ".svg"
    dwg = svgwrite.Drawing(fileName, profile='full', size=('{}px'.format(size), '{}px'.format(size)) )

    drawThis(phrase, dwg).save()

    f.write(phrase)



f.close()