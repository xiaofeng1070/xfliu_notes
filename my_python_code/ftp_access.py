#!/usr/local/bin/python3

import ftplib
from ftplib import FTP

ftp = FTP('sj-xfliu')
ftp.login('xfliu','Youneed3m')
ftp.cwd('/vols/rspace01/space/users/rock_cad/mce_releases')
#ftp.retrlines('LIST')
#ftp.retrlines('NLST')
aaa=ftp.nlst()
#print (aaa)
print (aaa[-1])
#output = aaa.split(",")[-1]
#print (output)
ftp.quit()

