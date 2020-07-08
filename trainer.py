from generate_text import generate 
from draw import drawThis
import svgwrite
from dictionaries import getSize
from csv import DictWriter
import pandas as pd
import random
from process_text import process_paragraph

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


for imgNum in range(0,1000):

    #generate multiple lines with this code:
    numPhrases = random.randint(1, 10)
    paragraph = ""
    for i in range(0, numPhrases):
        paragraph = paragraph + generate()

    phrases = process_paragraph(paragraph)

    phrases = phrases.split("Draw")[1:]

    phrases = [phrases[i].strip() for i in range(len(phrases))]

    fileName = "images/{}.svg".format(imgNum)
    dwg = svgwrite.Drawing(fileName, profile='full', size=('{}px'.format(size), '{}px'.format(size)) )


    drawnImg, imgDetails = drawThis(phrases, dwg, fileName)

    drawnImg.save()
    #imgDict[phrase] = fileName

    append_dict_as_row('output.csv', imgDetails, fieldNames)

    upgradeCSV('output.csv', fieldNames)

    


