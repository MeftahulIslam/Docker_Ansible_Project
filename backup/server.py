from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


FTP_PORT = 21
FTP_USER = "ftp"
FTP_PASSWORD = "ftp"
FTP_DIRECTORY = "/opt"


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "Server Ready"
    address = ('0.0.0.0', FTP_PORT)
    server = FTPServer(address, handler)
    server.serve_forever()


if __name__ == '__main__':
    main()