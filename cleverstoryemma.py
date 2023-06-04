print('Hello reader!, This is your clever story generator')
print()
adjective = input('Please input an adjective: ') 
animal = input('Please input name of an animal: ')
verb1 = input('Please input the first verb(present continuous tense): ')
exclamation1 = input('Please input an exclamation: ')
verb2 = input('Please input the second verb (present tense): ')
verb3 = input('Please input the third verb (present tense): ')
print()

words = f'''The other day, I was really in trouble.\nIt all started when I saw a very {adjective} {animal.capitalize()} {verb1} down the hallway.
         \n"{exclamation1.capitalize()}!" I yelled.\nBut all I could think to do was to {verb2} over and over.
         \nMiraculously,that caused it to stop, but not before it tried to {verb3} right in front of my family.'''

print(words)