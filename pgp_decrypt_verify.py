import gnupg
import os
gpg=gnupg.GPG(gnupghome='/home/bob/.gnupg')

gpg.encoding = 'utf-8'


path='/home/bob/txtfiles'
ptext = '/plaintext_alice.txt.pgp'

stream =  open(path+ptext, 'rb')
decrypted_data = gpg.decrypt_file(stream,passphrase = 'mypassphrase',output=path + ptext + '.verified')

print(decrypted_data.status)
print(decrypted_data.valid)
print(decrypted_data.trust_text)

