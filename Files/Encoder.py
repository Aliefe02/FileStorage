# Receives string as input and produces encoded string
# Input can be manually entered as argv, if none entered string in clipboard will be used
# Output is copied to clipboard

import sys,pyperclip

characters = list(' abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ1234567890_"é!\'^+%&/()=?-#${[]}\\*@€~,`;.:<>| abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ1234567890_"é!\'^+%&/()=?-#${[]}\\*@€~,`;.:<>|')
sys.argv

if len(sys.argv) > 1:
    input = " ".join(sys.argv[1:])
else:
    input = pyperclip.paste()

input = list(input)

n = 0
while n<10:
    j = 0
    for i in input:
        input[j] = characters[characters.index(i)+j]
        j+=1
    n += 1

output = ''.join(input)
print(output)
pyperclip.copy(output)

