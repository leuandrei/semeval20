import numpy as np
import matplotlib.pyplot as plt
import re
import csv

with open('train.csv',  encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)

    #parse input data
    for line in  csv_reader:
        #print(line[1], line[2], line[4])

        #print(re.match('<.*\/>', line[1]))

        #Obtained edited headline
        line[1] = re.sub('<.*\/>',
                  line[2],
                  line[1])
        plt.show
        print(line[1], line[4])