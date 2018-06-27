from PIL import Image, ImageDraw, ImageFont
import random

im = Image.open("avatar.png").convert('RGBA')

# get a drawing context
rannum = str(random.randrange(1, 98))
# set font
fnt = ImageFont.truetype('arialbd.ttf', 40)
# generate a new blank image
txt = Image.new('RGBA', im.size, (255, 255, 255, 0))

d = ImageDraw.Draw(txt)

d.text((85, 0), rannum, font=fnt,  fill=(255, 0, 0, 255))

out = Image.alpha_composite(im, txt)
out.save('newavatar.png')
out.show()