import pandas as pd 
import seaborn as sns 
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, NumeralTickFormatter

data_frame = pd.read_csv('data.csv')

df1 = pd.DataFrame(data_frame, columns=['Name', 'Overall', 'Wage', 'Value', 'Position'])

def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000 
    
    if 'M' in x: 
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000

wage = df1['Wage'].replace('[\€,]', '', regex=True).apply(value_to_float)
value = df1['Value'].replace('[\€,]', '', regex=True).apply(value_to_float)

df1['Wage'] = wage
df1['Value'] = value

sns.set()

graph = sns.scatterplot(x='Wage', y='Value', data=df1)

TOOLTIPS = HoverTool(tooltips=[
    ('Name', '@Name'),
    ('Overall', '@Overall'),
    ('Position', '@Position'),
    ('Wage', '@Wage{($0.00a)}'),
    ('Value', '@Value{($0.00a)}')
    ])

plot = figure(
    title = 'Fifa 19 Wage vs. Value', 
    x_axis_label = 'Wage (Weekly)', 
    y_axis_label = 'Player Value', 
    plot_width = 700, 
    plot_height = 700,
    tools = [TOOLTIPS, 'pan, wheel_zoom, box_zoom, reset, save'],
    toolbar_location = 'above'
    )

plot.circle(
    'Wage', 
    'Value',
    size = 10,
    fill_alpha = 0.8,
    line_color = 'blue',
    source = df1
    )

# Format X and Y axis into readable format
plot.xaxis.formatter = NumeralTickFormatter(format = '($0.00a)')
plot.yaxis.formatter = NumeralTickFormatter(format = '($0.00a)')

# Hide toolbar until hover on scatterplot
plot.toolbar.autohide = True

# Output scatterplot to external HTML file and save
output_file('output/fifa19_wage_value.html', title = 'Fifa 19 Wage vs. Value', mode = 'inline')

# Display the scatterplot
show(plot)