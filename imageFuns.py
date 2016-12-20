from __future__ import print_function
from PIL import Image, ImageDraw
import sys

im=Image.open(sys.argv[1])
# print("Hello world")

print(im.format, im.size, im.mode)
side=int(sys.argv[3]) #how big pixels are
qRatio=.1*side #how many it skips; bigger the number faster the results but inaccurate

#core
for sqX in range(int(im.size[0]/side)):
    for sqY in range(int(im.size[1]/side)):
        r=0
        g=0
        b=0
        for i in range(int(side/qRatio)):
            for j in range(int(side/qRatio)):
                x=im.getpixel(((sqX*side)+qRatio*i,(sqY*side)+qRatio*j))
                #find average color
                r+=x[0]
                g+=x[1]
                b+=x[2]
        rAv=int(r/((side/qRatio)**2))
        gAv=int(g/((side/qRatio)**2))
        bAv=int(b/((side/qRatio)**2))
        draw=ImageDraw.Draw(im)
        draw.rectangle([sqX*side,sqY*side,(sqX+1)*side,(sqY+1)*side],(rAv,gAv,bAv))
        
im.save(sys.argv[2])

