#! python3
#phoneAndEmail.py - finds phone numbers and email addresses on the clipboard

import pyperclip, re



phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username  + oznacza że jest ich iles pod rząd wymienoonych literek
    @                   #@symbol - brak plusa - jest jedne 
    [a-zA-Z0-9.-]+      #domain name 
    (\.[a-zA-Z]{2,4})   #dot-something
    )''', re.VERBOSE)

#re.VERBOSE
#This flag allows you to write regular expressions that look nicer and are more readable 
#by allowing you to visually separate logical sections of the pattern and add comments. 
#Whitespace within the pattern is ignored, except when in a character class, 
#or when preceded by an unescaped backslash, or within tokens like *?, (?: or (?P<...>. 



# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []        #pusta na początku lista
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum +=' x'+groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy result to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")
