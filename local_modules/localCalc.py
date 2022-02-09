from statistics import stdev, mean
from math import sqrt
    
# calculates and outputs standard error
def stErrCalc(lengths, widths, areas):
    # Standard area of length
    size = len(lengths)
    len_stError = stdev(lengths)/(size**0.5)
    # Standard area of width
    size = len(widths)
    wid_stError = stdev(widths)/(size**0.5)
    # Standard error of area
    size = len(areas)
    area_stError = stdev(areas)/(size**0.5)

    # output standard error values
    print('Length Standard Error: ', len_stError)
    print('Width Standard Error: ', wid_stError)
    print('Area Standard Error: ', area_stError)

    return

# calculates and outputs averages
def avgCalc(lens, wids, areas):
    len_avg = mean(lens) # length average
    wid_avg = mean(wids) # width average
    avg_lw_area = len_avg * wid_avg # area from average of each leg
    avg_area = mean(areas) # average of areas for each leg

    # output averages
    print('Average of areas for each leg (Method 1):', avg_area)
    print('Area from average of each leg (Method 2):', avg_lw_area)
    print('Average length: ', len_avg)
    print('Average width: ', wid_avg)

    return

# calculates the distances between each point for length and width values
def distCalc(row):
    # x diff of green and yellow
    green_yellow_x = abs(row[1] - row[5])
    
    # y diff of green and yellow
    green_yellow_y = abs(row[2] - row[6])

    # x diff of pink and yellow
    pink_yellow_x = abs(row[3] - row[5])
    
    # y diff of pink and yellow
    pink_yellow_y = abs(row[4] - row[6])

    # distance green and yellow (length)
    length = sqrt(green_yellow_x**2 + green_yellow_y**2)

    # distance pink and yellow (width)
    width = sqrt(pink_yellow_x**2 + pink_yellow_y**2)

    return length, width