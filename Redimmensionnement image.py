from PIL import Image  
for i in range (0,10):
    im = Image.open("Coupe_%03d.tif"%(i,))
    size=im.size
    Nuancegrey=40
    im1 = im.crop((4, 4, 996, 996))
    newsize = (992, 992)
    im1 = im1.resize(newsize)
    im1.save('C:/Users/quent/Desktop/stage-thermo-m1/Patin-Feutre-Rose-@10um/1000x1000/Redim/' + 'Coupe_%03d.png'%(i,))
    grey = Image.new('L',(992,992))
    for x in range (992):
        for y in range (992):
            r,g,b=im1.getpixel((x,y))
            if r < Nuancegrey:
                r=255
            else:
                r=0
            grey.putpixel((x,y),r)
    grey.save('C:/Users/quent/Desktop/stage-thermo-m1/Patin-Feutre-Rose-@10um/1000x1000/Black-White/' + 'Coupe_%03d.png'%(i,))
