#Read,write and parse csv files

import csv

with open ('Desktop/names.txt','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    with open ('Desktop/new_names.txt','w') as new_file:
        csv_writer=csv.writer(new_file,delimiter='|')

        for line in csv_reader:
            csv_writer.writerow(line)
        

        
