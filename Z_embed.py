from PIL import Image
from Steganography import Steganography

final = Steganography.steganography()
new_img = Image.fromarray(final)
new_img.show()
