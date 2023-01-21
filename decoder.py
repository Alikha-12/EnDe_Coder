User_Message = input("Type message ").lower()
def Decoder(Message):
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(len(Alphabet)):
        New_Alphabet = Alphabet[i:] + Alphabet[:i]
        New_Message = ""
        for i in range(len(Message)):
            index = Alphabet.find(Message[i])
            if index <0:
                New_Message += Message[i]
            else:
                New_Message += New_Alphabet[index]
        print(New_Message)
Decoder(User_Message)
