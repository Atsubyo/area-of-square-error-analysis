from statistics import stdev, mean

def stError(data_set):
    size = len(data_set)
    stdErr = stdev(data_set)/(size**0.5)
    return stdErr

def avglwArea(lens, wids):
    len_avg = mean(lens)
    wid_avg = mean(wids)
    area_avg_lw = len_avg * wid_avg
    return area_avg_lw, len_avg, wid_avg