from generate_text import generate 

f = open('output.txt', 'w')

for i in range(1,1000):
    f.write(generate())

f.close()