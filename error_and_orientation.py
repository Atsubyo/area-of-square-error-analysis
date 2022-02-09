import csv
from statistics import mean
from local_modules.histogram_grapher import histoGrapher
from local_modules.calculator import avglwArea, stError
from local_modules.fileReader import fileRead

with open('csv_files/data.csv', 'r') as data:
    reader = csv.reader(data)
    next(reader)
    avg_areas, lengths, widths = fileRead(reader)

avg_lw_area, len_avg, wid_avg = avglwArea(lengths, widths)

# histogram for green-yellow distances(length)
histoGrapher(lengths, 'lengths_histogram')

# histogram for pink-yellow distances(width)
histoGrapher(widths, 'widths_histogram')

# Standard error of length values
len_stError = stError(data_set = lengths)

# Standard error of width values
wid_stError = stError(data_set = widths)

# Standard error of area values
area_stError = stError(data_set = avg_areas)

print('Area calculated by averaging the area from each leg:', mean(avg_areas))
print('Area calculated from averaging each leg and multiplying them:', avg_lw_area)
print('Average length: ', len_avg)
print('Average width: ', wid_avg)
print('Length Standard Error: ', len_stError)
print('Width Standard Error: ', wid_stError)
print('Area Standard Error: ', area_stError)