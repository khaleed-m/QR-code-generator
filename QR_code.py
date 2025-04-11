#just making simple qr code 
import qrcode as qr
img =qr.make("www.linkedin.com/in/m-mahammad-khaleed-6a8a30313")
img.save("Linkedin_profile.png")