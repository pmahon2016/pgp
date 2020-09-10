import gnupg
import os

gpg = gnupg.GPG(gnupghome = '/home/alice/.gnupg')

path = '/home/alice/txtfiles'
ptfile = '/debug.encrypted'


with open(path+ptfile,'rb')as f:
    status = gpg.decrypt_file(f, passphrase = 'mypassphrase', output = path+ptfile + ".decrypted")

print(status.ok)
print(status.stderr)
