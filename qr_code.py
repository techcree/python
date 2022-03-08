#QR Code Generator ssk
#import
import qrcode
value = input("Wie soll der Inhalt des QR Codes lauten?:\n")
imgname = input("Wie soll der QR Code Dateiname lauten?:\n")
#creating QR code and print
qr = qrcode.make(value)
print (value)
print (imgname)
#saving QR code as png file
qr.save((imgname)+'.png')
