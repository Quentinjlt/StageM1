import numpy as np
from PIL import Image
import time
startTime=time.time()
def img_3D(h,k,l):
    axe_h_min=h
    axe_h_max=h+8
    axe_k_min=k
    axe_k_max=k+8
    axe_l_min=l
    axe_l_max=l+8
    axe_z=8
    axe_x=8
    axe_y=8
    tableau_pixel=np.zeros((axe_z,axe_x,axe_y),int)
    a=0
    for z in range (axe_h_min,axe_h_max):
        with Image.open("C:\\Users\\quent\\Desktop\\stage-thermo-m1\\Patin-Feutre-Rose-@10um\\1000x1000\Binaire\\Coupe_%03d.png"%(z), 'r') as image:
            b=0
            for x in range (axe_k_min,axe_k_max):
                c=0
                for y in range (axe_l_min,axe_l_max):
                    coord=x,y
                    tableau_pixel[a][b][c]=image.getpixel(coord)
                    c=c+1
                b=b+1
        a=a+1
        image.close()
    sumpix=np.sum(tableau_pixel)/255
    return sumpix,x,y,z
for m in range (0,992,8):
    nuance_grey=Image.new('RGB',(124,124))
    for v in range (0,992,8):
        for n in range (0,992,8):
            pixel=int(img_3D(m, v, n)[0])
            v1=int(v/8)
            n1=int(n/8)
            if pixel >= 510:
                rouge=255
                vert=255
                bleu=pixel-510
            if 510>pixel>=256:
                rouge=255
                bleu=0
                vert=pixel-255
            if pixel<256:
                vert=0
                bleu=0
                rouge=pixel
            nuance_grey.putpixel((v1,n1),(rouge,vert,bleu))
    m1=int(m/8)
    nuance_grey.save('C:/Users/quent/Desktop/stage-thermo-m1/b-from-2d-png-to-mentat/image-512-rose-couleur/' + 'Coupe_%03d_x512.png'%(m1))
    nuance_grey.close()
executionTime=(time.time()-startTime)
print('Execution time in seconds: '+str(executionTime))
