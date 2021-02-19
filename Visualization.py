def create_plot(param_values, title_value, entity_value, figure_title):
    '''Creates separate plots from manually entered values'''
    param_plot = params[param_values].plot(figsize=(20,5), title=figure_title, grid = pref_grid_visible)
    param_plot.set_xlabel('Time (seconds)')
    param_plot.set_ylabel(title_value + ' (' + entity_value + ')')
    plt.legend(['X', 'Y', 'Z'], loc=1)
    
    if pref_save_figures:
        plt.savefig('fig_' + title_value.lower().replace(' ', '_') + '.png', dpi=300)
    
    return param_plot
   
