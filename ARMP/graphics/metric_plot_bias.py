from lib.loader import dic
from lib.control import iter_list
from utils.portrait_plot import metric_plot
from io.input import read_json_file, extract_dict
from matplotlib import pyplot as plt
import os


def metric_plot_bias(matrix, xaxis_labels, yaxis_labels, cbar_label,
                      title, fig_filename, fig_dir):

    maxvalue = np.max(matrix)
    minvalue = np.min(matrix)
    maxvalue = max(maxvalue, minvalue*-1)
    minvalue = maxvalue*-1

    fig = plt.figure(figsize =([8.5, 8.5]))

    fig, ax, im, cbar = \
                    metric_plot(matrix,
                    fig = fig,
                    xaxis_labels=xaxis_labels,
                    yaxis_labels=yaxis_labels,
                    annotate=True,
                    annotate_format = "{x:d}",
                    annotate_textcolors_threshold = (minvalue*0.7, maxvalue*0.7),
                    annotate_fontsize=10,
                    cmap="RdBu_r",
                    cbar_label=cbar_label,
                    vrange = (minvalue, maxvalue),
                    box_as_square=True)
    

    ax.set_title( title, fontsize=20, color="black")

    #ax.axvline(x=2, color='k', linewidth = 3)
    
    plt.tight_layout()

    plt.subplots_adjust(left=0.2, right=0.95, top=0.75, bottom=0.03)

    plt.savefig(os.path.join(fig_dir, fig_filename, '.png'), dpi=300)

    plt.close()



if __name__ == "__main__":

    # set metrics for plotting
    model_list = dic['model_lsit'][1:]
    ARDT_list = dic['ARDT_lsit'][0]
    region_list = dic['region_lsit']
    season_list = dic['season_lsit'][0]

    metric_layout = list([model_list, ARDT_list, region_list, season_list])
    metric_var = 'bias'
    metric = 'metric_peak_day_bias'

    # load metrics value
    dict_in = read_json_file(dic, metric)
    metric_value = extract_dict(dict_in['RESULTS'], metric_layout, metric_var)

    # format and rotate metrics matrix if necessary
    matrix = metric_value.T.astype(int)


    # metric plot setting 
    xaxis_labels = model_list
    yaxis_labels = region_list

    fig_dir = dic['dir_fig']
    cbar_label='peak day bias'
    title = 'landfalling AR peak day bias'
    fig_filename = 'AR_peak_day_bias'


    metric_plot_bias(matrix, xaxis_labels, yaxis_labels, cbar_label,
                      title, fig_filename, fig_dir)

