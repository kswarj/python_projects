#enter the user input for website to be opened with qrcode
#enter the file to save the QRcode 
#generate the QRcode with qrcode generator library
#store the image in file entered by the user


import qrcode

#Enter the website or file input
user_input = input("Enter the website").strip()

#Input  file to save the qrcode 
file_to_save = input("Enter the file name").strip()

# create a QR code object
qr = qrcode.QRCode(box_size=10,border=4)
qr.add_data(user_input)
qr.make(fit=True)

#create a image with the QRcode 
img = qr.make_image(fill_color = 'black' ,back_color = 'white')

#save the qrcode in to file input provided by the user
img.save(file_to_save)