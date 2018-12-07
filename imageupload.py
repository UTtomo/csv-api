import csv
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime
import wiringpi as pi
import time
import mcp_adc


print('Data collecting program start')
SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3
adc = mcp_adc.mcp3208( SPI_CE, SPI_SPEED, VREF )
now = datetime.datetime.now()
City = 'citycity'


fmt_name = "python-data/test_{0:%Y%m%d-%H%M%S}.csv".format(now)
print('start collecting data...')

with open(fmt_name,'w') as f:
    for i in range(0,50):
        now = datetime.datetime.now()
        value = adc.get_value( READ_CH )
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([now,value,City])
        time.sleep( 0.1 )
f.close()


print( 'New file has created. Its name is ')
print(fmt_name)
print('    ')

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)


f = drive.CreateFile({'title': "/{0:%Y%m%d-%H%M%S}.csv".format(now), 'mimeType': 'text/comma-separated-values'})
f.SetContentFile('%s' % fmt_name)
print('uploading files to Google Drive... ...')
f.Upload()

print('Completed uploading files')
print()
