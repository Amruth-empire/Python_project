import qrcode as qr 
upi_id=input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount%cu=CURRENCY&tn=MESSAGE  &am=100

scanner_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cu=INR&tn=Thank%20you'

scanner=qr.make(scanner_url)
# scanner.save("Google_pay_scanner.png")
scanner.show()