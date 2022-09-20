from PIL import Image

img = Image.open("UnoDeck2.png")

i = 0
for y in range(6):
    j = 2
    k = 3
    for x in range(12):
        if i == 64:
            break
        left = 0
        top = 0
        height = 256
        width = 166
        box = (width+j)*x, (height+k)*y, width*(x+1)+(j*x), height*(y+1)+(k*y)
        area = img.crop(box)
        cardName = "Card" + str(i)+ ".png"
        area.save((cardName),"PNG")
        i += 1
        

