# Veiled
Secure, file-less password manager
---
Veiled is a secure file-less password manager which computes unique passwords securely by processing your masterpassword with other information like the website name, your username for the website and the password length (default: 32) without internet or without saving your password anywhere which protects your password database from breach or theft.
## Usage:
```
$ git clone https://github.com/spignelon/veiled
$ python veiled.py
```
***
### How does it work?
It first append your username and password length (if any) to your website name and then creates [SHA512](https://en.wikipedia.org/wiki/SHA-2) hash of it, then it uses the SHA512 hash as a salt and derive a key using [scrypt](https://en.wikipedia.org/wiki/Scrypt) as a [KDF](https://en.wikipedia.org/wiki/Key_derivation_function). _Scrypt was designed to be computationally intensive, to make it costly to perform large-scale custom hardware attacks and make it resistant to attacks like brute-force._ The Scrypt derived key is then passed to [BLAKE2b](https://en.wikipedia.org/wiki/BLAKE_(hash_function)#BLAKE2) just to make things more sophisticated and make any attacks against Veiled infeasible. The BLAKE2b hash is then encoded to Ascii85/Base85 and then trimmed to a desired length, maximum password length is 128 and default is 32. <br>
***
**Tips:**
+ It is recommended to use passphrase as master password
+ Leaving website name empty will generate you a random 32 digit password
