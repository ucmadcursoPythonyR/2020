import matplotlib.pyplot as plt
import numpy as np

def barplot(x_data, y_data, x_label="", y_label="", title="",color="#539caf",sizeh=5,sizev=5):
    _, ax = plt.subplots(figsize=(sizeh,sizev))# Creación del objeto
    ax.barh(x_data, y_data, color = color, align = 'center') #capas
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

def stackedbarplot(x_data, y_data_list, colors, y_data_names=["Data1","Data2"], x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    for i in range(0, len(y_data_list)):
        if i == 0:
            ax.bar(x_data, y_data_list[i], color = colors[i], align = 'center', label = y_data_names[i])
        else:
            ax.bar(x_data, y_data_list[i], color = colors[i], bottom = y_data_list[i-1], align = 'center', label = y_data_names[i])
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'upper right')
def groupedbarplot(x_data, y_data_list, colors, y_data_names=["Data1","Data2"], x_label="", y_label="", title=""):
    x_ax=np.arange(len(x_data))
    _, ax = plt.subplots()
    # Total width for all bars at one x location
    total_width = 0.8
    # Width of each individual bar
    ind_width = total_width / len(y_data_list)
    # This centers each cluster of bars about the x tick mark
    alteration = np.arange(-(total_width/2), total_width/2, ind_width)

    # Draw bars, one category at a time
    for i in range(0, len(y_data_list)):
        # Move the bar to the right on the x-axis so it doesn't
        # overlap with previously drawn ones
        ax.bar(x_ax + alteration[i], y_data_list[i], color = colors[i],label = y_data_names[i],width = ind_width)
    plt.xticks(x_ax-ind_width/2, x_data),
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'upper right')
def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r", yscale_log=False,s=10):

    # Create the plot object
    _, ax = plt.subplots()


    ax.scatter(x_data, y_data, s = s, color = len(y_data)//len(color)*color+color[0:len(y_data)%len(color)], alpha = 0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
def lineplot(x_data, y_data, x_label="", y_label="", title="",color='#539caf', ancholinea=2):
    _, ax = plt.subplots()

    ax.plot(x_data, y_data, lw = ancholinea, color = color, alpha = 1)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
from matplotlib import colors
def histogram(data, n_cajas=5, cumulative=False, x_label = "", y_label = "", title = "", color = '#539caf'):
    _, ax = plt.subplots()
    ax.hist(data, bins =n_cajas, cumulative = cumulative, color = color)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
def boxplot(x_labeld, y_data, base_color="#539caf", median_color="#297083", x_label="", y_label="", title=""):
    _, ax = plt.subplots()

    # Draw boxplots, specifying desired style
    ax.boxplot(y_data
               # patch_artist must be True to control box fill
               , patch_artist = True
               # Properties of median line
               , medianprops = {'color': median_color}
               # Properties of box
               , boxprops = {'color': base_color, 'facecolor': base_color}
               # Properties of whiskers
               , whiskerprops = {'color': base_color}
               # Properties of whisker caps
               , capprops = {'color': base_color})

    # By default, the tick label starts at 1 and increments by 1 for
    # each box drawn. This sets the labels to the ones we want
    ax.set_xticklabels(x_labeld)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
