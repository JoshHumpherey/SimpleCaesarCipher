# Python Caesar Cipher Program
# Written by Josh Humphrey
# Based on project from: https://inventwithpython.com/chapter14.html

def Mode(Mode):
    print("Do you want to transmit or recieve a secret message?")
    print("Enter '1' for transmission or '0' for recieving")
    Mode = int(input())
    if Mode == 1:
        print("You have chosent to 'Transmit' a message")
        return Mode
    elif Mode == 0:
        print("You have chosent to 'Recieve' a message")
        return Mode
    else:
        print("Sorry! You did not choose a correct mode :(")
        exit()

def GetKey(Key):
    print("Please enter the value of your secret key!")
    print("Keep in mind it must be an integer between 0 and 25")
    Key = int(input())
    if (Key<0 or Key>25):
        print("Sorry, but you gave me an invalid key value!")
        print("Please try again :)")
        exit()
    else:
        return Key

def Message():
    print("Please enter your message")
    Message = input()
    return Message

def Encoder(Message):
    length = len(Message)
    EncryptedASCII = list(range(0,length))
    EncryptedMessage = EncryptedASCII
    i = 0
    for i in range(length):
        if Message[i] == ' ':
            EncryptedMessage[i]=Message[i]
        else:
            EncryptedASCII[i] = ord(Message[i]) + 5
            EncryptedMessage[i] = chr(EncryptedASCII[i])
            i += 1
    result = "".join(EncryptedMessage)
    return result

def Decoder():
    length = len(Message)
    i = 0
    for i in range(length):
        Message[i] = ord(Message[i]) - Key
        i += 1
    return DecryptedMessage


# Main Function
Type = Mode(Mode)
Key = GetKey(Key)
Message = Message(Message)
if Type == 1:
   Encoder(Message)
   print(Message)

else:
   Decoder(Message)
   print(Message)


    
