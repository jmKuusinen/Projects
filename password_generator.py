import sys
import hashlib
import binascii
import os


def hash_password(password):
    
    # Luodaan suola
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    # Lasketaan salasanan hash sisältäen suolan, 100 000 iteraatiota tietoturvan vuoksi
    pwdhash = hashlib.pbkdf2_hmac(
        'sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    # Suola säilötään erikseen ja sitä käytetään aina kun tarkistetaan käyttäjän syöttämää salasanaa
    
    return (salt + pwdhash).decode('ascii')


def main():
    if len(sys.argv) != 2:
        print("Invalid arguments!")
        sys.exit(2)

    password = sys.argv[1]
    print(hash_password(password))

    # Palataan main - funktioon
if __name__ == '__main__':
    main()
