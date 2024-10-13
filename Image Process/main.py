from PIL import Image, ImageFilter, ImageOps

img = Image.new('RGB', (400, 400), (255, 0, 0))
img.show()

try:
    im = Image.open('Image Process/colours.png')
except FileNotFoundError:
    print("Error: 'colours.png' not found.")
else:
    print(f"Format: {im.format}")
    print(f"Size: {im.size}")
    print(f"Mode: {im.mode}")
    
    filterd = im.filter(ImageFilter.BLUR)
    filterd.save('blurred.png', 'PNG')

    print("Blurred image saved as 'blurred.png'.")
