import os, random, struct
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):

    in_filename = os.path.dirname(__file__) + in_filename.name

    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = Random.get_random_bytes(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    #filesize = in_filename.size
    #in_filename = in_filename.url
    with open(in_filename, 'rb') as infile:
    #in_filename.open(mode='rb')
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

    # with open(out_filename,'rb') as decfile:
    #     origsize = struct.unpack('<Q', decfile.read(struct.calcsize('Q')))[0]
    #     iv = decfile.read(16)
    #     decryptor = AES.new(key, AES.MODE_CBC, iv)
    #
    #     with open(out_filename+".dec", 'wb') as outfile:
    #         while True:
    #             chunk = decfile.read(chunksize)
    #             if len(chunk) == 0:
    #                 break
    #             outfile.write(decryptor.decrypt(chunk))
    #
    #         outfile.truncate(origsize)

def getKey(password):
    hasher = SHA256.new(str.encode(password))
    # print (hasher.digest())
    return hasher.digest()


def decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    #
    # print (out_filename)
    # print (in_filename)

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
