from PIL import Image,ImageDraw
import numpy as np

def im_editor():

    basewidth = 64
    img = Image.open('pic.jpg')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS).convert("RGB")
    # img.save('new.jpg')

    # Open the input image as numpy array, convert to RGB
    # img=Image.open("new.jpg")
    npImage=np.array(img)
    h,w=img.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)

    # Convert alpha Image to numpy array
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save('result.png')

    for i in [1, 2]:
        img = Image.open('result.png')
        background = Image.open(f't{i}.jpg')

        offset = (95,50)
        background.paste(img, offset)
        background.save(f'out{i}.png')

im_editor()