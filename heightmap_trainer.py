from generate_text import generate 

from draw_heightmap import drawThis, fillWithTrees

import numpy as np

from PIL import Image

import svgwrite
# from dictionaries import getSize
from csv import DictWriter
import pandas as pd
import random
from process_text import process_paragraph

#f = csv.writer(open('output.csv', 'w'))

fieldNames = ['File Name', 'Phrase', 'Road', 'River', 'Lake', 'Forest', 'Mountain']
#road, river, lake, forest, mountain

# size = getSize()

def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)

def upgradeCSV(fileName, fieldNames):
    df = pd.read_csv(fileName, header=None)
    df.rename(columns={0: fieldNames[0], 1:fieldNames[1], 2: fieldNames[2], 3: fieldNames[3], 4: fieldNames[4], 5: fieldNames[5], 6: fieldNames[6]}, inplace=True)
    df.to_csv('output1.csv', index=False)


for imgNum in range(1335,3000):

    #generate multiple lines with this code:
    numPhrases = random.randint(1, 10)
    paragraph = ""
    for i in range(0, numPhrases):
        paragraph = paragraph + generate()

    phrases = process_paragraph(paragraph)

    phrases = phrases.split("Draw")[1:]

    phrases = [phrases[i].strip() for i in range(len(phrases))]

    fileName = "heightmap_images/{}.png".format(imgNum)

    color_world, img_details, forest = drawThis(phrases, fileName)    

    array = np.array(color_world, dtype=np.uint8)

    new_image = Image.fromarray(array)
    new_image.save(fileName)

    if forest:
        new_image = fillWithTrees(fileName, forest[0], forest[1])
        new_image.save(fileName)
    
    print(imgNum)

    append_dict_as_row('output.csv', img_details, fieldNames)

    upgradeCSV('output.csv', fieldNames)

    


