import pyqrcode
import png
from pyqrcode import QRCode

s = "https://www.linkedin.com/in/justin-kato-852838205/"

url = pyqrcode.create(s)
  
url.png("myqr.png", scale = 6)