import qrcode

print("-----------------------QR Code Generator--------------------")
name = input('Name: ')
phone = input('Phone: ')
contact = f'Name : {name} \nPhone : {phone}'
img = qrcode.make(contact)


qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=3
)

img.save(f'{name}.png')
