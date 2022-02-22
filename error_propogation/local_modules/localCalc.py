from statistics import stdev, mean
from math import sqrt
from types import NoneType
    
# calculates and outputs standard error
def stErrCalc(lengths, widths, areas):
    # Standard area of length
    size = len(lengths)
    len_stError = stdev(lengths)/(size**0.5)
    # Standard area of width
    size = len(widths)
    wid_stError = stdev(widths)/(size**0.5)
    # Standard error of statistical area
    size = len(areas)
    area_stError = stdev(areas)/(size**0.5)
    # Standard error of propagated area
    avg_area, len_avg, wid_avg = avgCalc(lengths, widths, areas)
    area_propErr = avg_area * sqrt((len_stError/len_avg)**2 + (wid_stError/wid_avg)**2)

    # output standard/propagated error values
    print('Area (Statistical) Standard Error: ', area_stError)
    print('Area (Propagated) Propagated Error: ', area_propErr)
    print('Length Standard Error: ', len_stError)
    print('Width Standard Error: ', wid_stError)

    return

# calculates and outputs averages
def avgCalc(lens, wids, areas):
    len_avg = mean(lens) # length average
    wid_avg = mean(wids) # width average
    avg_lw_area = len_avg * wid_avg # area from average of each leg
    avg_area = mean(areas) # average of areas for each leg

    # output averages
    print('Area (Propagated):', avg_area)
    print('Area (Statistical):', avg_lw_area)
    print('Average length: ', len_avg)
    print('Average width: ', wid_avg)

    return avg_area, len_avg, wid_avg

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