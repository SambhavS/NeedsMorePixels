from __future__ import print_function
from PIL import Image, ImageDraw
im=Image.open("cow.jpg")
print("Hello world")
print(im.format, im.size, im.mode)
side=80
qRatio=10
for sqX in range(int(im.size[0]/side)):
    for sqY in range(int(im.size[1]/side)):
        r=0
        g=0
        b=0
        for i in range(side):
            for j in range(side):
                x=im.getpixel(((sqX*side)+i,(sqY*side)+j))
                #find average color
                r+=x[0]
                g+=x[1]
                b+=x[2]
        rAv=int(r/(side**2))
        gAv=int(g/(side**2))
        bAv=int(b/(side**2))
        draw=ImageDraw.Draw(im)
        draw.rectangle([sqX*side,sqY*side,(sqX+1)*side,(sqY+1)*side],(rAv,gAv,bAv))
        #for i in range(side):
         #   for j in range(side):
         #       im.putpixel(((sqX*side)+i,(sqY*side)+j),(rAv,gAv,bAv))
im.show()

