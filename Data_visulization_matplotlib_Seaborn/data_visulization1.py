# Data visualization with python, matplotlib and seaborn
# Data visualization is the graphic representation of data. it involves producing images that communicate relationship among the rpresented data to viewers.
import matplotlib.pyplot as plt
import seaborn as srn

'''Line Chart: One of the simples an most widely used data visualization technique. a line chart displays 
information as a series of data points or markers connected by straight line.Draw a line chart we can use 
the plt.plot()'''
yield_apple=[0.895,0.91,0.919,0.926,0.929,0.931]
print(plt.plot(yield_apple))
# Plotting multiple line
year=range(2000,2012)
# Customizing the X-axis
year=[2010,2011,2012,2013,2014,2015]
yield_apple=[0.895,0.91,0.919,0.926,0.929,0.931]
plt.plot(year,yield_apple)
# Plotting multiple line
year=range(2000,2012)
yield_apple=[0.895,0.91,0.919,0.926,0.929,0.931,0.934,0.936,0.937,0.943,0.940],0.951
yield_orange=[0.962,0.941,0.930,0.923,0.918,0.908,0.907,0.904,0.901,0.905,0.899,0.879]
print(plt.plot(year,yield_apple))
print(plt.plot(year,yield_orange))
print(plt.xlabel('Year'))
print(plt.ylabel('Yield (tons per hectare)'))
# Chart title and legend
plt.plot(year,yield_apple)
plt.plot(year,yield_orange)
plt.xlabel("Year")
plt.ylabel("Yield(tons per year)")
plt.title("Crop Yield")
plt.legend(['Apple','Orange'])
# Line Markers
plt.plot(year,yield_apple,marker='o')
plt.plot(year,yield_orange,marker='x')
plt.title("Crop Yield")
plt.xlabel("Year")
plt.ylabel("Yield(tons per hectare)")
# Styling line and markers
'''The plt.plot function supports many arguments for styling lines and markers
1. color or c: set the color of the line 
2. linestyle or ls: choose between a solid or dashed line
3. linewidth or lw: set the width of line
4. markersize or ms: set the size of marker
5. markeredgcolor or msc: set the color of marker
6. markeredgwidth or msw: set the width of markers
7. markerfacecolor or mfc: set the fill color for marker
8. alpha: opacity of the plot'''
plt.plot(year,yield_apple,marker='s', c='g', ls='-', lw=2, ms=6, mew=2, mec='red',alpha=.8)
plt.plot(year,yield_orange,marker='x', c='r', ls='--', lw=2, ms=6, mew=2, mec='green',alpha=1)
plt.title("Crop Yield")
plt.xlabel('Year')
plt.ylabel("Yield(tons per hectear)")
plt.legend(['Apple','Orange'])
# the fmt argument provides a shorthand for specify theline style, marker and color.it can be provided third argument to plt.plot
# fmt='[marker][line][color]'
plt.plot(year,yield_apple,'o-b')
plt.plot(year,yield_orange,'s--g')
plt.title("Crop Yield")
plt.xlabel('Year')
plt.ylabel("Yield(tons per hectear)")
plt.legend(['Apple','Orange'])
# If no line style is specified in fmt only marker drown.
plt.plot(year,yield_orange,'ob')
plt.title("Yield of orange(tons per hectear")
# Changing the figure size- we can use plt.figure function to change the size of figure
plt.figure(figsize=(10,5))
plt.plot(year,yield_apple,'o-b')
plt.plot(year,yield_orange,'s--g')
plt.title("Crop Yield")
plt.xlabel('Year')
plt.ylabel("Yield(tons per hectear)")
plt.legend(['Apple','Orange'])
# Improving Default style using seaborn
'''An easy way to make your charts look beautyful is to use some default styles provided in the seaborn library
these can be applied globally using srn.set_style'''
import seaborn as srn
srn.set_style('whitegrid')
plt.figure(figsize=(10,5))
plt.plot(year,yield_apple,'o-b')
plt.plot(year,yield_orange,'s--g')
plt.title("Crop Yield")
plt.xlabel('Year')
plt.ylabel("Yield(tons per hectear)")
plt.legend(['Apple','Orange'])
srn.set_style('darkgrid')
plt.figure(figsize=(10,5))
plt.plot(year,yield_apple,'o-b')
plt.plot(year,yield_orange,'s--g')
plt.title("Crop Yield")
plt.xlabel('Year')
plt.ylabel("Yield(tons per hectear)")
plt.legend(['Apple','Orange'])
plt.plot(year,yield_apple,'og')
plt.title("Yield of Apple(tons per hectear")
