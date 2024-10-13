from PIL import Image, ImageDraw, ImageFont

img = Image.open('Write Text on Image/dark.png')

draw = ImageDraw.Draw(img)

fnt = ImageFont.truetype("comicbd.ttf", 80)
text = "Hello Team!!!"
bbox = draw.textbbox((0, 0), text, font=fnt)  
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

image_width, image_height = img.size
x = (image_width - text_width) // 2
y = (image_height - text_height) // 2

draw.text((x, y), text, font=fnt, fill=(255, 255, 255))

img.save("textImage.png")

