import qrcode

# URL que irá en el código QR
url = "https://joseorteha.github.io/MyPortafolio/"

# Crear el QR con tamaño y borde específicos
qr = qrcode.QRCode(version=1, box_size=25, border=5)

# Añadir la URL al código QR
qr.add_data(url)

# Ajustar el tamaño del QR
qr.make(fit=True)

# Crear y guardar la imagen del QR
imagen = qr.make_image()
imagen.save("My_Qr.png")   
