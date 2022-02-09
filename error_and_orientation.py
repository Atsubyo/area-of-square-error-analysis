import csv
import statistics as stat
from math import sqrt
import matplotlib.pyplot as plt

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

      # distance green and yellow
      green_yellow_dist = sqrt(green_yellow_x**2 + green_yellow_y**2)

      # distance pink and yellow
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
fig = plt.figure(figsize=(10,6))
n, bins, patches = plt.hist(green_yellow_dists, bins=10, histtype='bar', ec='black')
plt.title('Distance between green and yellow points')
plt.xlabel('Distance (pixels)')
plt.ylabel('Frequency')
plt.xticks(bins)
plt.savefig('green_yellow_histogram')

# histogram for pink-yellow distances(width)
fig = plt.figure(figsize=(10,6))
n, bins, patches = plt.hist(pink_yellow_dists, bins=10, histtype='bar', ec='black')
plt.title('Distance between pink and yellow points')
plt.xlabel('Distance (pixels)')
plt.ylabel('Frequency')
plt.xticks(bins)
plt.savefig('pink_yellow_histogram')

print('Area calculated by averaging the area from each leg:', stat.mean(areas))
print('Area calculated from averaging each leg and multiplying them:', area_avg_wl)
print('Average length: ', green_yellow_avg)
print('Average width: ', pink_yellow_avg)
