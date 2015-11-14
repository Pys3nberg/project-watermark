from Crypto.Cipher import AES
import base64
#import os

def encryption(privateInfo):
    # 16bytes for 128bit encryption
    BLOCK_SIZE = 16
    # is used to ensure that the encrypted data meets the block size
    PADDING = '{' 
    # so this takes the string and adds padding so that its length is divisible
    # by block size
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING 
    # This anonymous function takes in a cipher that we will initialize and then
    # encrypts the padded string. Then we use base64encoding so that we turn the
    # binary data into common characters
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))#
    # this generates a randome key of BLOCK_SIZE long, os.urandom is the most
    # accepted form
    #secret = os.urandom(BLOCK_SIZE) 
    secret = b'W\xdc\x99<\x0f\xc0\x9c\xe5=m\xe7b\x1a\x05\xdeQ'
    print('encryption key: ', secret)
    # Create the AES cipher and bass the secret key
    cipher = AES.new(secret)
    # finnaly encrypt and encode our message
    encoded = EncodeAES(cipher, privateInfo)
    print('Encrypted string:', encoded)

                        
def decryption(encryptedString):

    PADDING = '{'
    decodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode('UTF-8').rstrip('{')
    secret = b'W\xdc\x99<\x0f\xc0\x9c\xe5=m\xe7b\x1a\x05\xdeQ'
    cipher = AES.new(secret)
    decoded =  decodeAES(cipher, encryptedString)
    print(decoded)
