from time import sleep
import pyotp
import datetime

hotp = pyotp.HOTP('ZEC2DOHQT4DYMVY6KYI5FLBAMGLDC6LN')

print(hotp.at(1))

print(hotp.at(1))