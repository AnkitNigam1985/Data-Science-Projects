import csv

with open('sample_data.csv', 'r') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')

    with open('mobile_data.csv', 'w') as new_file:
        csv_writer=csv.writer(new_file, delimiter='-')
        for line in csv_reader:
            #print(line)
            csv_writer.writerow(line)


#Dictionary reader - preferred way
with open('sample_data.csv', 'r') as csv_file:
    csv_reader=csv.DictReader(csv_file)

    with open('new_dict_sample.csv', 'w') as new_file:
        fieldnames = ['event_id', 'device_id','timestamp', 'longitude', 'latitude', 'state']
        csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
    #for line in csv_reader:
     #   print(line)
        for line in csv_reader:
            del line['state']
            csv_writer.writerow(line)
