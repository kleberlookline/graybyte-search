
# Graybyte : SSL
# https://github.com/etybyarg

import socket
import ssl
import cryptography.x509
import cryptography.hazmat.backends.openssl

class gbssl():
    def __init__(self, ip, port=443):
        self.ssladdr  = str(ip)
        self.sslport = int(port)

    def sslsocketo(self, timeout=5): # Socket
        self.timeoutsock = timeout
        self.gsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gsock.settimeout(self.timeoutsock)
        self.ssl_gsock = self.gcontext.wrap_socket(self.gsock, do_handshake_on_connect=True)
        self.ssl_gsock.connect((self.ssladdr, self.sslport))

    def sslv3(self): # SSLv3 POODLE
        try:
            self.gcontext = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
            self.sslsocketo()
            self.ssl_gsock.close()
            return 1
        except:
            return 0

    def sslhashpref(self, shaone=0): # Pref for detect signature
        self.shaone = int(shaone)
        self.sslsocketo()
        self.cert = cryptography.x509.load_der_x509_certificate(self.ssl_gsock.getpeercert(True), cryptography.hazmat.backends.openssl.backend)
        self.ssl_gsock.close()
        if self.shaone is 1:
            if self.cert.signature_hash_algorithm.name is 'sha1':
                return 1
            else:
                return 0
        else:
            return self.cert.signature_hash_algorithm.name

    def sslhash(self, shaoneprint=0): # Pref for detect signature
        self.shaoneprint = int(shaoneprint)
        try:
            self.gcontext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            return self.sslhashpref(self.shaoneprint)
        except:
            try:
                self.gcontext = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
                return self.sslhashpref(self.shaoneprint)
            except:
                return 0

    def sslsha1(self): # SHA-1
        return self.sslhash(1)

    def sslsignhash(self): # Signature hash
        return self.sslhash(0)
