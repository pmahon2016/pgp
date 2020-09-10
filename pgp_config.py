import gnupg
import os
gpg=gnupg.GPG(gnupghome='/home/bob/.gnupg')

gpg.encoding = 'utf-8'


path='/home/alice/txtfiles'
ptext = '/testverify'

stream =  open(path+ptext, 'rb')
decrypted_data = gpg.decrypt_file(stream,passphrase = 'mypassphrase')

