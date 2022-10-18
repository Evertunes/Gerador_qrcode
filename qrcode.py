import pyqrcode
import png
from pyqrcode import QRCode

qr =  'www.github.com/Evertunes'

url = pyqrcode.create(qr)

url.png('myqr.png', scale = 6)