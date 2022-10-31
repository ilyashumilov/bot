from PIL import Image,ImageDraw, ImageFont
import numpy as np

def im_editor(user):
    basewidth = 64
    img = Image.open('img/pic.jpg')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS).convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).save('img/result.png')
    for i in [1, 2]:
        img = Image.open('img/result.png')
        background = Image.open(f'img/t{i}.jpg')
        offset = (95,50)
        background.paste(img, offset)
        background.save(f'img/out{i}.png')
        img = Image.open(f"img/out{i}.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 23)
        draw.text((173, 56), str(user), (0, 0, 0), font=font, stroke_width=1)
        draw.ellipse((79, 33, 172, 127), fill=None, outline='white', width=17)
        img.save(f'img/out{i}.png')

im_editor('var')