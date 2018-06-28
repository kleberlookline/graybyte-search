
# Graybyte : FTP
# https://github.com/etybyarg

import ftplib

class gbftp():
    def __init__(self, ip, port=21):
        self.ftpaddr  = str(ip)
        self.ftpport  = int(port)

    def ftpconnect(self, login, password):
        self.ftplogin = str(login)
        self.ftppass  = str(password)
        try:
            self.ftpconn = ftplib.FTP(self.ftpaddr, self.ftplogin, self.ftppass)
            if self.ftpconn.connect(self.ftpaddr, self.ftpport):
                return 1
            else:
                return 0
        except:
            return 0
