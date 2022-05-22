from __future__ import division
from PIL import Image
import numpy as np
import statistics
def repartition(filename):
    image_file = Image.open(filename)
    tab = np.array(image_file.getdata())
    nt = tab.size
    n1 = np.count_nonzero(tab==255)
    n0 = np.count_nonzero(tab==0)
    return n1/nt, n0/nt
Nylon=list()
Air=list()    
for i in range (0,7):     
    noir, blanc = repartition("Coupe_%03d.png"%(i,))
    Nylon.append(noir)
    Air.append(blanc)
MeanNyl=statistics.mean(Nylon)
MeanAir=statistics.mean(Air)
print ("Nylon : {0:5.2f}% et Air : {1:5.2f}%".format( 100*MeanNyl, 100*MeanAir))