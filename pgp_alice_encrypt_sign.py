import gnupg
import os
gpg=gnupg.GPG(gnupghome='/home/alice/.gnupg')

gpg.encoding = 'utf-8'


path='/home/alice/txtfiles'
ptext = '/plaintext_alice.txt'

stream =  open(path+ptext, 'rb')

fp = gpg.list_keys(True).fingerprints[0]

edata = gpg.encrypt_file(stream, recipients='bob@acme.org',sign=fp,passphrase='mypassphrase',output=path+ptext+'.pgp')
