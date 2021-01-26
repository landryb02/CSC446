from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',8888)
ftp.login()
#ftp.cwd('directory_name') #replace with your directory
ftp.retrlines('LIST')

def uploadFile():
    filename = 'test.txt' #replace with your file in your home folder
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

def downloadFile():
    filename = 'test.txt' #replace with your file in the directory ('directory_name')
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 8888)
    ftp.quit()
    localfile.close()

uploadFile()
#downloadFile()