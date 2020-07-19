# To-do List
As of 7/6/2020

## Generating Images and Text

- add color filter to loaded images
- road network generation for roads/rivers
    - cheap techniques, you can even have it avoid other features
    - for rivers: generate heightmap, then make sure they only flow downwards. Makes a random choice in the event of tie. Can end in lake or go off side of screen
- heightmap generation; perlin noise heightmap generation, fractal brownian motion
    - tweak heightmap for shallower banks, depressions to put water in. Rivers can create a channel where we need
        - to represent height, maybe a gradient fill. Topographical map with contours. Simpler would be to approximate contours using ellipses
        - heightlines based off a point
        ^this is all more geared towards pixels
    - add beaches to lakes
    - generate roads and rivers


### Optional ###
- add curves to rivers
- change rivers/roads to be their own separate grammar, taking in start & endpts
- change generation so that it accepts x,y locations

## ML
- meet with Prof. Osborn Wed 7/8 @ 12pm for next steps and discussion
- instead of teaching the network to generate img from phrase, you could instead have a network that generates images and a network that tells you if an image is of a phrase. GAN - train them both together.  
    - your model: input is an image and output is a caption. Image synthesis from text; look it up! Score for how well it fits, probably along several different features. 
- VAE could also work
