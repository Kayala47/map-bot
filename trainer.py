from generate_text import generate 
from draw import drawThis
import svgwrite
from dictionaries import getSize
import csv

f = csv.writer(open('output.csv', 'w'))
imgDict = {}

size = getSize()

for i in range(0,10):
    phrase = generate()

    fixedPhrase = phrase.replace(" ", "-")
    fixedPhrase = fixedPhrase.replace('Draw-a-', '')
    fixedPhrase = fixedPhrase.replace('in-the-', '')
    fixedPhrase = fixedPhrase[:-1]

    fileName = "images/" + fixedPhrase + ".svg"
    dwg = svgwrite.Drawing(fileName, profile='full', size=('{}px'.format(size), '{}px'.format(size)) )

    drawThis(phrase, dwg).save()
    
    imgDict[phrase] = fileName

    

for key, val in imgDict.items():
    f.writerow([key, val])

