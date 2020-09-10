import gnupg
gpg = gnupg.GPG(gnupghome="/home/bob/.gnupg")
gpg.encoding = 'utf-8'

input_data = gpg.gen_key_input(
    name_email='bob@acme.org',
    passphrase='mypassphrase',
    key_type = "RSA",
    Key_length = 1024)


    
key = gpg.gen_key(input_data)


print(key)

public_key = gpg.export_keys(str(key))

with open('bob_pub_key.asc','w') as f:
    f.write(public_key)

