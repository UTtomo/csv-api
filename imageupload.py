import csv
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime

now = datetime.datetime.now()
Name = '真里'
City = '真里'

# 現在時刻を織り込んだファイル名を生成
fmt_name = "python-data/test_{0:%Y%m%d-%H%M%S}.csv".format(now)

# ここにAD変換したデータの添付
with open(fmt_name,'w') as f:
    for i in range(0,50):
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([i,Name,City])

f.close()

print(now.date())
print(fmt_name)


gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)


f = drive.CreateFile({'title': "/{0:%Y%m%d-%H%M%S}.csv".format(now), 'mimeType': 'text/comma-separated-values'})
f.SetContentFile('%s' % fmt_name)
print('uploading files... ...')
f.Upload()

print('completed uploading files')
