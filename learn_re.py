#Regular Expression
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'
##pattern=re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d[89]')
##matches=pattern.finditer(text_to_search)

##for match in matches:
##    print(match)
##print(text_to_search[1:4])

sentence = 'Start a sentence and then bring it to an end Start'
pattern=re.compile(r'sentence')
matches=pattern.search(sentence)
print(matches)

sentence = 'Start a sentence and then bring it to an end Start'
pattern=re.compile(r'start',re.IGNORECASE)
matches=pattern.match(sentence)
print(matches)


##for match in matches:
##    print(match)


##with open('data.txt','r') as f:
##    content=f.read()
##    matches=pattern.finditer(content)
##    for match in matches:
##        print(match)

##pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
##matches=pattern.finditer(text_to_search)
##
##for match in matches:
##    print(match)
##
##pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
##matches=pattern.finditer(text_to_search)
##
##for match in matches:
##    print(match)

##pattern=re.compile(r'(M|r|rs|s)\.?\s[A-Z]\w*')
##matches=pattern.finditer(text_to_search)
##
##for match in matches:
##    print(match)
                   

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.[a-zA-Z]+')
pattern1 = re.compile(r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.(com|edu|net)')

matches = pattern1.finditer(emails)

for match in matches:
    print(match)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

##pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
##
##subbed_urls = pattern.sub(r'\2\3', urls)
##
##print(subbed_urls)
##
##matches = pattern.finditer(urls)
##
##for match in matches:
##    print(match.group(3))


"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"""
