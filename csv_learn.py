import csv

##with open('names.csv.txt','r') as csv_file:
##  csv_reader=csv.reader(csv_file)
##  next(csv_reader)
##  for line in csv_reader:
##    print(line[0],"\t",line[1],"\t",line[2])

##with open('names.csv.txt','r') as crf:
##  csv_reader=csv.reader(crf)
##  with open('newnames.csv.txt','w') as cwf:
##    csv_writer=csv.writer(cwf,delimiter='|')
##    for line in csv_reader:
##      csv_writer.writerow(line)

##with open('newnames.csv.txt','r') as crf:
##  csv_reader=csv.reader(crf,delimiter='|')
##  for line in csv_reader:
##    print(line)

##with open('names.csv.txt','r') as crf:
##  csv_reader=csv.DictReader(crf)
##  for line in csv_reader:
##    print(line['first_name'],'|',line['last_name'],'|',line['email'])

with open('names.csv.txt','r') as crf:
  csv_reader=csv.DictReader(crf)
  with open('Copy_names.txt','w') as cwf:
    fieldnames=['first_name','last_name','email']
    csv_writer=csv.DictWriter(cwf,fieldnames=fieldnames,delimiter='|')
    csv_writer.writeheader()
    for line in csv_reader:
      del line['last_name']
      csv_writer.writerow(line)
