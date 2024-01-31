import qrcode as qr
img = qr.make("https://github.com/")
img.save("qrcode2.png")