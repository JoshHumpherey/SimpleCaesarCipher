# Caesar Cipher Encoder and Decoder written by Josh Humphrey

def GetKey()
    print("Please enter a secret key! It must be an integer between 1 and 25")
    key = input()
    if key<0 or key>25:
        print("Sorry your key is invalid! Try again")


def Encoder()
    print("Please enter your message below!")
    message