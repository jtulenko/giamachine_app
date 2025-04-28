from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.models import Span, HoverTool
from bokeh.embed import components
from bokeh.io import output_file, show
import pandas
import numpy
from numpy import array, log, tan, pi
import xyzservices.providers as xyz
import matplotlib


def be_plot(be_result):
    # The input arg is a tuple of (x,y)
    df1 = pandas.DataFrame(list(be_result))
    x = df1[0]
    y = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    data = {'y': array(y),
            'x': array(x),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="Beryllium-10 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[Be-10]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle('x','y', source=data, size=8, fill_color='rgba(247, 74, 74, 1)', fill_alpha=0.6, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"), ("Lab", "@lab"),("Error (%)", "@y")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]


def be_plot2(be_result1, be_result2):
    #The input arg will need be two tuples of (x,y)
    df1 = pandas.DataFrame(list(be_result1))
    x1 = df1[0]
    y1 = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    df2 = pandas.DataFrame(list(be_result2))
    x2 = df2[0]
    y2 = 100 * df2[1] / df2[0]

    data = {'x1': array(x1),
            'y1': array(y1),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="Beryllium-10 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[Be-10]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle(x2,y2, size=6, fill_color='grey', fill_alpha=0.1, line_color='grey', line_alpha=0.1)
    p.circle('x1','y1', source=data, size=8, fill_color='rgba(247, 74, 74, 1)', fill_alpha=0.9, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Lab", "@lab"),("Error (%)", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]



def al_plot(al_result):
    # The input arg is a tuple of (x,y)
    df1 = pandas.DataFrame(list(al_result))
    x = df1[0]
    y = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    data = {'y': array(y),
            'x': array(x),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="Aluminum measurements-26 in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[Al-26]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle('x','y', source=data, size=8, fill_color='rgba(64, 144, 230, 1)', fill_alpha=0.6, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"), ("Lab", "@lab"),("Error (%)", "@y")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]


def al_plot2(al_result1, al_result2):
    #The input arg will need be two tuples of (x,y)
    df1 = pandas.DataFrame(list(al_result1))
    x1 = df1[0]
    y1 = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    df2 = pandas.DataFrame(list(al_result2))
    x2 = df2[0]
    y2 = 100 * df2[1] / df2[0]

    data = {'x1': array(x1),
            'y1': array(y1),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="Aluminum-26 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[Al-26]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle(x2,y2, size=6, fill_color='grey', fill_alpha=0.1, line_color='grey', line_alpha=0.1)
    p.circle('x1','y1', source=data, size=8, fill_color='rgba(64, 144, 230, 1)', fill_alpha=0.9, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Lab", "@lab"),("Error (%)", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]



def c_plot(c_result):
    # The input arg is a tuple of (x,y)
    df1 = pandas.DataFrame(list(c_result))
    x = df1[0]
    y = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    data = {'y': array(y),
            'x': array(x),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="In-situ Carbon-14 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[C-14]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle('x','y', source=data, size=8, fill_color='rgba(255, 168, 38, 1)', fill_alpha=0.6, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"), ("Lab", "@lab"),("Error (%)", "@y")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]


def c_plot2(c_result1, c_result2):
    #The input arg will need be two tuples of (x,y)
    df1 = pandas.DataFrame(list(c_result1))
    x1 = df1[0]
    y1 = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    df2 = pandas.DataFrame(list(c_result2))
    x2 = df2[0]
    y2 = 100 * df2[1] / df2[0]

    data = {'x1': array(x1),
            'y1': array(y1),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="In-situ Carbon-14 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[C-14]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle(x2,y2, size=6, fill_color='grey', fill_alpha=0.1, line_color='grey', line_alpha=0.1)
    p.circle('x1','y1', source=data, size=8, fill_color='rgba(255, 168, 38, 1)', fill_alpha=0.9, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Lab", "@lab"),("Error (%)", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]



def hepxol_plot(he1_result):
    # The input arg is a tuple of (x,y)
    df1 = pandas.DataFrame(list(he1_result))
    x = df1[0]
    y = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    data = {'y': array(y),
            'x': array(x),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="He-3 measurements from Px/Ol in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[He-3]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle('x','y', source=data, size=8, fill_color='rgba(153, 153, 153, 1)', fill_alpha=0.6, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"), ("Lab", "@lab"),("Error (%)", "@y")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]


def hepxol_plot2(he1_result1, he1_result2):
    #The input arg will need be two tuples of (x,y)
    df1 = pandas.DataFrame(list(he1_result1))
    x1 = df1[0]
    y1 = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    df2 = pandas.DataFrame(list(he1_result2))
    x2 = df2[0]
    y2 = 100 * df2[1] / df2[0]

    data = {'x1': array(x1),
            'y1': array(y1),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="He-3 measurements from Px/Ol in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[He-3]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle(x2,y2, size=6, fill_color='grey', fill_alpha=0.1, line_color='grey', line_alpha=0.1)
    p.circle('x1','y1', source=data, size=8, fill_color='rgba(153, 153, 153, 1)', fill_alpha=0.9, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Lab", "@lab"),("Error (%)", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]



def heqtz_plot(he2_result):
    # The input arg is a tuple of (x,y)
    df1 = pandas.DataFrame(list(he2_result))
    x = df1[0]
    y = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    data = {'y': array(y),
            'x': array(x),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="He-3 measurements from Quartz in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[He-3]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle('x','y', source=data, size=8, fill_color='rgba(199, 199, 199, 1)', fill_alpha=0.6, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"), ("Lab", "@lab"),("Error (%)", "@y")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]


def heqtz_plot2(he2_result1, he2_result2):
    #The input arg will need be two tuples of (x,y)
    df1 = pandas.DataFrame(list(he2_result1))
    x1 = df1[0]
    y1 = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    df2 = pandas.DataFrame(list(he2_result2))
    x2 = df2[0]
    y2 = 100 * df2[1] / df2[0]

    data = {'x1': array(x1),
            'y1': array(y1),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="He-3 measurements from Quartz in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[He-3]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle(x2,y2, size=6, fill_color='grey', fill_alpha=0.1, line_color='grey', line_alpha=0.1)
    p.circle('x1','y1', source=data, size=8, fill_color='rgba(199, 199, 199, 1)', fill_alpha=0.9, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Lab", "@lab"),("Error (%)", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]



def cl_plot(cl_result):
    #The input arg is a tuple of (x,y,z)
    df1 = pandas.DataFrame(list(cl_result))
    x = df1[0]
    y = 100 * df1[2] / df1[1]
    name = df1[3]
    lab = df1[4]

    data = {'y': array(y),
            'x': array(x),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="Cl-36 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[Cl-36]"
    p.yaxis.axis_label = "Exposure age internal error (%)"

    p.circle('x','y', source=data, size=8, fill_color='rgba(154, 86, 166, 1)', fill_alpha=0.6, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"), ("Lab", "@lab"),("Error (%)", "@y")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]

def cl_plot2(cl_result1, cl_result2):
    #The input arg will need to be two tuples of (x,y,z)
    df1 = pandas.DataFrame(list(cl_result1))
    x1 = df1[0]
    y1 = 100 * df1[2] / df1[1]
    name = df1[3]
    lab = df1[4]

    df2 = pandas.DataFrame(list(cl_result2))
    x2 = df2[0]
    y2 = 100 * df2[2] / df2[1]

    data = {'x1': array(x1),
            'y1': array(y1),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="Cl-36 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[Cl-36]"
    p.yaxis.axis_label = "Exposure age internal error (%)"

    p.circle(x2,y2, size=6, fill_color='gray', fill_alpha=0.1, line_color="grey", line_alpha=0.1)
    p.circle('x1','y1', source=data, size=8, fill_color='rgba(154, 86, 166, 1)', fill_alpha=0.9, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Lab", "@lab"),("Error (%)", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]



def ne_plot(ne_result):
    #The input arg is a tuple of (x,y,name,lab)
    df1 = pandas.DataFrame(list(ne_result))
    x = df1[0]
    y= 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    data = {'y': array(y),
            'x': array(x),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="Ne-21 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[Ne-21]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle('x','y', source=data, size=8, fill_color='rgba(239, 255, 64, 1)', fill_alpha=0.6, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"), ("Lab", "@lab"),("Error (%)", "@y")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]


def ne_plot2(ne_result1, ne_result2):
    #The input arg will need be two tuples of (x,y)
    df1 = pandas.DataFrame(list(ne_result1))
    x1 = df1[0]
    y1 = 100 * df1[1] / df1[0]
    name = df1[2]
    lab = df1[3]

    df2 = pandas.DataFrame(list(ne_result2))
    x2 = df2[0]
    y2 = 100 * df2[1] / df2[0]


    data = {'x1': array(x1),
            'y1': array(y1),
            'name': array(name),
            'lab': array(lab)}

    p= figure(width=400, height=500, x_axis_type="log", title="Ne-21 measurements in ICE-D", y_range=(0,20))
    p.xaxis.axis_label = "[Ne-21]"
    p.yaxis.axis_label = "AMS Measurement error (%)"

    p.circle(x2,y2, size=6, fill_color='grey', fill_alpha=0.1, line_color='grey', line_alpha=0.1)
    p.circle('x1','y1', source=data, size=8, fill_color='rgba(239, 255, 64, 1)', fill_alpha=0.9, line_color="grey", line_width=0.5)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Lab", "@lab"),("Error (%)", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]

def ratio_elv_plot(result):
    #The input arg will be one tuple of (x,y,z,y_min,z_min)
    df1 = pandas.DataFrame(list(result))

    x1= df1[2]
    y1= df1[1] / df1[0]
    y_min= y1 - (((df1[3] / df1[0])**2) + ((df1[4] / df1[1])**2))**0.5
    y_max= y1 + (((df1[3] / df1[0])**2) + ((df1[4] / df1[1])**2))**0.5
    sizes = df1[0] ** (1/4.5)
    name = df1[5]

    data = {'x1': array(x1),
            'y1': array(y1),
            'y_min': array(y_min),
            'y_max': array(y_max),
            'sizes': array(sizes),
            'name': array(name)}


    par = numpy.polyfit(x1, y1, 1, full=True)
    slope=par[0][0]
    intercept=par[0][1]
    y_predicted = [slope*i + intercept  for i in x1]
    correlation_matrix = numpy.corrcoef(x1, y1)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2

    p= figure(width=475, height=500, title="[Al]/[Be] ratio with Elevation", y_range=(4,10))
    p.xaxis.axis_label = "Elevation (m)"
    p.yaxis.axis_label = "[Al]/[Be]"

    p.vbar(x='x1', bottom='y_min', top='y_max', width=1, source=data, line_color='black')
    p.circle('x1', 'y1', size='sizes', source=data, fill_color= 'rgba(220, 208, 255, 1)', fill_alpha=0.9, line_color='grey', line_width=0.5, legend_label = 'size = [10Be] ^ (1/4.5)')
    p.line(x1,y_predicted, color='black',legend_label='y= '+str(round(slope,6))+'x+'+str(round(intercept,2))+'   r^2 ='+str(round(r_squared,6)))
    p.add_tools(HoverTool(tooltips=[("sample name", "@name"),("[Al-26] / [Be-10]", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]

def c14_PR(result):
    #The input arg will be one tuple of (x,y,z,name)
    df1 = pandas.DataFrame(list(result))
    x1 = df1[0] * 0.00012096809
    y1 = df1[1]
    sizes = df1[2] ** (1/4)
    name = df1[3]

    data = {'x1': array(x1),
            'y1': array(y1),
            'sizes': array(sizes),
            'name': array(name)}

    p= figure(width=475, height=500, x_axis_type="log", title="Saturation concentration of in-situ C-14")
    p.xaxis.axis_label = "N * I"
    p.yaxis.axis_label = "Elevation (m)"

    p.circle('x1','y1', size='sizes', source=data, fill_color='rgba(255, 168, 38, 1)', fill_alpha=0.9, line_color='grey', line_alpha=0.1)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Age (ka)", "@sizes"),("N * I", "@x1")]))


    plot_script, plot_div = components(p)

    return [plot_script, plot_div]

def GrIS_TDD(result):
    #The input arg will be one tuple of (x,y,z)
    df1 = pandas.DataFrame(list(result))
    #df1 = df1.replace(result, regex=True).astype('float64')
    x1 = df1[0]
    x1 = x1.astype('float64')
    y1 = (df1[1] / 1.0134) / 1000
    y_min = y1 - ((df1[2] / 1.0134) / 1000)
    y_max = y1 + ((df1[2] / 1.0134) / 1000)
    name = df1[3]

    data = {'x1': array(x1),
            'y1': array(y1),
            'y_min': array(y_min),
            'y_max': array(y_max),
            'name': array(name)}

    p= figure(width=475, height=500, y_range=(16,5), title="Western Greenland longitude versus boulder ages")
    p.xaxis.axis_label = "Longitude (decimal degrees)"
    p.yaxis.axis_label = "Exposure ages using aproximated Arctic PR and St Scaling (ka)"

    events = [9.3, 8.2]

    e1 = Span(location=events[0], dimension='width', line_color='grey', line_alpha=0.5, line_width=20)
    e1.level = 'underlay'

    e2 = Span(location=events[1], dimension='width', line_color='grey', line_alpha=0.5, line_width=20)
    e2.level = 'underlay'

    p.add_layout(e1)
    p.add_layout(e2)
    p.line([],[], line_color='grey', line_alpha=0.5, line_width=20, legend_label= "grey bars = 9.3 and 8.2 ka events")
    p.legend.location = "top_left"

    p.vbar(x='x1', bottom='y_min', top='y_max', source=data, width=.0005, line_color='black')
    p.circle('x1','y1', source=data, size = 12, fill_color='rgba(0, 128, 128, 1)', fill_alpha=0.9, line_color='grey', line_alpha=0.1)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name"),("Age (ka)", "@y1")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]

def create_at(result):
    df1 = pandas.DataFrame(result)

    date1 = df1[0]
    date1 = date1.astype('float64')

    date2 = df1[1]
    date2 = date2.astype('float64')
    date2_1 = date2 / 12

    date3 = df1[2]
    date3 = date3.astype('float64')
    date3_1 = date3 / 365

    date = date1 + date2_1 + date3_1

    p= figure(width=475, height=500, title="Dates for samples entered into ICE-D")
    p.xaxis.axis_label = "Date Entered (decimal date)"
    p.yaxis.axis_label = "Sample Count"

    bins = numpy.arange(numpy.min(date),numpy.max(date) + (5/365), (5/365))
    hist, edges = numpy.histogram(date, bins=bins)

    #p.hist(date, bins=numpy.arange(numpy.min(date),numpy.max(date) + (5/365), (5/365)))
    p.quad(top=hist,bottom=0,left=edges[:-1], right=edges[1:], fill_color="navy", line_color="white", alpha=0.5)

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]

def geo_map(result):
    #The input arg will maybe be lat lon name tuple (x,y,z)
    df1=pandas.DataFrame(list(result))
    #y1= log(tan((df1[0] + 90) / 360 * pi())) * 111319.490778 / pi() * 180
    y1=df1[0]
    y1=y1.astype('float64')
    y1=numpy.log(numpy.tan((90 + y1) * numpy.pi/360.0)) * 6378137
    x1=df1[1]
    x1=x1.astype('float64')
    x1=x1 * (6378137 * numpy.pi/180)
    name=df1[2]

    data = {'lat': array(y1),
            'lon': array(x1),
            'name': array(name)}

    p = figure(width=400, height=300, x_range=(-19926188, 19926188), y_range=(-16967796, 16967796),
           x_axis_type="mercator", y_axis_type="mercator")
    p.circle(x='lon',y='lat', source=data, size = 8, fill_color='grey', fill_alpha=0.9, line_color='black', line_alpha=6)
    p.add_tile(xyz.OpenStreetMap.Mapnik)
    p.add_tools(HoverTool(tooltips=[("Sample name", "@name")]))

    plot_script, plot_div = components(p)

    return [plot_script, plot_div]
