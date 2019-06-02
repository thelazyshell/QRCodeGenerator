import pyqrcode
from pyqrcode import QRCode
import sys

url = 'Any URL or anything you want'

qr = pyqrcode.create(url)

qr.png("myqr.png")