from jsonExp import jsonExp

import getpass
import socket

jsonFunction = jsonExp

jsonFunction.jsonSave(socket.gethostname(), getpass.getuser(), socket.gethostbyname(socket.gethostname()))