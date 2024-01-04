import qrcode
img = qrcode.make("https://gokulrportfolio.netlify.app/")
img.save("qr.jpg")
