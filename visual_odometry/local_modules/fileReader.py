import csv
from local_modules.localCalc import distCalc

def fileRead(file_path):
    areas = []
    lengths = []
    widths = []
    
    with open(file_path, 'r') as data:
        reader = csv.reader(data)
        next(reader)
        for row in reader:
            if row[1] == '' or row[3] == '' or row[5] == '':
                continue
            else:
                for i,item in enumerate(row):
                    row[i] = int(item)

                # will return length(green-yellow) and width(pink-yellow)
                length, width = distCalc(row)

                # calculate area
                area = length * width
                
                # appending areas and distances
                areas.append(area)
                lengths.append(length)
                widths.append(width)

    return areas, lengths, widths