#Read write and parse csv file

import csv

with open ('Desktop/names.txt','r') as nfile:
    csv_reader=csv.DictReader(nfile)

    with open ('Desktop/n_names.txt','w') as wfile:
        fieldnames=['First_Name','Last_Name']

        csv_writer=csv.DictWriter(wfile,fieldnames=fieldnames,delimiter='|')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email_id']
            csv_writer.writerow(line)
            
