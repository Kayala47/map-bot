from generate_text import generate 
from draw import drawThis
import svgwrite
from dictionaries import getSize
from csv import DictWriter
import pandas as pd
import random

#f = csv.writer(open('output.csv', 'w'))

fieldNames = ['File Name', 'Phrase', 'Road', 'River', 'Lake', 'Forest']

size = getSize()

def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)

def upgradeCSV(fileName, fieldNames):
    df = pd.read_csv(fileName, header=None)
    df.rename(columns={0: fieldNames[0], 1:fieldNames[1], 2: fieldNames[2], 3: fieldNames[3], 4: fieldNames[4], 5: fieldNames[5]}, inplace=True)
    df.to_csv('output1.csv', index=False)


for i in range(0,10):

    #generate multiple lines with this code:
    numPhrases = random.randint(1, 10)
    paragraph = ""
    for i in range(0, numPhrases):
        paragraph = paragraph + generate()

    phrase = generate()

    fixedPhrase = phrase.replace(" ", "-")
    fixedPhrase = fixedPhrase.replace('Draw-a-', '')
    fixedPhrase = fixedPhrase.replace('in-the-', '')
    fixedPhrase = fixedPhrase[:-1]

    fileName = "images/" + fixedPhrase + ".svg"
    dwg = svgwrite.Drawing(fileName, profile='full', size=('{}px'.format(size), '{}px'.format(size)) )

    drawnImg, imgDetails = drawThis(phrase, dwg, fileName)

    drawnImg.save()
    #imgDict[phrase] = fileName

    append_dict_as_row('output.csv', imgDetails, fieldNames)

    upgradeCSV('output.csv', fieldNames)

    


