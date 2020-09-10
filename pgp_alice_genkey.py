import gnupg
import os
gpg=gnupg.GPG(gnupghome='/home/alice/.gnupg')

gpg.encoding = 'utf-8'


input_data = gpg.gen_key_input(
        name_email = 'alice@acme.org',
        passphrase = 'mypassphrase',
        key_type = 'RSA',
        key_length = 1024)


key = gpg.gen_key(input_data)

print(key)


