import gnupg
import os

gpg = gnupg.GPG(gnupghome = '/home/alice/.gnupg')

path = '/home/alice/txtfiles'

for f in os.listdir(path):
    with open(path+"/"+ f, 'rb')as efile:
        status = gpg.encrypt_file(efile,recipients= 'alice@acme.org',output = path+"/"+f)


print(status.stderr)
