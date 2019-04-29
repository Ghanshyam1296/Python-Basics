message='Hello World'
print(message)
#Esacpe Character
message='Ghanshyam\'s Home'
print(message)
#Multiple line comment
message="""Ghanshyam Rathore is from Rajasthan"""
print(message)
print(len(message))
#Slicing
print(message[0])
print(message[10:])
print(message[:10])
print(message[10:35])
#lower case conversion
print(message.lower())
#Uppercase Conversion
print(message.upper())
#Counting the desired word in string
print(message.count('a'))
#Finding word in a string
print(message.find('Naresh'))
print(message.find('Ghanshyam'))

#Replace function
message='Hello World'
new_message=message.replace('World','Universe')
print(new_message)
print(message)

#Concatinating String
greeting='Hello'
Name='Ghanshyam'
message=greeting+','+Name+'.Welcome!'
print(message)

message='{},{}.Welcome!'.format(greeting,Name)
print(message)

