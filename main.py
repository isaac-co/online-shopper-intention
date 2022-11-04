import csv



data_set = []

#csv reader
with open('datasets/online_shoppers_intention.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in reader:
        #skips first line
        if line_count == 0:
            line_count += 1
        else:
            data_set.append(row)

print(len(data_set))