import os, random, struct
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):

    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = Random.get_random_bytes(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    foo=str.encode(' ' * (16 - len(chunk) % 16))
                    chunk +=foo

                outfile.write(encryptor.encrypt(chunk))

def getKey(password):
    hasher = SHA256.new(str.encode(password))
    return hasher.digest()


def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)


if __name__ == '__main__':
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ")

    if choice == 'E' or choice == 'e':
        filename = input("File to encrypt: ")
        savename = input("Encrypt Name: ")
        password = input("Password: ")

        encrypt_file(getKey(password), filename, savename)
        print("Encoding Complete.")

    elif choice == 'D' or choice == 'd':
        filename = input("File to decrypt: ")
        savename = input("Encrypt Name: ")
        password = input("Password: ")
        decrypt_file(getKey(password), filename, savename)
        print("Decoding Complete.")
    else:
        print("No Option selected, closing...")
