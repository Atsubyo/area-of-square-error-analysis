import matplotlib.pyplot as plt

def histoGrapher(data_set, png_file_save):
    fig = plt.figure(figsize=(10,6))
    n, bins, patches = plt.hist(data_set, bins=10, histtype='bar', ec='black')
    plt.title('Distance between green and yellow points')
    plt.xlabel('Distance (pixels)')
    plt.ylabel('Frequency')
    plt.xticks(bins)
    plt.savefig('saved_plots/{}'.format(png_file_save))