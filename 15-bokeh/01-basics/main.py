
from bokeh.plotting import figure, show
from bokeh.layouts import row


#* Create a single line chart

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# create a new plot with a title and axis labels
single_chart = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")

# add a line renderer with legend and line thickness
single_chart.line(x, y, legend_label="Temp.", line_width=2)



#* Combining multiple graphs

x1 = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

multi_graph = figure(title="Multiple line example", x_axis_label='x', y_axis_label='y')

# Add multiple renders
multi_graph.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
multi_graph.line(x, y2, legend_label="Rate", color="red", line_width=2)
multi_graph.line(x, y3, legend_label="Objects", color="green", line_width=2)

# show the results
show(row(single_chart, multi_graph)) 
# show(multi_graph)