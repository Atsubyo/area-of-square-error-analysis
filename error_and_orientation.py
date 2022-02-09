from local_modules.histogram_grapher import histoGrapher
from local_modules.localCalc import avgCalc, stErrCalc
from local_modules.fileReader import fileRead

# will read through csv file & return average area, & lists for lengths & widths
areas, lengths, widths = fileRead('csv_files/data.csv')

# calculates and outputs average of areas, area of averages, average length, average width
avgCalc(lengths, widths, areas)

# calculates and outputs standard error of length, width, area
stErrCalc(lengths, widths, areas)

# histogram for green-yellow distances(length)
histoGrapher(lengths, 'lengths_histogram')

# histogram for pink-yellow distances(width)
histoGrapher(widths, 'widths_histogram')