import qrcode
from PIL import Image

data = " QR_KOD_ÇALIŞIYOR :)"

qr =qrcode.QRCode(
   version=2, 
   box_size=10,
   border=4,
 )

qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill_color="red", back_color="darkblue")

img.save("QR_KOD_ÇALIŞIYOR.png")
img.show()