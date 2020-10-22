import hashlib
import binascii
import sys



# Tässä dictionaryssa säilytetään käyttäjätiedot salattuna

users = {
    "Admin": "fd63b1666e856c6c5d057b09499808f375a6e39639394115d180e8becb6e7edf8460eb749381f77acfa070dac0f9dee26667fdd509998dbcff456ce3062474df212d52065c9a4edc94ebdd11edd8f15664abfbf0efde069470cbf630e397ee7e",
    "sovellus": "5cac46632d505040a1d14afb414bdc243925aaa4621173690dbad3f921e4ad1ab173d5c22eddf0f52b024d6a6f4adb770622c3916c69496937e54296cb99adfcaddf92e8f2aa618ba34c44aebab77a31ef01b3ddb3fdc46059f97314b76468db"
}


def verify_password(user, provided_password):
    
    global users
    # Tarkistetaan salasana
    if user not in users:
        return False

    stored_password = users[user]
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def main():
    if len(sys.argv) != 3:
        print("Invalid arguments!")
        sys.exit(3)

    user = sys.argv[1]
    password = sys.argv[2]
    isValid = verify_password(user, password)
    if isValid:
        print("Oikea salasana")
    else:
        print("Väärä käyttäjätunnus ja/tai salasana!")


if __name__ == '__main__':
    main()
