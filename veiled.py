import sys
import getpass
import secrets
import hashlib
from hashlib import blake2b
import base64
web = input("Enter the website name: ")
if not bool(web):
	print("Your Random Password is: ", secrets.token_urlsafe(24))
	sys.exit(0)
uname = input("Enter username: ")
key = bytes(getpass.getpass("Enter your master key: "), "UTF-8")
le = input("Set the length of the password: ")
if not (bool(uname) and bool(key)):
	print("Username and/or key cannot be empty!!")
	sys.exit(1)
sha = bytes(hashlib.sha512(bytes(web+le+"1684bb40c132de2167a62a8b"+uname, "UTF-8")).hexdigest(), "UTF-8")
rawpas = bytes(hashlib.scrypt(key, salt=sha, n=2**14, r=8, p=1).hex(), "UTF-8")
rawpas = blake2b(rawpas).hexdigest()
pas1 = str(base64.b85encode(bytes(rawpas, 'UTF-8')))
if not (le.isdigit() or le==''):
	print("Please Enter a correct numerical password length or leave it empty.")
	sys.exit(1)
elif not bool(le):
	le="32"
elif int(le) > 128:
	le="128"
elif int(le) < 8:
	le="8"
for i in range(5, int(le)+5):
	print(pas1[i], end="")
print("")
del i, web, uname, key, le, sha, rawpas, pas1
