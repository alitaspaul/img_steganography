from PIL import Image
from Steganography import Steganography

final = Steganography.reverse()
new_img = Image.fromarray(final)
new_img.show()