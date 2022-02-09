import csv
import statistics as stat
from math import sqrt
from local_modules.histogram_grapher import histoGrapher
from local_modules.calculator import stError

areas = []
green_yellow_dists = []
pink_yellow_dists = []

with open('data.csv', 'r') as data:
    reader = csv.reader(data)
    for row in reader:
        if row[1] == '' or row[3] == '' or row[5] == '':
            continue
        elif row[0] == 'frame_no':
            continue
        else:
            for i,item in enumerate(row):
                row[i] = int(item)
            # x diff of green and yellow
            green_yellow_x = abs(row[1] - row[5])
            
            # y diff of green and yellow
            green_yellow_y = abs(row[2] - row[6])
            
            # x diff of pink and yellow
            pink_yellow_x = abs(row[3] - row[5])
            
            # y diff of pink and yellow
            pink_yellow_y = abs(row[4] - row[6])

            # distance green and yellow (length)
            green_yellow_dist = sqrt(green_yellow_x**2 + green_yellow_y**2)

            # distance pink and yellow (width)
            pink_yellow_dist = sqrt(pink_yellow_x**2 + pink_yellow_y**2)

            # calculate area
            area = green_yellow_dist * pink_yellow_dist
            
            # appending areas and distances
            areas.append(area)
            green_yellow_dists.append(green_yellow_dist)
            pink_yellow_dists.append(pink_yellow_dist)

pink_yellow_avg = stat.mean(pink_yellow_dists)
green_yellow_avg = stat.mean(green_yellow_dists)
area_avg_wl = pink_yellow_avg * green_yellow_avg

# histogram for green-yellow distances(length)
histoGrapher(green_yellow_dists, 'green_yellow_histogram')

# histogram for pink-yellow distances(width)
histoGrapher(pink_yellow_dists, 'pink_yellow_histogram')

# Standard deviation of length values
len_stError = stError(green_yellow_dists)

# Standard deviation of width values
wid_stError = stError(pink_yellow_dists)

# Standard deviation of area values
area_stError = stError(areas)

print('Area calculated by averaging the area from each leg:', stat.mean(areas))
print('Area calculated from averaging each leg and multiplying them:', area_avg_wl)
print('Average length: ', green_yellow_avg)
print('Average width: ', pink_yellow_avg)
print('Length Standard Error: ', len_stError)
print('Width Standard Error: ', wid_stError)
print('Area Standard Error: ', area_stError)