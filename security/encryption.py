from Crypto.PublicKey import RSA
from Crypto import Random


"""
Be cautious, as this will invalidated the previously saved rows in db
"""


KEY_STORAGE_DIR = '../webapp/keys/'

def generate_new_pub_private_keys():
    KEY_LENGTH = 2048
    random_gen = Random.new().read

    keypair = RSA.generate(KEY_LENGTH, random_gen)

    f = open(KEY_STORAGE_DIR + 'private.key', 'wb')
    f.write(keypair.exportKey())
    f.close()

    f = open(KEY_STORAGE_DIR + 'public.pem', 'wb')
    f.write(keypair.publickey().exportKey())
    f.close()



if __name__ == "__main__":
    generate_new_pub_private_keys()