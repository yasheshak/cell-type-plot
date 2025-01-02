import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

import matplotlib.patheffects as patheffects

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--position', default='BME163_Input_Data_Week3.position.tsv', type=str, action='store', help='input position tsv file')
parser.add_argument('-c', '--celltype', default='BME163_Input_Data_Week3.celltype.tsv', type=str, action='store', help='input celltype tsv file')
parser.add_argument('-o', '--output', default='tSNE_plot.png', type=str, action='store', help='output png file')

args = parser.parse_args()

positionFile = args.position
celltypeFile = args.celltype
outFile = args.output

print(positionFile, celltypeFile, outFile)


figureWidth=8
figureHeight=4

plt.style.use('BME163.mplstyle')

plt.figure(figsize=(figureWidth,figureHeight))
panelWidth=2
panelHeight=2

panel1 = plt.axes([0.5/figureWidth,0.5/figureHeight,panelWidth/figureWidth,panelHeight/figureHeight])
           #[x values], [y values]
panel1.set_xticks(range(-30,31,10))
panel1.set_yticks(range(-40,31,10))

panel1.set_xlim(-30, 30)
panel1.set_ylim(-40, 30)

plt.xlabel('tSNE 2')
plt.ylabel('tSNE 1')

file = open('BME163_Input_Data_Week3.position.tsv', 'r')
x_values = []
y_values = []
barcode = []
for line in file:
    field = line.strip().split()
    barcode.append(field[0])
    x_values.append(float(field[1]))
    y_values.append(float(field[2]))
file.close()



# Open the celltype.tsv file and extract the cell types for each cell
file = open('BME163_Input_Data_Week3.celltype.tsv', 'r')
ctype = {}
for line in file:
    field = line.strip().split()
    ctype[field[2]] = field[1]
file.close()


iBlue=(88/255,85/255,120/255)
iGreen=(120/255,172/255,145/255)
iGrey = (7/10, 7/10, 7/10)


for i in range(len(x_values)):
    if ctype[barcode[i]] == 'monocyte':
        color = iGrey
    elif ctype[barcode[i]] == 'bCell':
        color = iBlue
    #else:
    elif ctype[barcode[i]] == 'tCell':
        color = iGreen

    panel1.plot(x_values[i], y_values[i],
                marker='o',
                markersize=4,
                color=color,
                linewidth=0,
                alpha=1,
                markeredgecolor='black',
                markeredgewidth=0.1
        )
#create empty dictionaries for x and y values according to each cell type (ct)   
x_ct = {}
y_ct = {}

#loop through the length of x values
for i in range(len(x_values)):
    name = ctype[barcode[i]] #name/label is the value of the cell type dictionary with barcode as the key
    
    #iterate again and make empty lists to store, append after
    if name not in x_ct:
        x_ct[name] = []
        y_ct[name] = []
    x_ct[name].append(x_values[i])
    y_ct[name].append(y_values[i])

#use np.median
for name in ["monocyte", "bCell", "tCell"]:
    x_median = np.median(x_ct[name])
    y_median = np.median(y_ct[name])

    text = panel1.text(x_median, y_median, name, 
                       color='black', 
                       ha='center', va='center')
    
    #found how to add border on text during TA session and using the internet
    text.set_path_effects([patheffects.Stroke(linewidth=1, 
                                              foreground='white'), 
                                              patheffects.Normal()])


plt.savefig(outFile,dpi=600)
