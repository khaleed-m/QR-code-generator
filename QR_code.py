#just making simple qr code 
# import qrcode as qr
# img =qr.make("www.linkedin.com/in/m-mahammad-khaleed-6a8a30313")
# img.save("Linkedin_profile.png")

import qrcode 
 
data =input("Enter the Text or URL: ").strip()
filename=input("Enter the filename:").strip()

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=20,border=10)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save(filename)
print(f'QR code saved as {filename}')
