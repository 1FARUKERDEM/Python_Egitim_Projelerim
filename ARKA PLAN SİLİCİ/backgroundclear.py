from PIL import Image # resim açıp göstermek için 
from rembg import remove # arka planı silmek için 

input_image = Image.open("indir.png")
output_image =remove(input_image)

output_image.save ("indir_edit.png")
output_image.show()