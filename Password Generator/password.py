import random
import string
from PIL import Image, ImageDraw, ImageFont

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_characters = lowercase + uppercase + digits + special_chars

    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def save_password_image(password):
    img = Image.new('RGB', (300, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    text_position = (10, 30)  
    draw.text(text_position, f"Generated Password: {password}", fill=(0, 0, 0), font=font)

    img.save("generated_password.png")
    print("Password saved as an image")

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)

    print(f"Generated Password: {password}")
    save_to_image = input("Do you want to save the password as an image? (yes/no): ").strip().lower()
    if save_to_image == 'yes':
        save_password_image(password)
