Message = input("Type your message ").lower()
Key = int(input("Type key"))
Alphabet = "abcdefghijklmnopqrstuvwxyz"
New_Alphabet = ""
New_Message = ""
if Key == 0:
    New_Alphabet = Alphabet
elif Key > 0:
    New_Alphabet = Alphabet[Key:] + Alphabet[:Key]

else:
    New_Alphabet = Alphabet[(26 + Key):] + Alphabet[:(26 + Key)]
for i in range(len(Message)):
    index = Alphabet.find(Message[i])
    if index <0:
        New_Message += Message[i]
    else:
        New_Message += New_Alphabet[index]
print(New_Message)