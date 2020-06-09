from generate_text import generate 
from draw import drawThis
import svgwrite

f = open('output.txt', 'w')

for i in range(0,4):
    phrase = generate()

    fixedPhrase = phrase.replace(" ", "-")
    fixedPhrase = fixedPhrase.replace('Draw-a-', "")
    fixedPhrase = fixedPhrase.replace('in-the-', '')
    fixedPhrase = fixedPhrase[:-1]

    fileName = "images/" + fixedPhrase + ".svg"
    dwg = svgwrite.Drawing(fileName, profile='tiny')

    drawThis(phrase, dwg).save()

    f.write(phrase)



f.close()