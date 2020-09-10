import gnupg
import os
gpg = gnupg.GPG(gnupghome="/home/alice/.gnupg")

path = '/home/alice/pgp_encrypt'
ptfile = '/encrypt_test.txt'
print(path)
with open(path + ptfile) as f_ile:

    status = gpg.encrypt_file(f_ile,recipients=["bob@acme.org"], output='/home/alice/test')

print(status.ok)
print(status.stderr)
