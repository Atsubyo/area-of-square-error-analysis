from math import sqrt

def fileRead(reader):
    areas = []
    lengths = []
    widths = []
    
    for row in reader:
        if row[1] == '' or row[3] == '' or row[5] == '':
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
            lengths.append(green_yellow_dist)
            widths.append(pink_yellow_dist)
    return areas, lengths, widths