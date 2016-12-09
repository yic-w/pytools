#!/usr/bin/python
from  ftplib import FTP
import sys
import os

if len(sys.argv) <= 1:
	print ''' usage \
		prog <file> <ap|pc> ip4'''
	sys.exit()

HOST = '192.168.100.84'
USER = 'ftp'
PASS = 'ftp'

if sys.argv[2] == 'ap':
	DESTCMD = 'scp %s root@172.16.25.%s:/tmp' %  (sys.argv[1],sys.argv[3])
elif sys.argv[2] == 'pc':
	DESTCMD = 'sz %s' % sys.argv[1]
	
ftp = FTP(HOST,USER,PASS)

print ftp.getwelcome()

ftp.cwd("yicheng.wang")

for name in ftp.nlst():
	if name == sys.argv[1]:
		ftp.retrbinary('RETR %s' % name,open('%s'% name,'wb').write)
		os.system(DESTCMD)
		os.remove(name)
		print name,'send OK'
		break

ftp.quit()
