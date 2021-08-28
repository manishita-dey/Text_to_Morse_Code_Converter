morse_chart = {
'A': '•-',
'B': '-•••',
'C': '-•-•',
'D': '-••',
'E': '•',
'F': '••-•',
'G': '--•',
'H': '••••',
'I': '••',
'J': '•---',
'K': '-•-',
'L': '•-••',
'M': '--',
'N': '-•',
'O': '---',
'P': '•--•',
'Q': '--•-',
'R': '•-•',
'S': '•••',
'T': '-',
'U': '••-',
'V': '•••-',
'W': '•--',
'X': '-••-',
'Y': '-•--',
'Z': '--••',
'0': '-----',
'1': '•----',
'2': '••---',
'3': '•••--',
'4': '••••-',
'5': '•••••',
'6': '-••••',
'7': '--•••',
'8': '---••',
'9': '----•',
'•': '•-•-•-',
',': '--••--',
'?': '••--••',
' ': ' ',
}

user_input = input('Type something you want to convert into morse code:').upper()

char_list = list(user_input)

morse_code = [morse_chart[char] for char in char_list]

morse_string = ''

for code in morse_code:
    morse_string+=code
    morse_string+= ' '

print(f' Morse code for your provided string is: {morse_string}')



