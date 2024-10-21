from PIL import Image, ImageDraw, ImageFont

image = Image.open("Write Text on Image/dark.png")  
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 48)  
watermark_text = "Watermarked by Pillow"
text_color = (255, 255, 255, 128) 

text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)[2:]
x = image.width - text_width - 10  
y = image.height - text_height - 10  

draw.text((x, y), watermark_text, font=font, fill=text_color)

image.save("watermarked_image.png")

