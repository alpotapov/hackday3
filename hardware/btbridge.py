import serial
import urllib2

ser = serial.Serial('/dev/cu.CaseBT01-DevB', 9600)
#ser.write('5')
while True:
	line = ser.readline()
	print line
	if "Coin" in line:
		print "!!!!!!!"
		try:
			print urllib2.urlopen("http://payment-backend.herokuapp.com/hook/payment_received").read()
		except:
			pass