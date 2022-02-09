from cmath import sqrt
from statistics import stdev

def stError(data_set):
    size = len(data_set)
    stdErr = stdev(data_set)/(size**0.5)
    return stdErr