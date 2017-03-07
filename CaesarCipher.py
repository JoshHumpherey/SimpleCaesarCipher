# Python Caesar Cipher Program
# Written by Josh Humphrey
# Based on project from: https://inventwithpython.com/chapter14.html

def Mode():
    print("Do you want to transmit or recieve a secret message?")
    print("Enter '1' for transmission or '0' for recieving")
    Mode = input()
    if Mode == 1:
        print("You have chosent to 'Transmit' a message")
        return Mode
    elif Mode == 0:
        print("You have chosent to 'Recieve' a message")
        return Mode
    else:
        print("Sorry! You did not choose a correct mode :(")
        exit()

def GetKey():
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

def Encoder():
    length = len(Message)
    i = 0
    for i in range(length):
        EncryptedMessage[i] = ord(Message[i]) + Key
        i += 1
    return EncryptedMessage

def Decoder():
    length = len(Message)
    i = 0
    for i in range(length):
        Message[i] = ord(Message[i]) - Key
        i += 1
    return DecryptedMessage

#automated test script for parameters
auto = open("test.txt","r")
automode = auto.read(1)
autokey = auto.read(2)
#automated test script for message
hellomessage = open("message.txt","r")
automessage = hellomessage.read(20)

# Main Function
Type = Mode(automode)
Key = GetKey(autokey)
Message = Message(automessage)
if Type == 1:
   Encoder(Message)
   print(Message)

else:
   Decoder(Message)
   print(Message)
