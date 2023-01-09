#import qrcode
#img = qrcode.make('Some data here')
#type(img)  # qrcode.image.pil.PilImage
#img.save("./images/some_file.png")
import io
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=2
    )

qr.add_data('i am a gd girl')
qr.make(fit=True)
img = qr.make_image(fill_color='blue',back_colour='white')
img.save('./imgs/by_color.png')
f=io.stringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())