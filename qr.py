import qrcode

input_URL = input("Enter Link: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=1,
)

qr.add_data(input_URL)
qr.make(fit=True)

image = qr.make_image()
image.save("qr.png")

print("Entered Link: "+input_URL)
