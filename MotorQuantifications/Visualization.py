def create_plot(param_values, title_value, entity_value, figure_title):
    '''Creates separate plots from manually entered values'''
    param_plot = params[param_values].plot(figsize=(20,5), title=figure_title, grid = pref_grid_visible)
    param_plot.set_xlabel('Time (seconds)')
    param_plot.set_ylabel(title_value + ' (' + entity_value + ')')
    plt.legend(['X', 'Y', 'Z'], loc=1)
    
    if pref_save_figures:
        plt.savefig('fig_' + title_value.lower().replace(' ', '_') + '.png', dpi=300)
    
    return param_plot
# Create individual plots
create_plot(['accX', 'accY', 'accZ'], 'Acceleration', 'G','Acceleration(G) vs Time(seconds)')
create_plot(['roll', 'pitch', 'yaw'], 'Rotation', 'degrees','Rotation(degrees) vs Time(seconds)')
create_plot(['rotX', 'rotY', 'rotZ'], 'Rotation speed', 'd / second','Rotation Speed (d/second) vs Time(seconds)')
if pref_plot_gravity:
    create_plot(['gravX', 'gravY', 'gravZ'], 'Gravity', 'G','NULL')

   
